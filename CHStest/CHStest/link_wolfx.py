import asyncio
import websockets
import json
import warning_window
import signal


# 存储地震信息的全局列表
earthquake_info = []


async def sc_eew_warning():
    uri = "wss://ws-api.wolfx.jp/sc_eew"
    try:
        async with websockets.connect(uri) as websocket:
            print("地震预警测试（仅二个）")
            await websocket.send('query_sceew')
            while True:
                warning_message = await websocket.recv()
                parsed_message = json.loads(warning_message)
                message_type = parsed_message.get('type')
                if message_type == 'heartbeat':
                    await websocket.send('ping')
                    print('ping')
                elif message_type == 'pong':
                    pass
                else:
                    print(f"四川地震局地震预警: 震级: {parsed_message.get('Magunitude')}, 震源地: {parsed_message.get('HypoCenter')}")
                    warning_window.show_reminder(
                        f"四川地震局地震预警: 震级: {parsed_message.get('Magunitude')}, 震源地: {parsed_message.get('HypoCenter')}")
                    sceewjson = {
                        "name": parsed_message.get('type'),
                        "area": parsed_message.get('HypoCenter'),
                        "eqtime": parsed_message.get('OriginTime'),
                        "reportnum": parsed_message.get('ReportNum'),
                        "depth": 10,
                        "lat": parsed_message.get('Latitude'),
                        "lon": parsed_message.get('Longitude'),
                        "mag": parsed_message.get('Magunitude'),
                        # 修正后的烈度计算，考虑可能的None值并使用更合适的经验公式
                        "int": parsed_message.get('MaxIntensity'),
                        "eewtime": parsed_message.get('ReportTime')
                    }
                    earthquake_info.append(sceewjson)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"四川地震局连接关闭: {e}")
    except Exception as e:
        print(f"四川地震局发生异常: {e}")


async def fj_eew_warning():
    uri = "wss://ws-api.wolfx.jp/fj_eew"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send('query_fjeew')
            while True:
                warning_message = await websocket.recv()
                parsed_message = json.loads(warning_message)
                message_type = parsed_message.get('type')
                if message_type == 'heartbeat':
                    await websocket.send('ping')
                    print('ping')
                elif message_type == 'pong':
                    pass
                else:
                    print(f"福建地震局地震预警: 震级: {parsed_message.get('Magunitude')}, 震源地: {parsed_message.get('HypoCenter')}")
                    warning_window.show_reminder(f"福建地震局地震预警: 震级: {parsed_message.get('Magunitude')}, 震源地: {parsed_message.get('HypoCenter')}")
                    # 假设 parsed_message 是一个包含地震相关信息的字典
                    fjeewjson = {
                        "name": parsed_message.get('type'),
                        "area": parsed_message.get('HypoCenter'),
                        "eqtime": parsed_message.get('OriginTime'),
                        "reportnum": parsed_message.get('ReportNum'),
                        "depth": 10,
                        "lat": parsed_message.get('Latitude'),
                        "lon": parsed_message.get('Longitude'),
                        "mag": parsed_message.get('Magunitude'),
                        # 修正后的烈度计算，考虑可能的None值并使用更合适的经验公式
                        "int": 0.24 + (float(parsed_message.get('Magunitude', 0)) * 1.29),
                        "eewtime": parsed_message.get('ReportTime')
                    }
                    earthquake_info.append(fjeewjson)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"福建地震局连接关闭: {e}")
    except Exception as e:
        print(f"福建地震局发生异常: {e}")


def handle_exit(signum, frame):
    print("Exiting gracefully...")
    loop = asyncio.get_event_loop()
    # 这里可以添加更多的清理代码
    loop.stop()


if __name__ == "__main__":
    # 注册信号处理程序
    signal.signal(signal.SIGINT, handle_exit)
    # 同时运行两个异步任务
    async def main():
        await asyncio.gather(sc_eew_warning(), fj_eew_warning())

    asyncio.get_event_loop().run_until_complete(main())
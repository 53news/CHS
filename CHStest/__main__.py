# CHS/CHStest/CHStest/__main__.py
import asyncio
import signal
import link_wolfx
import main_gui
import main_gui_change

# 信号处理函数，用于优雅地退出程序
def handle_exit(signum, frame):
    print("Exiting gracefully...")
    loop = asyncio.get_event_loop()
    # 这里可以添加更多的清理代码
    loop.stop()

async def main():
    try:
        # 注册信号处理程序
        signal.signal(signal.SIGINT, handle_exit)

        # 同时运行两个异步任务
        await asyncio.gather(link_wolfx.sc_eew_warning(), link_wolfx.fj_eew_warning())

        # 启动主 GUI
        main_gui.start_main_gui()

        # 启动 GUI 变更任务
        await main_gui_change.start_gui_change()

    except Exception as e:
        print(f"发生异常: {e}")

if __name__ == "__main__":
    # 获取事件循环
    loop = asyncio.get_event_loop()
    try:
        # 运行主异步函数
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        # 关闭事件循环
        loop.close()
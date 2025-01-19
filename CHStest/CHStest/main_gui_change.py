import asyncio
import link_wolfx as lw
import main_gui as mg


async def start_gui_change():
    try:
        # 调用 fj_eew_warning 函数
        fjeew_task = asyncio.create_task(lw.fj_eew_warning())
        # 调用 sc_eew_warning 函数
        sceew_task = asyncio.create_task(lw.sc_eew_warning())

        fjeew = await fjeew_task
        if fjeew:
            fj_text = f"福建发震地区：{fjeew.get('HypoCenter')}"
        else:
            fj_text = "福建发震地区：无信息"
        mg.start_main_gui.label2.config(text=fj_text)

        sceew = await sceew_task
        if sceew:
            sc_text = f"四川发震地区：{sceew.get('HypoCenter')}"
        else:
            sc_text = "四川发震地区：无信息"
        mg.start_main_gui.label2.config(text=sc_text)
    except Exception as e:
        print(f"发生异常: {e}")


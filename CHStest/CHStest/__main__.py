import link_wolfx
import main_gui
import main_gui_change


def main():
    # 调用 link_wolfx 中的函数并等待返回值
    result = link_wolfx.sc_eew_warning()
    # 根据返回值进行处理，例如判断是否继续执行后续操作
    if result:
        main_gui.start_main_gui()
        main_gui_change.start_gui_change()


if __name__ == "__main__":
    main()

import win32gui


def check_window():
    hwnd = win32gui.FindWindow(None, "讯飞E听说中学-作业-首页")
    if hwnd != 0:
        return True
    else:
        return False


check_window()

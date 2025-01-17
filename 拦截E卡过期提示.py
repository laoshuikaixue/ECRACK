import win32gui
import win32con

hwnd = win32gui.FindWindow(None, "讯飞E听说中学-E卡提示")
win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)

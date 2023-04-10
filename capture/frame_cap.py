import os
import win32api
import win32con
import win32gui
import win32ui


def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width, height, left, top)


def screenshot_bmp(name="current_screen"):
    outdir = os.path.join(os.getcwd(), "results")
    hdesktop = win32gui.GetDesktopWindow()
    width, height, left, top = get_dimensions()
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()
    screen_shot = win32ui.CreateBitmap()
    screen_shot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screen_shot)
    mem_dc.BitBlt((0,0), (width,height), img_dc, (left,top), win32con.SRCCOPY)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    filename = os.path.join(outdir, f"{name}.bmp")
    screen_shot.SaveBitmapFile(mem_dc, filename)
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screen_shot.GetHandle())
    return filename


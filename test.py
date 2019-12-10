import random
import win32con
import win32clipboard as wincld
import PyHook3
import pythoncom
import linecache

def MouseSwitch():
    pass
def onMouseEvent(event):
    # 过滤鼠标移动
    if(event.MessageName != "mouse move"):
       print(event.MessageName)
    return True

def onKeyboardEvent(event):
    #输出按下的键
    print(event.Key)
    global Lmenu_press
    if(event.Key == "Lmenu"):
        Lmenu_press = True
    handle_key()
    return True

def getText():
    count = len(open('E:\\text.txt','rb').readlines())
    randomNum = random.randrange(1, count, 1)
    return linecache.getline('D:\\github\\fuck\\text.txt',randomNum)

def handle_key():
    global Lmenu_press
    if(Lmenu_press):
        wincld.OpenClipboard()
        wincld.EmptyClipboard()
        wincld.SetClipboardData(win32con.CF_UNICODETEXT, getText())
        print(getText())
        wincld.CloseClipboard()
        Lmenu_press = False
    # 一直监听事件 
def main():
    #创建管理器
    hm = PyHook3.HookManager()
    #监听键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    #监听鼠标
    #hm.MouseAll = onMouseEvent
    #hm.HookMouse()
    #循环监听
    pythoncom.PumpMessages()

if __name__ == '__main__':
    Lmenu_press = False
    main()
    

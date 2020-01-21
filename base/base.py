import time ,os
from datetime import datetime
import win32clipboard as w
import win32con
import win32api



class base(object):

    VK_CODE = {'enter': 0x0D, 'ctrl': 0x11, 'v': 0x56}

    def __int__(self,driver):
        self.driver=driver

# 页面操作基本方法
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

# 时间和新建文件夹基本方法

    def get_time(self):
        self.now = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    def get_screen_shot(self,module):
        time=self.get_time()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s' %(module,time)
        self.driver.get_screenshot_as_file(image_file)

#键盘操作基础用法
    def settex(self,str):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT ,str)
        w.CloseClipboard()

    def gettext(self):
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()
        return d

    def keyDown(self,keyName):
        win32api.keybd_event(self.VK_CODE[keyName], 0, 0, 0)

    def keyUp(self,keyName):
        win32api.keybd_event(self.VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

    def oneKey(self,key):
        self.keyDown(key)
        self.keyUp(key)

    def twoKeys(self,key1, key2):
        self.keyDown(key1)
        self.keyDown(key2)
        self.keyUp(key1)
        self.keyUp(key2)


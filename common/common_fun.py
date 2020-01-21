from base.base import base
import time

class common(base):

    def input(self,inputstr,*loc):
        return self.find_element(*loc).sendkeys(inputstr)

    def click(self,*loc):
        return self.find_element(*loc).click()

    def clear(self,*loc):
        return self.find_element(*loc).click()

    def open_url(self,url):
        return self.driver.get(url)

    def close_browser(self):
        try:
            self.driver.quit()
        except Exception as e:
            raise e

    def sleep(self,sec):
        return time.sleep(sec)


#一个桌面提示打卡的小程序

import time
import easygui
import datetime
from datetime import datetime

Hour=3600
def TiShi():
    count=0
    Button=easygui.msgbox("别忘记打卡",title="提示",ok_button="知道了")
    if Button!=0:
        time.sleep(Hour)
while True:
    now = datetime.now()
    hour=now.hour
    if hour==9 or hour==17:
       TiShi()


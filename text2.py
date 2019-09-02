from PyQt5.QtCore import QTimer

timer = QTimer()
#设置计时间隔并启动(1000ms == 1s)
timer.start(1000)
#计时结束调用timeout_slot()方法,注意不要加（）
timer.timeout.connect(timeout_slot)

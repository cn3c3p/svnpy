# encoding: UTF-8

isUI = False

import sys
import os
import ctypes
import platform

import vtPath
from vtEngine import MainEngine
if isUI:
    from uiMainWindow import *

# 文件路径名
path = os.path.abspath(os.path.dirname(__file__))
ICON_FILENAME = 'vnpy.ico'
ICON_FILENAME = os.path.join(path, ICON_FILENAME)

SETTING_FILENAME = 'VT_setting.json'
SETTING_FILENAME = os.path.join(path, SETTING_FILENAME)


# ----------------------------------------------------------------------
def initDeamon(mainEngine):
    # 定时关闭
    import threading
    waitSecond = 20  # 秒
    print(u"close after %s sec  ..." % waitSecond)
    def closeServe():
        print(u"time to close vnpy ...")
        mainEngine.exit()
    threading.Timer(waitSecond, closeServe).start()

    # 建立 CTP 链接
    mainEngine.dbConnect()
    mainEngine.connect("CTP")


def main():
    """主程序入口"""
    # 重载sys模块，设置默认字符串编码方式为utf8
    reload(sys)
    sys.setdefaultencoding('utf8')

    mainEngine = MainEngine()

    if isUI:
        # 设置Windows底部任务栏图标
        if 'Windows' in platform.uname():
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('vn.trader')

        # 初始化Qt应用对象
        app = QtGui.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon(ICON_FILENAME))
        app.setFont(BASIC_FONT)

        # 设置Qt的皮肤
        try:
            f = file(SETTING_FILENAME)
            setting = json.load(f)
            if setting['darkStyle']:
                import qdarkstyle
                app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
        except:
            pass

        # 初始化主引擎和主窗口对象
        mainWindow = MainWindow(mainEngine, mainEngine.eventEngine)
        mainWindow.showMaximized()

        # 初始化实例的业务
        initDeamon(mainEngine)

        # 在主线程中启动Qt事件循环
        sys.exit(app.exec_())
    else:
        initDeamon(mainEngine)


if __name__ == '__main__':
    main()

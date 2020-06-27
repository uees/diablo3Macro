import threading

from pynput import keyboard

from army import ZhuDongSanGuang
from core import state


class Hotkey(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.listener = None

    def run(self):
        self.listener = keyboard.GlobalHotKeys({
            '<f1>': self.on_f1,
            '<ctrl>+<alt>+i': self.on_activate_i,
            '<ctrl>+<esc>': self.terminate,
        })
        self.listener.start()
        self.listener.join()

    def terminate(self):
        self.listener.stop()

    def on_f1(self):
        # 正在运行 则 关闭
        if state.is_run and state.name == ZhuDongSanGuang.__name__:
            state.is_run = False
            return

        print(f"run {ZhuDongSanGuang.__name__}")

        # 设置 State
        state.is_run = True
        state.name = ZhuDongSanGuang.__name__

        bot = ZhuDongSanGuang(name=ZhuDongSanGuang.__name__)
        bot.setDaemon(True)
        bot.start()

    def on_activate_i(self):
        print('<ctrl>+<alt>+i pressed')

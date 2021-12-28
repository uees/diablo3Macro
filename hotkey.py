import keyboard

from core import BOT_SWITCH
from logger import logger
from settings import HOT_KEY


class Hotkey(object):

    def __init__(self, bot):
        self.is_running = False
        self.bot = bot
        self.bot.daemon = True
        self.bot.start()

    def toggle(self):
        self.is_running = not self.is_running
        if BOT_SWITCH.is_set():
            BOT_SWITCH.clear()
        else:
            BOT_SWITCH.set()

    def run(self):
        logger.info(f"脚本启用状态：{BOT_SWITCH.is_set()}")
        self.start()
        keyboard.wait()

    def start(self):
        keyboard.add_hotkey(HOT_KEY, self.handle)

    def restart(self):
        keyboard.unhook_all()
        self.start()

    def handle(self):
        if not self.is_running:
            logger.info(f"running {self.bot.name} {self.bot.__module__}")
        else:
            self.restart()

        self.toggle()
        logger.info(f"脚本启用状态：{BOT_SWITCH.is_set()}")

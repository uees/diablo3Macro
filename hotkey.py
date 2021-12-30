import keyboard
from playsound import playsound

from almighty_ring import AlmightyRing
from core import BOT_SWITCH, RING_SWITCH
from logger import logger
from settings import HOT_KEY, RING_KEY, BASE_DIR, EXIT_KEY


class Hotkey(object):

    def __init__(self):
        self.is_running = False
        self.bot = None

    def load_bot(self, bot):
        self.bot = bot
        self.bot.daemon = True
        self.bot.start()

    def load_ring_sound(self):
        ring = AlmightyRing()
        ring.daemon = True
        ring.start()

    def toggle(self):
        self.is_running = not self.is_running
        if BOT_SWITCH.is_set():
            BOT_SWITCH.clear()
            playsound(f"{BASE_DIR}/resources/bot_end.mp3")
        else:
            BOT_SWITCH.set()
            playsound(f"{BASE_DIR}/resources/bot_start.mp3")

    def run(self):
        if self.bot:
            logger.info(f"脚本启用状态：{BOT_SWITCH.is_set()}")
            keyboard.add_hotkey(HOT_KEY, self.handle_bots)

        self.load_ring_sound()
        logger.info(f"全能法戒提示启用状态：{RING_SWITCH.is_set()}")
        keyboard.add_hotkey(RING_KEY, self.handle_ring)

        keyboard.wait(EXIT_KEY)

    def handle_bots(self):
        if not self.is_running:
            logger.info(f"running {self.bot.name} {self.bot.__module__}")

        self.toggle()
        logger.info(f"脚本启用状态：{BOT_SWITCH.is_set()}")

    def handle_ring(self):
        if RING_SWITCH.is_set():
            RING_SWITCH.clear()
            playsound(f"{BASE_DIR}/resources/ring_off.mp3")
        else:
            RING_SWITCH.set()

        logger.info(f"全能法戒提示启用状态：{RING_SWITCH.is_set()}")

from pynput import keyboard

from almighty_ring import AlmightyRing
from core import BOT_SWITCH, RING_SWITCH, BaseAsyncBot
from logger import logger
from settings import HOT_KEY, RING_KEY, BASE_DIR, EXIT_KEY
import pygame


class Hotkey(object):

    def __init__(self):
        self.is_running = False
        self.bot = None
        self.listener = None
        self.ring_cycle = 16
        # 初始化pygame mixer
        pygame.mixer.init()

    def run(self):
        if self.bot:
            logger.info(f"脚本启用状态：{BOT_SWITCH.is_set()}")

        self.load_ring_sound()
        logger.info(f"全能法戒提示启用状态：{RING_SWITCH.is_set()}")

        # 启动键盘监听
        self.listener = keyboard.Listener(
            on_press=self.on_key_press
        )
        self.listener.start()
        self.listener.join()

    def set_ring_cycle(self, cycle):
        self.ring_cycle = cycle

    def on_key_press(self, key):
        # 处理按键事件
        try:
            # 检查是否是热键（F2）
            if hasattr(key, 'name') and key.name == HOT_KEY.lower():
                self.handle_bots()
            # 检查是否是法戒键（F3）
            elif hasattr(key, 'name') and key.name == RING_KEY.lower():
                self.handle_ring()
            # 检查是否是退出键（F12）
            elif hasattr(key, 'name') and key.name == EXIT_KEY.lower():
                # 停止监听
                if self.listener:
                    self.listener.stop()
                logger.info("程序已退出")
        except Exception as e:
            logger.error(f"按键处理错误: {e}")

    def load_bot(self, bot: BaseAsyncBot):
        self.bot = bot
        self.bot.daemon = True
        self.bot.start()

    def load_ring_sound(self):
        ring = AlmightyRing()
        ring.set_cycle(self.ring_cycle)
        ring.daemon = True
        ring.start()

    def toggle(self):
        self.is_running = not self.is_running
        if BOT_SWITCH.is_set():
            BOT_SWITCH.clear()
            sound = pygame.mixer.Sound(f"{BASE_DIR}/resources/bot_end.mp3")
            sound.play()
        else:
            BOT_SWITCH.set()
            sound = pygame.mixer.Sound(f"{BASE_DIR}/resources/bot_start.mp3")
            sound.play()

    def handle_bots(self):
        if not self.is_running and self.bot is not None:
            logger.info(f"running {self.bot.name} {self.bot.__module__}")

        self.toggle()
        logger.info(f"脚本启用状态：{BOT_SWITCH.is_set()}")

    def handle_ring(self):
        if RING_SWITCH.is_set():
            RING_SWITCH.clear()
            sound = pygame.mixer.Sound(f"{BASE_DIR}/resources/ring_off.mp3")
            sound.play()
        else:
            RING_SWITCH.set()

        logger.info(f"全能法戒提示启用状态：{RING_SWITCH.is_set()}")

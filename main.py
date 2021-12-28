import argparse

from logger import logger
from hotkey import Hotkey


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bot", required=True, help="脚本名称")
    args = parser.parse_args()

    try:
        bot_module = __import__(args.bot, fromlist=('PressKey',))
        bot = bot_module.PressKey()
        h = Hotkey(bot)
        h.run()
    except ModuleNotFoundError as e:
        logger.error(e)


if __name__ == "__main__":
    run()

import argparse

from logger import logger
from hotkey import Hotkey
from utils import get_all_bots


def main():
    all_bots = ", ".join(get_all_bots())
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bot", help=f"Available bots: {all_bots}")
    args = parser.parse_args()

    h = Hotkey()
    if args.bot:
        try:
            bot_module = __import__(f"bots.{args.bot}", fromlist=('PressKey',))
            bot = bot_module.PressKey()
            h.load_bot(bot)
        except ModuleNotFoundError as e:
            logger.error(e)

    h.run()


if __name__ == "__main__":
    main()

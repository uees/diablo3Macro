import argparse

from logger import logger
from hotkey import Hotkey
from utils import get_all_bots


def main():
    all_bots = ", ".join(get_all_bots())
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bot", help=f"Available bots: {all_bots}")
    parser.add_argument(
        "-c", "--cdr", help="CDR time in seconds", type=float, default=10)
    parser.add_argument(
        "-r", "--ring12", help="12s ring", action="store_true")
    args = parser.parse_args()

    h = Hotkey()
    if args.ring12:
        h.set_ring_cycle(12)
    if args.bot:
        try:
            bot_module = __import__(f"bots.{args.bot}", fromlist=('PressKey',))
            bot = bot_module.PressKey()
            bot.set_cdr(args.cdr)
            h.load_bot(bot)
        except ModuleNotFoundError as e:
            logger.error(e)

    h.run()


if __name__ == "__main__":
    main()

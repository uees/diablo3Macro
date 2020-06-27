from hotkey import Hotkey


def run():
    hotkey = Hotkey(name="Thread-DiabloHotkey")
    hotkey.setDaemon(True)
    hotkey.start()
    hotkey.join()


if __name__ == "__main__":
    run()

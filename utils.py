import os
import glob
import ctypes
import inspect

from settings import BASE_DIR


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def get_all_bots():
    bots = []
    for file in glob.glob(f"{BASE_DIR}/bots/*.py"):
        filename = os.path.basename(file)
        if filename != "__init__.py":
            bot, _ = os.path.splitext(filename)
            bots.append(bot)

    return bots

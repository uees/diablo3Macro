import asyncio
import threading


class BaseAsyncBot(threading.Thread):

    def __init__(self, name: str):
        super().__init__(name=name)

    @property
    def is_run(self):
        return state.name == self.__class__.__name__ and state.is_run

    def run(self):
        self.run_loop()

    def get_tasks(self):
        tasks = []
        for attr in dir(self):
            if attr.startswith("task_"):
                tasks.append(getattr(self, attr)())

        return tasks

    def run_loop(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = self.get_tasks()
        loop.run_until_complete(asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED))
        loop.close()


class BotState(object):
    def __init__(self, name: str, is_run: bool):
        self.name = name
        self.is_run = is_run


state = BotState(None, False)

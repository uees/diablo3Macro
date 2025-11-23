from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """僵尸熊 python main.py -b wd_bear
    1: 灵魂行走 - 撞魂
    2: 灵魂收割 - 困魂压迫
    3: 王者之墙 - 尸墙
    4: 惧灵 - 骇人仪容

    left: 瘟疫虫群 - 剧毒虫群
    right: 僵尸死士 - 僵尸熊
    被动: 沼泽调谐、欺瞒仪式、剥削死者、死亡蔓延
    """

    async def task_press_4(self):
        """ 王者之墙 - 尸墙 buff 8s """
        await self.loop_press('4', 7)

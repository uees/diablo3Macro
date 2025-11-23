from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """王者大军 python main.py -r -b nec_dajun
    1: 鲜血奔行 - 鲜血潜能
    2: 亡魂复生 - 亡魂护体
    3: 骨甲 - 白骨脱臼
    4: 号令骸骨 - 死寒之握
    left: 王者大军 - 死亡之谷
    right: 鲜血虹吸 - 强力相移

    被动: 绝命效忠、畸变复生、鲜血之力、死酱灾疫
    """

    async def task_press_4(self):
        """ 号令骸骨 - 死寒之握 """
        await self.loop_press('4', 0.3)

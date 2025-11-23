from core import BaseAsyncBot


class PressKey(BaseAsyncBot):
    """万箭归宗 python main.py -r -b nec_money
    left: 王者领域 - 死寒之地
    right: 鲜血虹吸 - 强力相移
    1: 鲜血奔行 - 鲜血潜能
    2: 尸矛 - 血污之矛
    3: 吞噬 - 吞血食肉
    4: 号令骸骨 - 死寒之握

    被动: 绝命效忠、王者滋养、鲜血之力、亡魂灌注
    """

    async def task_press_3(self):
        """ 吞噬 - 吞血食肉 """
        await self.loop_press('3', 0.3)

    async def task_press_4(self):
        """ 号令骸骨 - 死寒之握 """
        await self.loop_press('4', 0.3)

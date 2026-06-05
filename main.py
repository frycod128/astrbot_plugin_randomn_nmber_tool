from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Optional

from astrbot.api import FunctionTool
from astrbot.api.star import Star, Context
from astrbot.core.agent.tool import ToolExecResult


@dataclass
class RandomNumberTool(FunctionTool):
    name: str = "generate_random_number"
    description: str = (
        "生成指定范围内的随机数。支持设置上下界和小数位数。"
    )
    parameters: dict = field(default_factory=lambda: {
        "type": "object",
        "properties": {
            "lower_bound": {
                "type": "number",
                "description": "随机数下界（最小值），默认为0",
                "default": 0
            },
            "upper_bound": {
                "type": "number",
                "description": "随机数上界（最大值），默认为100",
                "default": 100
            },
            "decimal_places": {
                "type": "integer",
                "description": "小数位数，0表示整数，默认为0",
                "default": 0,
                "minimum": 0,
                "maximum": 10
            }
        }
    })

    async def call(
            self,
            context,
            lower_bound: Optional[float] = None,
            upper_bound: Optional[float] = None,
            decimal_places: Optional[int] = None
    ) -> ToolExecResult:
        lower = lower_bound if lower_bound is not None else 0
        upper = upper_bound if upper_bound is not None else 100
        decimals = decimal_places if decimal_places is not None else 0

        try:
            decimals = int(decimals)
            if decimals < 0:
                decimals = 0
            if decimals > 10:
                decimals = 10
        except (ValueError, TypeError):
            decimals = 0

        try:
            lower = float(lower)
            upper = float(upper)
        except (ValueError, TypeError):
            lower = 0.0
            upper = 100.0

        if lower > upper:
            lower, upper = upper, lower

        if decimals == 0:
            random_num = random.randint(int(lower), int(upper))
            result_str = str(random_num)
            result_num = random_num
        else:
            random_num = random.uniform(lower, upper)
            result_num = round(random_num, decimals)
            result_str = f"{result_num:.{decimals}f}"

        message = f"随机数范围：[{lower}, {upper}]\n小数位数：{decimals}\n结果：{result_str}"

        return ToolExecResult(
            content=message,
            data={
                "success": True,
                "value": result_num,
                "value_str": result_str,
                "lower_bound": lower,
                "upper_bound": upper,
                "decimal_places": decimals
            }
        )


class RandomNumberPlugin(Star):
    name = "random_number_plugin"
    version = "v1.0.2"
    description = "随机数生成工具插件"

    def __init__(self, context: Context):
        super().__init__(context)
        self.context.add_llm_tools(RandomNumberTool())
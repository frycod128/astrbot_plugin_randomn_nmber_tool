from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from typing import Optional

import mcp
from astrbot.api import FunctionTool
from astrbot.api.star import Star, Context


@dataclass
class RandomNumberTool(FunctionTool):
    name: str = "generate_random_number"
    description: str = (
        "生成指定范围内的随机数。支持设置上下界、小数位数和生成数量。"
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
            },
            "count": {
                "type": "integer",
                "description": "生成随机数的数量，默认为1",
                "default": 1,
                "minimum": 1
            }
        }
    })

    async def call(
            self,
            context,
            lower_bound: Optional[float] = None,
            upper_bound: Optional[float] = None,
            decimal_places: Optional[int] = None,
            count: Optional[int] = None
    ) -> mcp.types.CallToolResult:
        # 参数处理：使用默认值或传入的值
        lower = lower_bound if lower_bound is not None else 0
        upper = upper_bound if upper_bound is not None else 100
        decimals = decimal_places if decimal_places is not None else 0
        cnt = count if count is not None else 1

        # 验证并修正小数位数
        try:
            decimals = int(decimals)
            if decimals < 0:
                decimals = 0
            if decimals > 10:
                decimals = 10
        except (ValueError, TypeError):
            decimals = 0

        # 验证并修正数量
        try:
            cnt = int(cnt)
            if cnt < 1:
                cnt = 1
        except (ValueError, TypeError):
            cnt = 1

        # 验证数值有效性
        try:
            lower = float(lower)
            upper = float(upper)
        except (ValueError, TypeError):
            lower = 0.0
            upper = 100.0

        # 交换上下界（如果下界大于上界）
        if lower > upper:
            lower, upper = upper, lower

        # 生成随机数列表
        result_list = []
        for _ in range(cnt):
            if decimals == 0:
                # 生成整数
                num = random.randint(int(lower), int(upper))
            else:
                # 生成小数
                num = round(random.uniform(lower, upper), decimals)
            result_list.append(num)

        # 格式化输出
        if cnt == 1:
            message = f"随机数：{result_list[0]}（范围：{lower} ~ {upper}，小数位数：{decimals}）"
        else:
            message = f"随机数列表：{result_list}（范围：{lower} ~ {upper}，小数位数：{decimals}，数量：{cnt}）"

        # 返回结果
        return mcp.types.CallToolResult(
            content=[
                mcp.types.TextContent(
                    type="text",
                    text=json.dumps({
                        "success": True,
                        "values": result_list,
                        "count": cnt,
                        "lower_bound": lower,
                        "upper_bound": upper,
                        "decimal_places": decimals
                    }, ensure_ascii=False)
                )
            ]
        )


# 插件主类
class RandomNumberPlugin(Star):
    name = "random_number_plugin"
    version = "v1.1.1"
    description = "随机数生成工具插件"

    def __init__(self, context: Context):
        super().__init__(context)
        context.add_llm_tools(RandomNumberTool())

    async def terminate(self):
        pass
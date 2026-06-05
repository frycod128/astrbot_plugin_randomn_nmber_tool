# 随机数生成工具 (RandomNumberTool)

## 功能

生成指定范围内的随机数，支持整数和浮点数。

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| lower_bound | number | 0 | 下界（最小值） |
| upper_bound | number | 100 | 上界（最大值） |
| decimal_places | integer | 0 | 小数位数（0-10，0=整数） |

## 特性

- 参数缺失时自动使用默认值
- 下界 > 上界时自动交换
- 无效参数自动回退到默认值
- 返回显示文本 + 结构化数据

## 示例

```python
# 整数随机数 (1-10)
await tool.call(lower_bound=1, upper_bound=10)

# 浮点数随机数 (0-1, 保留2位小数)
await tool.call(upper_bound=1, decimal_places=2)

# 自动交换 (等价于 1-10)
await tool.call(lower_bound=10, upper_bound=1)
```

### 返回值

```python
ToolExecResult(
    content="随机数范围：[0, 10]\n结果：7",
    data={
        "success": True,
        "value": 7,
        "value_str": "7",
        "lower_bound": 0,
        "upper_bound": 10,
        "decimal_places": 0
    }
)
```
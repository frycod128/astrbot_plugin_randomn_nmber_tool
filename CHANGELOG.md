# 随机数生成工具插件
# 更新日志

## v1.1.1

### 修复
- 去除冗余的 `result_str`

---

## v1.1.0

### 变更
- 新增 `count` 参数
- 现在支持随机数批量生成

---

## v1.0.3

### 修复
- 修正工具调用返回类型错误
- 将 `ToolExecResult` 替换为正确的 `mcp.types.CallToolResult`
- 修复 `'types.UnionType' object is not callable` 错误

### 变更
- 返回格式改为 MCP 标准格式
- 简化返回消息内容

---

## v1.0.2

### 修复
- 修正插件注册方式
- 将 `context.register_tool()` 改为 `context.add_llm_tools()`
- 修复 `'Context' object has no attribute 'register_tool'` 错误

---

## v1.0.1

### 修复
- 添加插件主类 `RandomNumberPlugin` 继承 `Star`
- 修复插件未通过 Star 注册的错误

### 变更
- 添加 `__init__.py` 文件标识 Python 包

---

## v1.0.0

### 新增
- 初始版本发布
- 实现随机数生成功能
- 支持三个参数：
  - `lower_bound`：下界（默认 0）
  - `upper_bound`：上界（默认 100）
  - `decimal_places`：小数位数（默认 0）
- 特性：
  - 参数缺失时自动使用默认值
  - 下界大于上界时自动交换
  - 无效参数自动回退默认值
  - 支持整数和浮点数随机数

---

## 当前版本信息

| 项目 | 内容 |
|------|------|
| 最新版本 | v1.0.3 |
| 状态 | ✅ 稳定 |
| 插件名 | `astrbot_plugin_randomn_nmber_tool` |
| 工具名 | `generate_random_number` |
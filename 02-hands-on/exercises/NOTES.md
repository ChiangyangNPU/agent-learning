# 练习手记（坑本）

> 每做完一个练习追加一节：怎么做的、观察到了什么、踩了什么坑。
> 这些记录是整个仓库最值钱的产出——面试和实战里能讲出来的经验都从这里来。

## 练习①：单轮工具调用（2026-09-19）

**代码**：[ex1_single_tool_call.py](ex1_single_tool_call.py)

**实现要点**：

- 一次"单轮工具调用"其实是**两次 API 调用**：第 1 次带上 messages + tools，模型返回的不是答案而是 tool_calls（调用意图）；本地执行函数后，把结果作为 `role=tool` 的消息喂回，第 2 次调用模型才给出自然语言回答
- messages 列表是完整对话的账本，四种角色各司其职：system（约束）/ user（任务）/ assistant（含 tool_calls）/ tool（含 tool_call_id）。缺一条或 id 对不上，API 直接报错
- 客户端用 openai SDK 换 `base_url` 直连 OpenAI / DeepSeek / 智谱 GLM——Function Calling 的接口已事实标准化，这也是"框架没有魔法"的第一个证据

**验证记录**：本机暂无 API key，代码流程已用桩客户端（fake client）离线验证通过：两次调用的消息列表为 `[system, user, assistant, tool]`、assistant 消息原对象回传、tool_call_id 正确配对。**真实 API 的返回样例待跑通后补记在这里。**

**待观察**（跑通真实 API 后回答）：

- [ ] 模型返回的 tool_calls JSON 长什么样？`id`、`name`、`arguments` 各是什么格式？
- [ ] 换成"上海今天多少度？"这种说法，参数还是合法 JSON 吗？
- [ ] 故意把 description 删掉会怎样？（对应坑清单第 1 条）

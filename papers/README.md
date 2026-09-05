# 论文库

路线中涉及的论文原文，已从 arXiv 官方下载。**不要按顺序全读**——每篇只对应学习路线的某个阶段，按下面标出的阶段和重点读。

## 阅读顺序（对应学习路线）

| 阶段 | 论文 | 文件 | 怎么读 |
|------|------|------|--------|
| 一 | [ReAct (2022)](https://arxiv.org/abs/2210.03629) | [ReAct_2210.03629.pdf](ReAct_2210.03629.pdf) | **只需精读第 2 节和图 1**，理解"思考→行动→观察"循环即可，实验部分可跳过 |
| 一 | [Toolformer (2023)](https://arxiv.org/abs/2302.04761) | [Toolformer_2302.04761.pdf](Toolformer_2302.04761.pdf) | 选读。看摘要和图 1 即可：模型自学在何处插入 API 调用 |
| 二后 | [Reflexion (2023)](https://arxiv.org/abs/2303.11366) | [Reflexion_2303.11366.pdf](Reflexion_2303.11366.pdf) | 选读。Reflection 模式的来源：把失败反馈转成语言化的自我反思 |
| 三后 | [Tree of Thoughts (2023)](https://arxiv.org/abs/2305.10601) | [Tree_of_Thoughts_2305.10601.pdf](Tree_of_Thoughts_2305.10601.pdf) | 选读。了解"树状探索多种推理路径"的思想即可，工程中少直接用 |
| 四 | [SWE-agent / ACI (2024)](https://arxiv.org/abs/2405.15793) | [SWE-agent_ACI_2405.15793.pdf](SWE-agent_ACI_2405.15793.pdf) | **做项目 4 之前精读**。Agent-Computer Interface：为 Agent 设计工具如同为人设计 UI |

另有非论文但同样重要的两份指南（在路线中优先级高于所有论文）：

- [OpenAI《A Practical Guide to Building Agents》](OpenAI_A_Practical_Guide_to_Building_Agents.pdf) —— 阶段一阅读
- Anthropic《Building Effective Agents》是网页文章，链接见 [resources.md](../resources.md)，建议收藏网页原文

## 一个建议

读论文时在旁边放一个空文档，每读完一篇只写三行：它解决什么问题 / 核心方法一句话 / 对我写 Agent 的启发。这个习惯比"读懂每个细节"有价值得多。

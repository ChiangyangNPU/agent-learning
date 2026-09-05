# 资料索引

> 按用途分类，标注了对应的学习阶段。**不要先收藏再全部读完**——够用就开写。

## 核心文章（阶段一）

| 资料 | 阶段 | 说明 |
|------|------|------|
| [Anthropic《Building Effective Agents》](https://www.anthropic.com/engineering/building-effective-agents) | 一 | 最重要。Workflow vs Agent、五种常见模式、何时不用框架（[已转存本地副本](papers/Building_Effective_Agents_Anthropic.md)） |
| [OpenAI《A Practical Guide to Building Agents》](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | 一 | 产品视角，适合补充 |
| [12-factor agents](https://github.com/humanlayer/12-factor-agents) | 四 | 12 条 Agent 工程原则，每条都有代码级解释 |
| [Anthropic《Effective Context Engineering for AI Agents》](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 三 | 上下文工程的权威文章 |

## 奠基论文（阶段一、四，按优先级）

| 论文 | 年份 | 一句话 |
|------|------|--------|
| [ReAct (arXiv:2210.03629)](https://arxiv.org/abs/2210.03629) | 2022 | 思考-行动-观察循环，几乎所有 Agent 的骨架 |
| [Toolformer (arXiv:2302.04761)](https://arxiv.org/abs/2302.04761) | 2023 | 模型自学何时调用工具的早期工作 |
| [Reflexion (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366) | 2023 | 语言化自我反思（Reflection 模式的来源） |
| [SWE-agent / ACI (arXiv:2405.15793)](https://arxiv.org/abs/2405.15793) | 2024 | Agent-Computer Interface：为 Agent 设计工具如同为人设计 UI |
| [Tree of Thoughts (arXiv:2305.10601)](https://arxiv.org/abs/2305.10601) | 2023 | 树状探索多种推理路径（了解即可） |

## 动手实践（阶段二）

| 资料 | 说明 |
|------|------|
| [OpenAI Cookbook: Function Calling](https://cookbook.openai.com/examples/function_calling_with_databases) | 官方的工具调用示例 |
| [Anthropic Docs: Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) | 接口设计得最清晰 |
| [智谱 GLM API 文档](https://docs.bigmodel.cn/) / [DeepSeek API 文档](https://api-docs.deepseek.com/) | 国内可直连的选择 |
| [OpenRouter](https://openrouter.ai/) | 一个 Key 用多家模型，适合练习 |

## MCP（阶段三）

| 资料 | 说明 |
|------|------|
| [MCP 官方文档](https://modelcontextprotocol.io) | 从 Quickstart 开始 |
| [MCP 规范](https://spec.modelcontextprotocol.io) | 想深入协议再看 |
| [Python SDK](https://github.com/modelcontextprotocol/python-sdk) / [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 写自己的 Server |
| [官方 Servers 合集](https://github.com/modelcontextprotocol/servers) | 文件系统、GitHub、数据库等现成实现，读它们的源码学习 |

## 框架（阶段四）

| 资料 | 说明 |
|------|------|
| [LangGraph 文档](https://langchain-ai.github.io/langgraph/) | 状态图模型，看 Quickstart + Why LangGraph |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | 轻量，重点看 Handoff 和 Guardrail |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 完整开源软件工程 Agent |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | 学术严谨，源码干净 |

## 课程（系统化学习用）

| 课程 | 说明 |
|------|------|
| [HuggingFace Agents Course](https://huggingface.co/learn/agents-course) | 免费，从基础到多 Agent，有证书 |
| [DeepLearning.AI 短课程](https://www.deeplearning.ai/courses/) | 搜 "Agents"、"Function Calling"，每个 1~2 小时 |
| [MCP 官方教程](https://modelcontextprotocol.io/tutorials) | 写 Server 的手把手教程 |

## 评测（阶段三）

| 资料 | 说明 |
|------|------|
| [OpenAI Evals](https://github.com/openai/evals) | 评测框架 |
| [LangSmith 文档](https://docs.smith.langchain.com/) | 评测与轨迹追踪平台（收费，看概念即可） |
| Anthropic Docs: [Test & Evaluate](https://docs.anthropic.com/en/docs/test-and-evaluate) | 评测方法论 |

## 保持信息更新的渠道

- Anthropic Engineering Blog（`anthropic.com/engineering`）—— Agent 实践文章质量最高
- OpenAI Cookbook（`cookbook.openai.com`）
- HN / Twitter 上搜索 "agents" 的一线工程师讨论
- **最重要**：自己动手时遇到的问题，去读框架源码而不是只搜教程

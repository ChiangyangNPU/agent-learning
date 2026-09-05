# Agent 学习路线

> 预计总时长 6~9 周（业余时间），可按基础快进或跳过。
> 核心方法：**用中学**——每学一个概念，立刻动手验证它。

## 总览

```mermaid
flowchart LR
    subgraph S1["阶段一 · 理解本质"]
        A1[Workflow vs Agent] --> A2[ReAct 循环] --> A3[读两篇指南]
    end
    subgraph S2["阶段二 · 徒手实现"]
        B1[Function Calling] --> B2[多轮循环] --> B3[记忆与重试]
    end
    subgraph S3["阶段三 · 关键概念"]
        C1[MCP] --> C2[上下文工程] --> C3[评测]
    end
    subgraph S4["阶段四 · 框架与源码"]
        D1[LangGraph] --> D2[Agents SDK] --> D3[读开源源码]
    end
    S1 ==> S2 ==> S3 ==> S4
```

---

## 阶段一：理解本质（1~2 周）

**目标**：建立正确的心智模型。Agent = 在循环中使用工具的 LLM。

要搞清楚的问题：

1. **Workflow 和 Agent 的区别是什么？**
   - Workflow：开发者预先编排好代码执行路径，LLM 只是其中的环节（可控、便宜、可预测）
   - Agent：LLM 自己决定下一步做什么、用哪个工具、何时结束（灵活、贵、不可预测）
   - **关键结论：能用 Workflow 解决的问题不要上 Agent**
2. **ReAct 循环是什么？** 模型交替进行「思考（Reason）→ 行动（Act）→ 观察（Observe）」
3. **工具调用（Function Calling）的底层机制是什么？** 并不是模型真的"执行"了函数——模型只是输出一段结构化的 JSON 表达意图，由你的代码负责执行并把结果喂回去

详见 [01-fundamentals/README.md](01-fundamentals/README.md)

**必读资料**：
- Anthropic《Building Effective Agents》
- OpenAI《A Practical Guide to Building Agents》
- ReAct 论文（arXiv: 2210.03629）

**验收标准**：能用自己的话向别人解释清楚"Agent 循环"和"为什么不需要框架也能写出 Agent"。

---

## 阶段二：徒手写一个最小 Agent（1~2 周）⭐ 最重要

**目标**：不借助任何框架，只用 LLM API 手写一个能用的 Agent。这一步的价值在于彻底理解框架帮你封装了什么。

动手清单（循序渐进）：

```mermaid
flowchart TD
    T1["① 单轮工具调用<br/>让模型查一次天气"] --> T2["② 加 while 循环<br/>模型可连续调用工具直到任务完成"]
    T2 --> T3["③ 多工具 + 系统提示词<br/>设计工具描述让模型选对工具"]
    T3 --> T4["④ 错误处理与重试<br/>工具报错时把错误信息喂回模型"]
    T4 --> T5["⑤ 对话记忆<br/>维护 messages 列表实现多轮任务"]
```

三个关键的实战经验（都会在做题过程中踩到）：

1. **工具描述比模型聪明更重要**——模型选工具几乎完全依赖工具的 name / description / 参数说明
2. **错误也是信息**——工具执行失败时，把报错文本喂回模型，模型经常能自己修正
3. **必须有终止条件**——最大循环轮数、明确的"任务完成"信号，否则会烧钱死循环

详见 [02-hands-on/README.md](02-hands-on/README.md)（含参考代码骨架）

**验收标准**：不看教程，从空文件开始 30 分钟内写出一个可用的工具调用循环。

---

## 阶段三：补齐关键概念（2~3 周）

**目标**：掌握把玩具 Agent 变成可用产品所需的三块能力。

| 概念 | 要解决的问题 | 学习重点 |
|------|------------|---------|
| MCP | 工具接入的标准化 | 为什么需要统一协议、Server/Client 架构、写一个自己的 MCP Server |
| 上下文工程 | 有限窗口内塞进最有用信息 | 历史压缩、检索注入（RAG）、系统提示词分层 |
| 评测 | "感觉不错" → 可量化 | 任务成功率、轨迹评估、LLM-as-judge |

```mermaid
flowchart LR
    subgraph CE["上下文工程"]
        H[对话历史] -- 压缩/截断 --> CTX[上下文窗口]
        R[外部知识] -- RAG 检索 --> CTX
        SP[系统提示词] --> CTX
        T[工具结果] --> CTX
    end
```

RAG 的基本流水线：

```mermaid
flowchart LR
    D[原始文档] --> S[切分 Chunk] --> E[Embedding 向量化] --> VDB[(向量数据库)]
    Q[用户问题] --> E2[Embedding] --> VDB
    VDB --> TOP[取 Top-K 相关片段] --> LLM[拼入上下文交给 LLM] --> A[回答]
```

MCP 的架构：

```mermaid
flowchart LR
    H[Host 应用<br/>如 Claude Code] --> C[MCP Client]
    C <-->|协议通信| S1[MCP Server: 文件系统]
    C <-->|协议通信| S2[MCP Server: 数据库]
    C <-->|协议通信| S3[MCP Server: 你自己写的]
    S1 --> R1[本地资源]
    S3 --> R3[你的 API / 工具]
```

详见 [03-concepts/README.md](03-concepts/README.md)

**验收标准**：写出一个自己的 MCP Server 并在客户端里用起来；能说出自己项目的评测方案。

---

## 阶段四：框架原理与源码阅读（2 周）

**目标**：带着阶段二的理解去看框架，重点看"它把哪些东西抽象掉了"。

1. **LangGraph**：看它的状态图（StateGraph）和 checkpoint 机制——本质是把 Agent 循环显式建模成图
2. **OpenAI Agents SDK**：看它的 handoff（Agent 间交接）和 guardrails 设计
3. **读开源 Agent 源码**（选一个深入）：
   - [OpenHands](https://github.com/All-Hands-AI/OpenHands)：通用软件工程 Agent
   - [SWE-agent](https://github.com/SWE-agent/SWE-agent)： Princeton 的 SWE Agent，论文值得一读
   - [12-factor agents](https://github.com/humanlayer/12-factor-agents)：12 条构建可靠 Agent 的工程原则，强烈推荐

**验收标准**：能用阶段二的手写版复现某个框架的核心特性（比如子 Agent 委派）。

---

## 实战项目（贯穿全程）

详见 [projects/README.md](projects/README.md)。由易到难：

1. **命令行文件助手**——能读写本地文件的 Agent（简化版 Claude Code）
2. **网页信息搜集 Agent**——搜索 + 抓取 + 汇总成报告
3. **个人知识库问答**——加 RAG 的文档问答
4. **复刻 mini Claude Code**——理解任务、改代码、跑测试、根据报错自我修正

---

## 推荐的学习习惯

- **每天用 Agent 工具干活**（比如 ZCode），遇到它的行为就去想"内部是怎么实现的"，然后验证
- **建一个"坑本"**：把自己踩的坑（模型选错工具、循环不终止、上下文爆了……）记下来，这些就是面试和实战中最值钱的经验
- **不要收集资料上瘾**：资料够用就开写，写不下去再回来查

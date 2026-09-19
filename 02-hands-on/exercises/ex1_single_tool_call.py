"""阶段二 · 练习①：单轮工具调用（不用任何框架）

目标：只靠 LLM API 完成——注册一个 get_weather 工具，让模型调用一次并回答。

先建立预期（对应 01-fundamentals/README.md 第 3 节的结论）：
    模型从不执行函数。它只是输出一段结构化 JSON（tool_calls），
    表达"我想调 get_weather，参数是北京"这个意图；
    真正执行函数的是你的代码，把执行结果作为 tool 消息喂回去，
    模型才能基于真实结果生成最终回答。

一次完整运行 = 两次 API 调用：
    第 1 次：messages + tools   ->  模型返回 tool_calls（而不是答案）
    你在本地执行函数
    第 2 次：messages + tool 结果 ->  模型给出自然语言回答

运行前：配好任意一家的 key（接口同构，哪家有就用哪家）：
    export OPENAI_API_KEY=sk-...        # OpenAI
    export DEEPSEEK_API_KEY=sk-...      # DeepSeek
    export ZHIPUAI_API_KEY=...          # 智谱 GLM（open.bigmodel.cn）
    可选 export EX1_MODEL=...           # 覆盖该厂商的默认模型
然后：python3 ex1_single_tool_call.py
"""

import json
import os

from openai import OpenAI

# openai SDK 是通用客户端，换个 base_url 就能连不同厂商——
# 这也侧面说明 Function Calling 的接口已经事实标准化了。
PROVIDERS = [
    ("OPENAI_API_KEY", "https://api.openai.com/v1", "gpt-4o-mini"),
    ("DEEPSEEK_API_KEY", "https://api.deepseek.com", "deepseek-chat"),
    ("ZHIPUAI_API_KEY", "https://open.bigmodel.cn/api/paas/v4", "glm-4-flash"),
    ("Z_AI_API_KEY", "https://open.bigmodel.cn/api/paas/v4", "glm-4-flash"),
]


def make_client():
    """按环境变量选择厂商；EX1_MODEL 可覆盖默认模型。"""
    for env_name, base_url, model in PROVIDERS:
        key = os.environ.get(env_name)
        if key:
            return OpenAI(api_key=key, base_url=base_url), os.environ.get("EX1_MODEL", model)
    raise SystemExit(
        "未找到 API key。请先 export 任意一家："
        "OPENAI_API_KEY / DEEPSEEK_API_KEY / ZHIPUAI_API_KEY"
    )


# ---------- 第 1 步：工具就是一个普通的 Python 函数 ----------
def get_weather(city: str) -> str:
    """练习用假数据；真实场景这里才去调天气 API。"""
    return json.dumps({"city": city, "weather": "晴", "temp": "25°C", "air": "优"}, ensure_ascii=False)


# ---------- 第 2 步：把工具"注册"给模型（schema 描述） ----------
# ★ description 是模型选工具的唯一依据：写"什么时候该用我"，
#   而不是复述函数名。模型看不见函数体，只看得见这段 JSON。
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的当前天气。当用户问到天气相关问题时使用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名，如：北京"},
                },
                "required": ["city"],
            },
        },
    }
]
TOOL_IMPLS = {"get_weather": get_weather}  # 名字 -> 真正干活的函数


def main():
    client, model = make_client()

    messages = [
        {"role": "system", "content": "你是一个乐于助人的助手，可以使用工具。"},
        {"role": "user", "content": "北京今天天气怎么样？适合户外跑步吗？"},
    ]

    # ---------- 第 3 步：第 1 次调用 API ----------
    resp = client.chat.completions.create(model=model, messages=messages, tools=TOOLS)
    msg = resp.choices[0].message

    if not msg.tool_calls:
        # 模型没调工具就直接作答了？99% 是工具 description 太含糊，
        # 或用户消息没有触发场景（对照 02-hands-on/README.md 坑清单第 1 条）。
        print("模型没有调用工具，直接回答了：", msg.content)
        return

    # ★ assistant 的 tool_calls 消息必须 append 回去，消息列表才完整，
    #   否则第 2 次调用时 API 会报错（消息要能还原完整对话）。
    messages.append(msg)
    call = msg.tool_calls[0]  # 练习①只看第一个；多工具并行调用留给练习②
    print("① 模型想调用的工具:", call.function.name, "参数:", call.function.arguments)

    # ---------- 第 4 步：由你的代码真正执行函数 ----------
    args = json.loads(call.function.arguments)
    result = TOOL_IMPLS[call.function.name](**args)
    print("② 工具执行结果:", result)

    # ---------- 第 5 步：把结果作为 tool 消息喂回，第 2 次调用 API ----------
    # tool_call_id 必须和第 1 次返回的 id 对上，API 靠它配对请求和结果。
    messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
    final = client.chat.completions.create(model=model, messages=messages)
    print("③ 模型最终回答:", final.choices[0].message.content)


if __name__ == "__main__":
    main()

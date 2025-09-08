# smart-mcp

Generate high-quality **fine-tuning datasets for tool calling** from one or more **MCP (Model Context Protocol)** tool servers.  
`smart-mcp` scans your MCP endpoints, reads the available tools and historical calls, and synthesizes **natural-language prompts** that would reasonably lead a model to make each tool call. It emits training data in chat JSONL where the assistant turn includes a `tool_calls` record.

> Why? Supervised fine-tuning with realistic tool-calling traces can improve when/which tool the model picks and how it fills arguments. Your training examples should look as close to production as possible.

---

## ✨ What it does

- **Discovers tools** from multiple MCP servers (local or remote).
- **Ingests tool specs & past calls** (names, JSON schemas, example arguments, success traces).
- **Generates prompts** that naturally imply calling each tool (optionally multiple prompts per tool, varying phrasing and constraints).
- **Builds fine-tuning datapoints** in OpenAI-style chat format:
  - minimal pair _(user → assistant with `tool_calls`)_; or
  - full chain _(user → assistant `tool_calls` → `tool` response → assistant final)_.
- **Outputs**: `train_function_name.json`

---

## 📦 Output schema

Each line is a JSON object with a `messages` array (and optional `tools` block to mirror production). For the **minimal** variant:

```json
{
  "messages": [
    { "role": "user", "content": "What is the weather in San Francisco?" },
    {
      "role": "assistant",
      "tool_calls": [
        {
          "id": "call_id",
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "arguments": "{\"location\": \"San Francisco, USA\", \"format\": \"celsius\"}"
          }
        }
      ]
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather",
        "parameters": {
          "type": "object",
          "properties": {
            "location": { "type": "string" },
            "format": { "type": "string", "enum": ["celsius", "fahrenheit"] }
          },
          "required": ["location"]
        }
      }
    }
  ]
}
```

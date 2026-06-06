# 🛠️ AI Developer Tools

AI开发者工具，支持代码生成、调试、重构。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 💻 代码生成
- 🐛 代码调试
- ♻️ 代码重构
- 🔍 代码审查
- 🧪 测试生成
- 📖 代码解释

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_developer_tools import create_tools

tools = create_tools()

# 代码生成
code = tools.generate_code("斐波那契数列", "Python", "简洁")

# 代码调试
debug = tools.debug_code(code, "IndexError", "Python")

# 代码重构
refactored = tools.refactor_code(code, "提高性能", "Python")

# 代码审查
review = tools.review_code(code, "Python")

# 测试生成
tests = tools.generate_tests(code, "Python", "pytest")

# 代码解释
explanation = tools.explain_code(code, "Python", "beginner")
```

## 📁 项目结构

```
ai-developer-tools/
├── tools.py       # 开发者工具核心
└── README.md
```

## 📄 许可证

MIT License

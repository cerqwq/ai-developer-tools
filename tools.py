"""
AI Developer Tools - AI开发者工具
支持代码生成、调试、重构
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDeveloperTools:
    """
    AI开发者工具
    支持：生成、调试、重构
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_code(self, description: str, language: str, style: str = "clean") -> str:
        """生成代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{language}写以下代码：

描述：{description}
风格：{style}

要求：
1. 干净简洁
2. 类型提示
3. 文档字符串
4. 错误处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def debug_code(self, code: str, error: str, language: str) -> Dict:
        """调试代码"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请调试以下{language}代码：

代码：
```{language}
{code}
```

错误：{error}

请返回JSON格式：
{{
    "root_cause": "根因",
    "fix": "修复方案",
    "fixed_code": "修复后的代码",
    "prevention": "预防措施"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"debug": content}

    def refactor_code(self, code: str, goal: str, language: str) -> str:
        """重构代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请重构以下{language}代码：

代码：
```{language}
{code}
```

目标：{goal}

要求：
1. 保持功能不变
2. 提高可读性
3. 遵循最佳实践"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def review_code(self, code: str, language: str) -> Dict:
        """审查代码"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请审查以下{language}代码：

```{language}
{code}
```

请返回JSON格式：
{{
    "score": 1-100,
    "issues": [
        {{"severity": "high/medium/low", "description": "描述", "fix": "修复"}}
    ],
    "strengths": ["优点"],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"review": content}

    def generate_tests(self, code: str, language: str, framework: str = "pytest") -> str:
        """生成测试"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下{language}代码生成{framework}测试：

```{language}
{code}
```

要求：
1. 覆盖所有方法
2. 边界测试
3. 异常测试"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def explain_code(self, code: str, language: str, level: str = "intermediate") -> str:
        """解释代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{level}水平解释以下{language}代码：

```{language}
{code}
```

要求：
1. 整体功能
2. 关键逻辑
3. 重要细节"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def suggest_improvements(self, code: str, language: str) -> List[Dict]:
        """建议改进"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为以下{language}代码提供改进建议：

```{language}
{code}
```

请返回JSON格式：
[
    {{"area": "改进领域", "current": "当前", "suggested": "建议", "reason": "原因"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"improvements": content}]


def create_tools(**kwargs) -> AIDeveloperTools:
    """创建开发者工具"""
    return AIDeveloperTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Developer Tools")
    print()

    # 测试
    code = tools.generate_code("斐波那契数列", "Python", "简洁")
    print(code[:300] + "...")

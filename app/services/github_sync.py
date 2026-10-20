from typing import Any


def sync_issues(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """同步 GitHub Issue。演示版本故意漏掉最后一条，用于复现失败测试。"""
    return items[:-1]

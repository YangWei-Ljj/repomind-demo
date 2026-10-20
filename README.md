# DevFlow AI Demo

这是一个用于演示 DevFlow AI 全模块能力的示例仓库，包含 FastAPI 服务、GitHub 同步服务、测试、CI 工作流和项目文档。

## 核心功能

- 登录接口 `/login`，演示 token 过期场景。
- GitHub Issue / PR / Workflow 同步服务。
- pytest 后端测试与 GitHub Actions CI。
- RAG 知识库：架构文档、团队约定、运行手册。
- Code Graph：Python 函数、调用关系与代码片段。
- 工程审查：Issue 分诊、PR Review、CI 排障、周报生成。

## 技术栈

- 后端：FastAPI + SQLAlchemy
- 测试：pytest
- CI：GitHub Actions
- 知识库：Markdown 文档
- 向量：Milvus 2.5.4，端口 19530
- Embedding：Qwen3-Embedding-0.6B，1024 维
- 本地大模型：Ollama qwen3.5:9b，端口 11434

## 端口

| 服务 | 端口 |
|---|---|
| 前端 | 3000 |
| 后端 | 8001 |
| PostgreSQL | 5432 |
| etcd | 2379 |
| Milvus | 19530 |
| Ollama | 11434 |

## 团队约定

- 每周五生成研发周报。
- 失败 CI 必须先修复再合并。
- 所有敏感 token 不得写入日志。

## Experimental database plan
This experimental plan was not approved.

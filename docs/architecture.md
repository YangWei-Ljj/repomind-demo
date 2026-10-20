# 架构说明

## 系统组成

- 前端：Next.js 15 + React 19 + TypeScript + Tailwind CSS。
- 后端：FastAPI + SQLAlchemy。
- 关系库：PostgreSQL（pgvector），端口 5432。
- 元数据协调：etcd，端口 2379。
- 向量库：Milvus 2.5.4，端口 19530，支持 hybrid retrieval。
- 本地模型：Ollama qwen3.5:9b，端口 11434。
- 嵌入模型：Qwen3-Embedding-0.6B，输出 1024 维向量。

## 数据流

1. 文档上传后按结构感知方式切片。
2. 使用 Qwen3-Embedding 生成 1024 维向量。
3. 写入 Milvus 并保留关键词索引。
4. 提问时执行向量召回 + BM25 关键词召回 + 融合 + 重排。
5. 由本地 qwen3.5:9b 生成带引用的回答。

## 模块

- Workspace：Issue / PR / CI、团队、记忆、技能、图谱。
- RAG 工作室：检索、重排、问答。
- Repos：仓库连接与同步。
- Drafts：安全操作草稿。
- Runs：Planner / 专用 Agent / Observer / Synthesis。
- Reports：研发周报。
- Code Graph：符号与关系。
- Evals：RAGAS 质量评测。

## CI attribution
CI failures are automatically attributed to the likely failing module.

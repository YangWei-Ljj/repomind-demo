# RepoMind 演示仓库

这是 **RepoMind**（一个面向 GitHub PR / Issue 研发协作的全栈 AI Agent 平台）的官方演示仓库。
本仓库包含了用于演示 RepoMind **全部模块**的示例数据：Issue、Pull Request、CI 运行记录、代码、文档与团队信息。

> 配套的应用源码仓库：https://github.com/YangWei-Ljj/RepoMind

---

## 一、RepoMind 是什么

RepoMind 是一个 AI 驱动的研发协作平台，核心能力：

- 连接并同步 GitHub 仓库的 Issue、PR、Workflow Run 与日志。
- Issue 智能分析：分类、优先级、复杂度、建议负责人、重复候选、行动项。
- PR 智能审查：摘要、关键变更、风险点、检查清单、测试建议、重点文件。
- CI 故障排障：失败类型、可能原因、排查步骤、相关上下文。
- 多 Agent 工作流：Planner → 专用 Agent → Observer → Synthesis。
- RAG 知识问答：文档解析、切片、向量化、混合检索、重排、带引用生成。
- 工程周报、安全操作草稿、代码图谱、RAGAS 评测。

## 二、技术栈

| 层 | 技术 |
|---|---|
| 后端 | Python + FastAPI + SQLAlchemy + PostgreSQL（pgvector） |
| 向量库 | Milvus 2.5.4（1024 维，hybrid retrieval） |
| 嵌入模型 | Qwen3-Embedding-0.6B（本地 GPU） |
| 大模型 | Ollama qwen3.5:9b（本地，OpenAI 兼容接口） |
| 前端 | Next.js 15 + React 19 + TypeScript + Tailwind CSS |
| 基础设施 | Docker Compose（PostgreSQL / etcd / Milvus） |

## 三、端口

| 服务 | 端口 |
|---|---|
| 前端 | 3000 |
| 后端 API / 文档 | 8001 / 8001/docs |
| PostgreSQL | 5432 |
| etcd | 2379 |
| Milvus | 19530 |
| Ollama | 11434 |

## 四、本仓库的演示数据

| 模块 | 演示数据 |
|---|---|
| Issue | 7 条，覆盖「未回复 / 讨论中 / 待决策 / 已处理 / 已拒绝 / 已关闭」六种状态 |
| PR | 5 条，覆盖「审核中 / 需主审 / 有冲突 / 已完成 / 已拒绝」五种状态 |
| CI | 11 条运行记录（含 1 次失败 + 多次成功） |
| 代码 | FastAPI 示例 + GitHub 同步服务 + pytest 测试 |
| 文档 | 架构说明、团队与职责、运行手册 |
| 团队 | 张伟（后端）、李娜（前端）、王强（DevOps）、赵敏（QA） |

### Issue 状态与 GitHub 标签的对应关系

RepoMind 根据 GitHub Issue 的 `state / labels / assignees` 自动分类：

| RepoMind 状态 | 触发条件 |
|---|---|
| 未回复 | 无标签且无负责人 |
| 讨论中 | open，有标签或负责人，无特殊标签 |
| 待决策 | 标签含 `decision` / `rfc` / `proposal` |
| 已处理 | 标签含 `accepted` / `resolved` / `done` / `fixed` |
| 已拒绝 | 标签含 `rejected` / `wontfix` / `invalid` / `duplicate` |
| 已关闭 | Issue 状态为 closed |

### PR 状态与 GitHub 数据的对应关系

| RepoMind 状态 | 触发条件 |
|---|---|
| 审核中 | open，有作者，无冲突/未合并 |
| 需主审 | open，作者为空（导入/同步数据） |
| 有冲突 | 标题/正文/补丁包含 `conflict` |
| 已完成 | 已合并 |
| 已拒绝 | closed 且未合并 |

## 五、快速体验

1. 启动 RepoMind（详见应用仓库的 README / 运行手册）。
2. 在 **Repos** 页面连接本仓库：
   - Owner：`YangWei-Ljj`
   - Repository：`repomind-demo`
   - 本仓库已公开，无需 Token。
3. 等待自动同步完成后，依次体验：

### Workspace（Issue / PR / CI）
- 左侧选择 `YangWei-Ljj/repomind-demo`
- Issue / PR / CI 标签下点击任意条目 → 「分析当前 Issue / PR / CI」
- 观察 AI 生成的优先级、风险、根因、阻塞判断与证据

### 团队
- Workspace → 团队：查看 4 位成员；可添加新成员

### 记忆&知识库
- Workspace → 记忆&知识库 → 索引状态：查看项目文档索引与 Milvus 状态

### 技能&MCP
- Workspace → 技能&MCP：验证 MCP 握手，切换 6 个内置 Skill

### 图谱
- Workspace → 图谱：查看 Issue / PR / CI / 文档 / 代码的关系图谱

### 项目知识 / RAG 工作室
- 项目知识：查看文档解析与分段
- RAG 工作室：提问「Milvus 使用哪个端口？」验证检索 + 带引用生成

### Repos / Drafts / Runs / Reports / Code Graph / Evals
- Repos：查看已连接仓库与同步策略
- Drafts：查看安全草稿，人工确认后才执行
- Runs：查看 Planner → Agent → Observer → Synthesis 的执行链
- Reports：生成单仓库 / 多仓库研发周报
- Code Graph：搜索 `sync_issues` 查看符号、关系与代码片段
- Evals：查看 RAGAS 质量评测结果

## 六、CI 演示说明

- `backend-test`：首次提交包含一个故意失败的测试（`test_sync_issues` 断言 3 但实现返回 2），产生「失败」记录。
- 随后的修复提交恢复了测试，产生「成功」记录。
- 因此 CI 面板同时包含失败与成功两种结论，可用于演示「分析当前 CI」。

## 七、常见问题

- 页面提示 `Error code: 502`：通常是 Ollama 未启动，启动后重试。
- Issue/PR 为空：先点击「刷新 Issue/PR/CI」。
- 私有仓库需要 Personal Access Token（`repo` 权限）。

---

### 免责声明

本仓库为演示用途，示例 Issue / PR / CI 用于展示 RepoMind 的全部分析能力。

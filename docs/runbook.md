# 运行手册

## 启动

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

## 验证

```bash
curl http://localhost:8001/health
pytest -q
```

## 约定

- 失败 CI 必须先修复再合并。
- 每周五生成研发周报。
- 敏感 token 不得写入日志。

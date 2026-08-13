# kch_cicd_test

一个基于 VeADK 构建的智能助手，理解用户意图并调用合适的工具完成任务。

## 运行

```bash
pip install -r requirements.txt
cp .env.example .env   # 填入你的密钥
python app.py
```

`app.py` 通过 VeADK 的 AgentKit 公共组件发布 `root_agent`，监听 `0.0.0.0:8000`。

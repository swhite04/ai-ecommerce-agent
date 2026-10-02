# 1. 告诉 Docker 使用官方的 Python 3.10 环境
FROM python:3.10-slim

# 2. 设置工作目录
WORKDIR /app

# 3. 把本地的装箱清单复制到集装箱里，并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 把我们写的所有代码复制进去
COPY . .

# 5. 给启动脚本运行权限
RUN chmod +x start.sh

# 6. 暴露网页的端口
EXPOSE 8501

# 7. 启动！
CMD ["./start.sh"]
# 使用官方 Python 3.10 图像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将项目依赖文件复制到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件到容器中
COPY . .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# config/config.py
#!/usr/bin/env python
# coding: UTF-8
'''
@File    :   config.py
@Time    :   2024/12/10 23:21:48
@Author  :   Rango
@Version :   1.0
@Software:   vscode
@Contact :   ljxrango@outlook.com
@Desc    :   None
'''

import os

# 基础URL配置
BASE_URL = "https://rangoljx.github.io"

# HTTP请求头设置
HEADERS = {
    "Content-Type": "application/json",
    # 请注意，出于安全考虑，不建议将敏感信息硬编码在配置文件中
    # "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    # 推荐使用环境变量或安全存储机制来管理访问令牌
    "Authorization": f"Bearer {os.getenv('API_ACCESS_TOKEN', 'default_or_placeholder_token')}"
}

# 数据库连接配置（以SQLite为例）
DATABASE_CONFIG = {
    'name': 'test_database.db',  # 数据库文件名
    'user': '',  # 用户名（SQLite等某些数据库可能不需要）
    'password': '',  # 密码（SQLite等某些数据库可能不需要）
    'host': '',  # 数据库服务器地址（SQLite使用':memory:'或文件路径）
    'port': '',  # 数据库端口（SQLite等某些数据库可能不需要）
}

# 其他API端点配置
OTHER_ENDPOINTS = {
    'user_endpoint': f"{BASE_URL}/users/",
    'product_endpoint': f"{BASE_URL}/products/",
    # 可根据需求继续添加其他端点
}

# 请求超时设置（以秒为单位）
REQUEST_TIMEOUT = 10

# 其他可能的配置项，例如日志级别、重试策略等
# ...

# 注意事项：
# 1. 请确保所有敏感信息（例如数据库密码、访问令牌）均不硬编码在配置文件中。
# 2. 考虑使用环境变量、配置文件管理工具或加密存储来安全地管理这些信息。
# 3. 在实际部署前，请仔细检查并测试所有配置项。
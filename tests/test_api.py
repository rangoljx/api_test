# tests/test_website.py

import pytest
from config.config import BASE_URL
from utils.requests_utils import send_request  # 从请求工具文件中导入send_request函数

# 测试GET请求的可达性
@pytest.mark.flaky(reruns=3, reruns_delay=2)  # 指定重跑次数为 3 次
@pytest.mark.parametrize("endpoint", [
    "/",  # 首页
    "/about/",  # 关于页面（注意GitHub Pages通常会自动重定向.html结尾的URL）
    "/blog/"  # 博客页面（注意末尾的斜杠，这取决于实际的URL结构）
])
def test_get_endpoints(endpoint):
    """
    测试网站不同端点的GET请求可达性。
    参数:
        -endpoint (str): 要测试的网站端点。
    测试方法:
        - 构造完整的URL。
        - 发送GET请求。
        - 检查响应状态码是否为200（成功），301（永久重定向）或302（临时重定向）。
    """
    # url = f"{BASE_URL}{endpoint}"
    try:
        response = send_request("GET", endpoint)  # 使用封装的请求函数
        # 检查状态码是否在预期的范围内
        assert response['status_code'] in [200, 301, 302, 304], f"Failed to GET {url}: {response['status_code']}"
        # 如果状态码为200，进行额外的内容检查
        # if response['status_code'] == 200:
        #     assert "<title>" in response['text'], f"Missing <title> tag in response for {url}"
        #     # 可以添加更多的内容检查...
    except Exception as e:
        # 捕获并打印异常，以便调试
        pytest.fail(f"Request to {BASE_URL+endpoint} failed with exception: {e}")

# 测试GET请求的响应时间
@pytest.mark.parametrize("endpoint", [
    "/",  # 首页
    "/about/",  # 关于页面
    "/blog/"  # 博客页面
])
def test_get_endpoints_response_time(endpoint):
    """
    测试网站不同端点的GET请求响应时间。
    参数:
        - endpoint (str): 要测试的网站端点。
    测试方法:
        - 构造完整的URL。
        - 发送GET请求。
        - 检查响应时间是否小于设定的阈值。
    """
    try:
        response = send_request("GET", endpoint)  # 使用封装的请求函数
        rtime = response['response_time']
        
        # 设定响应时间阈值（例如：1秒）
        MAX_RESPONSE_TIME = 10
        
        # 检查响应时间是否在阈值范围内
        assert rtime < MAX_RESPONSE_TIME, f"Response time for {BASE_URL}{endpoint} was too long: {rtime} seconds"
    except Exception as e:
        # 捕获并打印异常，以便调试
        pytest.fail(f"Request to {BASE_URL}{endpoint} failed with exception: {e}")































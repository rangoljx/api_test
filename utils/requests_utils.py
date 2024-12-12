# utils/requests_utils.py
import time
import requests
from config.config import BASE_URL, HEADERS, REQUEST_TIMEOUT

def send_request(method, endpoint, **kwargs):
    """
    发送HTTP请求并返回响应数据。

    参数:
    method (str): HTTP请求方法（例如 'GET', 'POST' 等）。
    endpoint (str): API的端点或路径。注意：这里不包含BASE_URL。
    **kwargs: 可变关键字参数，用于传递给requests.request函数，如data, json, params, headers, timeout等。
              如果提供了headers参数，它将与从config.py导入的HEADERS合并，且kwargs中的headers优先级更高。

    返回:
    dict: 包含响应的状态码、文本内容和（如果可能）JSON内容的字典。

    抛出:
    requests.exceptions.HTTPError: 如果响应状态码不是20x。
    ValueError: 如果响应的内容不是有效的JSON，但尝试解析为JSON时。
    requests.exceptions.RequestException: 其他请求错误。
    """
    url = f"{BASE_URL}{endpoint}"
    
    # 合并headers，确保kwargs中的headers优先级更高
    request_headers = HEADERS.copy()
    if 'headers' in kwargs:
        request_headers.update(kwargs['headers'])
    kwargs['headers'] = request_headers
    
    # 如果kwargs中未提供timeout，则使用REQUEST_TIMEOUT
    if 'timeout' not in kwargs:
        kwargs['timeout'] = REQUEST_TIMEOUT
    
    try:
        start_time = time.time()  # 记录开始时间
        response = requests.request(method, url, **kwargs)
        end_time = time.time()  # 记录结束时间
        response.raise_for_status()  # 如果响应状态码不是20x，则引发HTTPError异常
        response_time = end_time - start_time  # 计算响应时间
        
        response_data = {
            'status_code': response.status_code,
            'text': response.text,
            'response_time' : response_time
        }
        try:
            response_data['json'] = response.json()  # 尝试解析JSON内容
        except ValueError:
            # 如果不是有效的JSON，则忽略'json'键的添加
            pass
        return response_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except requests.exceptions.RequestException as req_err:
        # ValueError for json decoding is handled inside the try block above
        print(f"Request error occurred: {req_err}")
        raise
import pytest
import subprocess
import os
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# pytest 钩子函数，用于在测试会话结束时执行
def pytest_sessionfinish(session, exitstatus):
    report_dir = "results/"  # 可配置的报告目录
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    if exitstatus == 0:
        generate_command = [
            "allure", "generate", "results/", "-o", report_dir, "--clean"
        ]
        try:
            subprocess.run(generate_command, check=True)
            logger.info("Allure report generated successfully.")
            # 如果在本地开发，并且希望提示如何查看报告，可以打印以下信息
            # logger.info(f"To view the report, run: allure serve {report_dir}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to generate Allure report: {e}")
    else:
        logger.warning("Tests did not pass, skipping Allure report generation.")
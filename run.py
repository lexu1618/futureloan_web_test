# author:CC
# email:yangdeyi1201@foxmail.com

from config.paths import REPORTS_PATH
from pathlib import Path
import shutil
import pytest

if __name__ == '__main__':
    allure_raw_path = REPORTS_PATH/'allure-raw'

    # 执行脚本生成 allure 报告时，先判断删除之前的 allure-raw 源文件
    if Path.exists(allure_raw_path):
        shutil.rmtree(allure_raw_path)
    # 再执行脚本生成 allure 报告，以确保 allure 报告最新
    pytest.main(['-m', 'not expired', '--reruns', '3', '--reruns-delay', '5', '--alluredir=reports/allure-raw', '-s'])

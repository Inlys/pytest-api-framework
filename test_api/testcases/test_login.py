# 这里写测试用例

import allure
import requests
from common.yaml_utils import load_yaml
from common.runner_utils import runner


def test_login():
    # 定义一个空字典
    my_var = {}

    # 加载对应yaml文件，获取数据
    data = load_yaml("E:/VisualData/test_api/test_api/yaml/test_api.yaml")
    # 报告标题与测试用例一致
    allure.title(data['case_name'])

    # 先判断是请求还是响应还是返回值
    # steps是列表
    for step in data['steps']:

        # step=》request、response、extract是字典
        # 每个step的 键:值 拿出来
        for k, v in step.items():
            runner(k, v, my_var)
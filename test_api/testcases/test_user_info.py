import allure
from common.yaml_utils import load_yaml
from common.runner_utils import runner

def test_user_info():
    my_var = {}
    data = load_yaml("E:/VisualData/test_api/test_api/yaml/user_info.yaml")
    allure.title(data["case_name"])
    for step in data["steps"]:
        for k, v in step.items():
            runner(k, v, my_var)
from typing import List

import pytest


@pytest.fixture(scope="session")
def login():
    return "登录"


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """
    Called after collection has been performed. May filter or re-order the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    #items是所有测试用例列表，item代表每个测试用例对象
    #自定义用例的执行顺序（倒序执行收集的用例）
    items.reverse()

    for item in items:
        #解决编码问题（中文的测试用例名称）
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        #自动添加标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'delete' in item.nodeid:
            item.add_marker(pytest.mark.delete)
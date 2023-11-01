#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/11/02 12:20
@Author  : Bian Jiang
@File    : test_baidu_ernie_api.py
"""

from metagpt.logs import logger
from metagpt.provider.baidu_ernie_api import BaiduErnieAPI

def test_message():
    llm = BaiduErnieAPI()

    result = llm.ask('请以「我爱中国」写一首藏头诗')
    logger.info(result)
    assert len(result) > 100
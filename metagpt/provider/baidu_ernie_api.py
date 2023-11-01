# -*- coding: utf-8 -*-
"""
@Time    : 2023/11/1 22:10
@Author  : Bian Jiang 
@File    : baidu_ernie_api.py
"""

from typing import Optional

import requests
import json
import time

from metagpt.config import CONFIG
from metagpt.logs import logger
from metagpt.provider.base_gpt_api import BaseGPTAPI

class BaiduErnieAPI(BaseGPTAPI):
    def __init__(self):
        self.ernie_api_key = CONFIG.ernie_api_key
        self.ernie_secret_key = CONFIG.ernie_secret_key
        self.ernie_api_base = CONFIG.ernie_api_base
        self.access_token = None
        self.token_refresh_at = 0
        logger.warning('当前方法无法支持异步运行。当你使用acompletion时，并不能并行访问。')

    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        if self.access_token != None and time.time() < self.token_refresh_at:
            return self.access_token
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.ernie_api_key,
                  "client_secret": self.ernie_secret_key}
        resp = requests.post(url, params=params).json()
        self.access_token = resp.get("access_token")
        self.token_refresh_at = time.time() + resp.get("expires_in")
        return self.access_token

    def get_choice_text(self, rsp: dict) -> str:
        return rsp.get('result')

    async def acompletion_text(self, messages: list[dict], stream=False) -> str:
        # 不支持
        logger.error('该功能禁用。')
        w = self.completion(messages)
        return w

    async def acompletion(self, messages: list[dict]):
        # 不支持异步
        return self.completion(messages)

    def completion(self, messages: list[dict]):
        if self.access_token == None or time.time() >= self.token_refresh_at:
            self.get_access_token()
        
        url = f"{self.ernie_api_base}?access_token={self.access_token}"
        msglist = []
        sysmsg = ""
        if type(messages) == str:
            print("messages is a string")
            msglist = [
                {
                    "role": "user", 
                    "content": messages
                }
            ]
        elif type(messages) == list:
            print("messages is a list")
            for message in messages:
                if message["role"] == "system":
                    sysmsg = message["content"]
                    continue
                msglist.append(message)
        payload = json.dumps({
            "messages": msglist,
            "system": sysmsg
        })
        headers = {
            'Content-Type': 'application/json'
        }
        
        logger.info(payload)

        response = requests.request("POST", url, headers=headers, data=payload)
        response = json.loads(response.text.replace('false', '"false"'))
        if 'error_code' in response:
            logger.error(response)
        return response
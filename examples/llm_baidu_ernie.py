#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/11/02 14:13
@Author  : Bian Jiang
@File    : llm_baidu_ernie.py
"""
import asyncio

from metagpt.llm import LLM, Baidu
from metagpt.logs import logger

async def main():
    # llm = LLM()
    baidu = Baidu()

    hello_msg = [{'role': 'user', 'content': 'count from 1 to 10. split by newline.'}]

    # logger.info("    #### Start Ask #### ")
    # logger.info(baidu.ask('你好，请进行自我介绍'))
    # logger.info(llm.ask('你好，请进行自我介绍'))

    logger.info("    #### Start aask #### ")
    logger.info(await baidu.aask('请以「我爱中国」写一首藏头诗'))
    # logger.info(await llm.aask('请以「我爱中国」写一首藏头诗'))

    # logger.info("    #### Start acompletion_text 1 #### ")
    # logger.info(await baidu.acompletion_text('请以「我爱中国」写一首藏头诗'))
    # logger.info(await llm.acompletion_text('请以「我爱中国」写一首藏头诗'))

    # logger.info("    #### Start acompletion_text 2 #### ")
    # logger.info(await baidu.acompletion_text(hello_msg))
    # logger.info(await llm.acompletion_text(hello_msg))


    # logger.info(await llm.aask_batch(['hi', 'write python hello world.']))

    # logger.info(await llm.acompletion(hello_msg))
    # logger.info(await llm.acompletion_batch([hello_msg]))
    # logger.info(await llm.acompletion_batch_text([hello_msg]))

    # logger.info(await llm.acompletion_text(hello_msg))

if __name__ == '__main__':
    asyncio.run(main())

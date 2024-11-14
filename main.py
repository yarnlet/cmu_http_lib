# found by yarnlet nov 13 2024
# https://github.com/yarnlet/cmu_http_lib

import json
import browser.aio as aio

async def get(url: str):
    req = await aio.ajax(url=url, method="GET")
    
    print(req.data)
    return req.data # response body

async def post(url: str)
    req = await aio.ajax(url=url, method="POST")
    
    print(req.data)
    return req.data
    
    
### sample function call
#aio.run(get("https://catfact.ninja/fact")).

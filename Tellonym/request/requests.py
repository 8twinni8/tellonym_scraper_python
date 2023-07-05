import requests as req
import random
from .useragents import USER_AGENTS


class Request:


    @staticmethod
    def get(url) -> req.Response:
        user_agent = random.choice(USER_AGENTS)
        headers = {
            'User-Agent': user_agent
        }
        
        return req.get(url, headers=headers)


import requests as req


class Request:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)',
    }

    @staticmethod
    def get(url) -> req.Response:
        return req.get(url, headers=Request.HEADERS)


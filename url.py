class Url:
    def __init__(self, origin_url, code):
        self.origin_url = origin_url
        self.code=code

    def url_dict(self):
        return {
            "origin_url": self.origin_url,
            "code": self.code
        }
class Url:
    def __init__(self, code, origin_url):
        self.origin_url = origin_url
        self.code=code

    def __str__(self):
        return f'The original URL: {self.origin_url} | The short code:{self.code}, The shortened URL: {self.origin_url}/{self.code}'

    def to_dict(self):
        return {
           "origin_url":self.origin_url,
            "short_code":self.code,
        }
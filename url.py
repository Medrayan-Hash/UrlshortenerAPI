class Url:
    def __init__(self, code, origin_url):
        self.origin_url = origin_url
        self.code=code

    def __str__(self):
        return f'{self.origin_url}/{self.code}'

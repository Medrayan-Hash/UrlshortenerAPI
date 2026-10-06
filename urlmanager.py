import string
import random
from url import Url

class UrlManager:
    def __init__(self):
        self.urls = []

    @staticmethod
    def generate_code():
        characters = string.ascii_letters + string.digits
        token = []
        for c in range(5):
            character = random.choice(characters)
            token.append(character)

        short_code = "".join(token)
        return short_code

    def create_url_object(self, url):
            code = self.generate_code()
            url_object = Url(code, url)
            self.urls.append(url_object)

            return url_object

    def shorten_url(self, url):
        self.create_url_object(url)






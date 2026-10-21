import json
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

    def urls_dict(self):
        urls_dicts = []
        for url in self.urls:
            urls_dicts.append(url.to_dict())

        return urls_dicts

    def save_url(self):
        with open('url.json', 'w') as w:
            json.dump(self.urls_dict(), w)

    def shorten_url(self, url):
        the_object=self.create_url_object(url)
        self.save_url()
        return f"http://127.0.0.1:8000/{the_object.code}"

    def return_object(self, url_code):
       self.load_object()
       for i in self.urls:
           if i.code == url_code:
               return i
       return None

    def load_object(self):
       with open('url.json', 'r') as read:
           data = json.load(read)

       for url_object in data:
           object_url=Url(**url_object)
           self.urls.append(object_url)
       return self.urls







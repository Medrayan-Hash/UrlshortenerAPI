from urlmanager import UrlManager
from fastapi import FastAPI
from pydantic import BaseModel

manager = UrlManager()

app = FastAPI()

class Url(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(payload: Url):
    short_url = {"short_url": manager.shorten_url(payload.url)}
    return short_url

@app.get("/{url_code}")
def get_short_url(url_code: str):
    return manager.return_object(url_code)




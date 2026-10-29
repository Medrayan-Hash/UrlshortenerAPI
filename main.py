from starlette import status
from urlmanager import UrlManager
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

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
    the_url=manager.return_object(url_code)
    return RedirectResponse(the_url.origin_url , status.HTTP_302_FOUND)


# Librerias externas
from msilib.schema import Directory
from re import template
from unicodedata import name
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Librerias internas


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def holaMundo(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/items/{id}", response_class=HTMLResponse)
async def root(request: Request, id:str):
    return templates.TemplateResponse("item.html", {"request":request , "id":id})
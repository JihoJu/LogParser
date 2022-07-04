from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from parser import parse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/logparser")
async def input_log(request: Request):
    context = dict()

    context["request"] = request

    return templates.TemplateResponse("index.html", context)


@app.post("/parsing")
async def parse_log(request: Request, log: str = Form(...)):
    res = dict()
    parsed_obj = parse(log)
    for obj_type in parsed_obj.keys():
        if len(parsed_obj[obj_type]) != 0:
            res[obj_type] = parsed_obj[obj_type]

    return res

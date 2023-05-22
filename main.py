import json

import uvicorn
from fastapi import FastAPI, Request, Form
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional

from compress_the_string import compress_the_string

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_problem/{problem_name}", response_class=HTMLResponse)
@app.get("/get_problem/", response_class=HTMLResponse)
async def get_problem(request: Request, problem_name: Optional[str] = None):
    with open("config.json", "r+") as file:
        content = json.loads(file.read())

    if problem_name:
        if problem_name in content:
            return templates.TemplateResponse("problem_list.html",
                                              {"request": request, "id": problem_name, "items": content[problem_name]})
        else:
            return templates.TemplateResponse("error.html", {"request": request,
                                                             "error_massage": f"No course wih name {problem_name}.\n All available names {list(content.keys())}"})

    else:
        return templates.TemplateResponse("problem_list.html", {"request": request, "id": problem_name, "items": []})


@app.get("/view_problem/{problem_id}", response_class=HTMLResponse)
async def view_problem(request: Request, problem_id: int):
    with open("config.json", "r+") as file:
        content = json.loads(file.read())
        content = content["Pythonist 3"][problem_id - 1]
    return templates.TemplateResponse("problem_solver.html",
                                      {"request": request, "problem_id": problem_id, "problem": content})


@app.post("/submit")
async def submit(user_input: int = Form(...)):
    # Затичка під одну задачу
    return {"solution of the problem": compress_the_string(user_input)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

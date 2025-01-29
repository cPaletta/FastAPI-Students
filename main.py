from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes import students, auth
from database import engine, Base

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

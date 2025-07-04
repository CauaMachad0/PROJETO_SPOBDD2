from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from backend.database import SessionLocal
from backend.models import Usuario, Produto

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/usuarios")
def listar_usuarios(request: Request):
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    return templates.TemplateResponse("usuarios.html", {"request": request, "usuarios": usuarios})

@app.post("/usuarios")
def criar_usuario(nome: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    db = SessionLocal()
    novo = Usuario(nome=nome, email=email, senha=senha)
    db.add(novo)
    db.commit()
    return RedirectResponse(url="/usuarios", status_code=303)

@app.get("/produtos")
def listar_produtos(request: Request):
    db = SessionLocal()
    produtos = db.query(Produto).all()
    return templates.TemplateResponse("produtos.html", {"request": request, "produtos": produtos})

@app.post("/produtos")
def criar_produto(nome: str = Form(...), categoria: str = Form(None), marca: str = Form(None)):
    db = SessionLocal()
    novo = Produto(nome=nome, categoria=categoria, marca=marca)
    db.add(novo)
    db.commit()
    return RedirectResponse(url="/produtos", status_code=303)

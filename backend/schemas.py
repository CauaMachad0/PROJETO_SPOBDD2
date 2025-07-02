from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioRead(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

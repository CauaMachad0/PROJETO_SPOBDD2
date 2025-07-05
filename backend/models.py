from sqlalchemy import Column, Integer, String
from backend.database import Base
from sqlalchemy.orm import mapped_column,registry,Mapped
table_registry = registry()


@table_registry.mapped_as_dataclass
class Usuario:
    __tablename__ = "usuario"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True,init=False,autoincrement=True)
    nome:Mapped[str] = mapped_column(String, nullable=False)
    email:Mapped[str] = mapped_column(String, unique=True, nullable=False)
    senha:Mapped[str] = mapped_column(String, nullable=False)


@table_registry.mapped_as_dataclass
class Produto:
    __tablename__ = "produto"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True,init=False,autoincrement=True)
    nome:Mapped[str] = mapped_column(String, nullable=False)
    categoria:Mapped[str] = mapped_column(String, nullable=True)
    marca:Mapped[str] = mapped_column(String, nullable=True)

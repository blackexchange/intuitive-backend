from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, Date
from database import Base
class Movie(Base):
    __tablename__ = "Movie"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    desc = Column(Text())
    type = Column(String(20))
    url = Column(String(100))
    rating = Column(Integer)

class Operadoras(Base):
    __tablename__ = "ans"
    Registro_ANS = Column(Integer, primary_key=True, index=True)
    Nome_Fantasia = Column(String(200))
    Razao_Social = Column(String(200))
    '''   CNPJ = Column(String(200)) 
    Modalidade = Column(String(200)) 
    Logradouro = Column(String(200)) 
    Numero = Column(String(200)) 
    Complemento = Column(String(200)) 
    Bairro = Column(String(200)) 
    Cidade = Column(String(200)) 
    UF = Column(String(200)) 
    CEP = Column(String(200)) 
    DDD = Column(String(200)) 
    Telefone = Column(String(200)) 
    Fax = Column(String(200)) 
    Endereco_eletronico = Column(String(200)) 
    Representante = Column(String(200)) 
    Cargo_Representante = Column(String(200)) 
    Data_Registro_ANS = Column(Date) 

   '''
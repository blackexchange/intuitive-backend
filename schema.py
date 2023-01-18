from datetime import date
from pydantic import BaseModel
class Movie(BaseModel):
    id = int
    name = str
    desc = str
    type = str
    url = str
    rating = str

    class Config:
        orm_mode = True
class Operadoras(BaseModel):
    Registro_ANS = int
    CNPJ = str
    Razao_Social = str
    Nome_Fantasia = str
    '''Modalidade = str
    Logradouro = str
    Numero = str
    Complemento = str
    Bairro = str
    Cidade = str
    UF = str
    CEP = str
    DDD = str
    Telefone = str
    Fax = str
    Endereco_eletronico = str
    Representante = str
    Cargo_Representante = str
    Data_Registro_ANS = date
    '''

    class Config:
        orm_mode = True
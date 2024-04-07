from typing import List
from pydantic import BaseModel

from Utils.Utils import GetCsv, ReadCsv

_fileNameProd = 'prod.csv'

def download_csv():
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv', _fileNameProd)


def LerCsv():
    csv = ReadCsv(_fileNameProd)
    csv_colunas = ['Nome','Nome Amigavel'] + [x for x in range(1997,2023)]
    lista = []
    for i in range(1, len(csv)):
        csv_linha = csv[i].split(';')
        retorno = Retorno(Id=csv_linha[0], Produto=csv_linha[1], Dados=[])
        for j in range(0,len(csv_colunas)):
            retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j]))
        lista.append(retorno)
    return lista
class RetornoAuxiliar(BaseModel):
    Ano: int
    Valor: float


class Retorno(BaseModel):
    Id: int
    Produto: str
    Dados: List[RetornoAuxiliar]




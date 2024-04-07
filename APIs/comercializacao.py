from typing import List
from pydantic import BaseModel

from Utils.Utils import GetCsv, ReadCsv

_fileNameProd = 'comercializacao.csv'


def download_csv():
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv', _fileNameProd)


def LerCsv():
    download_csv()
    csv = ReadCsv(_fileNameProd)
    csv_colunas = ['Id', 'Nome', 'Nome Amigavel'] + [x for x in range(1970, 2023)]
    lista = []
    for i in range(0, len(csv)):
        csv_linha = csv[i].split(';')
        retorno = Retorno(Id=csv_linha[0], Nome=csv_linha[1],NomeAmigavel=csv_linha[2].strip(), Dados=[])
        for j in range(3, len(csv_colunas)):
            retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j]))
        lista.append(retorno)
    return lista


class RetornoAuxiliar(BaseModel):
    Ano: int
    Valor: float


class Retorno(BaseModel):
    Id: int
    Nome: str
    NomeAmigavel: str
    Dados: List[RetornoAuxiliar]

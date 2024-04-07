from typing import List
from pydantic import BaseModel

from Utils.Utils import GetCsv, ReadCsv

_fileNameProd1 = 'ProcessaViniferas.csv'
_fileNameProd2 = 'ProcessaAmericanas.csv'
_fileNameProd3 = 'ProcessaMesa.csv'
_fileNameProd4 = 'ProcessaSemclass.csv'

def download_csv():
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv', _fileNameProd1)
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv', _fileNameProd2)
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv', _fileNameProd3)
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv', _fileNameProd4)


def LerCsv():
    download_csv()
    csv = ReadCsv(_fileNameProd1) + ReadCsv(_fileNameProd2,True) + ReadCsv(_fileNameProd3,True) + ReadCsv(_fileNameProd4,True)
    csv_colunas = csv[0].split(';')
    csv.sort(key=OrdernarPorNome)
    lista = []
    for i in range(1, len(csv)):
        csv_linha = csv[i].split(';')
        retorno = Retorno(Id=csv_linha[0], Produto=csv_linha[1], Dados=[])
        for j in range(2,len(csv_colunas)):
            retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j]))
        lista.append(retorno)
    return lista

def OrdernarPorNome(linha):
    return linha.lower().split('\t')[1]

class RetornoAuxiliar(BaseModel):
    Ano: int
    Valor: float


class Retorno(BaseModel):
    Id: int
    Produto: str
    Dados: List[RetornoAuxiliar]




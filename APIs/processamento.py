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
    Dicionario = {
        'Viniferas': _fileNameProd1,
        'Americanas': _fileNameProd2,
        'Mesa': _fileNameProd3,
        'SemClasse': _fileNameProd4
    }
    lista = []

    for key, val in Dicionario.items():

        csv = ReadCsv(val, key != 'Viniferas')
        csv_colunas = csv[0].split(';')
        for i in range(1, len(csv)):
            csv_linha = csv[i].split(';')
            retorno = Retorno(Id=csv_linha[0], Nome=csv_linha[1], NomeAmigavel=csv_linha[2], TipoProduto=key, Dados=[])
            for j in range(3, len(csv_colunas)):
                print(csv_colunas[j])
                print(csv_linha[j])
                retorno.Dados.append(
                    RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j] if csv_linha[j].isdigit() else 0))
            lista.append(retorno)
    return lista

def OrdernarPorNome(linha):
    return linha.trim().lower().split('\t')[1]

class RetornoAuxiliar(BaseModel):
    Ano: int
    Valor: float


class Retorno(BaseModel):
    Id: int
    Nome: str
    NomeAmigavel: str
    TipoProduto: str
    Dados: List[RetornoAuxiliar]




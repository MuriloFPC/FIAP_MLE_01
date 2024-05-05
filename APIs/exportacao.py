from typing import List
from pydantic import BaseModel

from Utils.Utils import GetCsv, ReadCsv

_fileNameProd1 = 'ExportacaoVinhos.csv'
_fileNameProd2 = 'ExportacaoEspumantes.csv'
_fileNameProd3 = 'ExportacaoFrescas.csv'
_fileNameProd4 = 'ExportacaoSucos.csv'


def download_csv():
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv', _fileNameProd1)
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv', _fileNameProd2)
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv', _fileNameProd3)
    GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv', _fileNameProd4)


def LerCsv():
    download_csv()
    Dicionario = {
        'Vinhos': _fileNameProd1,
        'Espumantes': _fileNameProd2,
        'Uvas_Frescas': _fileNameProd3,
        'Sucos': _fileNameProd4,
    }
    lista = []

    for key, val in Dicionario.items():

        csv = ReadCsv(val, key != 'Vinhos')
        if(key == 'Vinhos'):
            csv_colunas = csv[0].split(';')
        for i in range(1, len(csv)):
            csv_linha = csv[i].split(';')
            retorno = Retorno(Id=csv_linha[0], Pais=csv_linha[1], TipoProduto=key, Dados=[])
            for j in range(2, len(csv_colunas)):
                retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j] if csv_linha[j] != '' else 0))
            lista.append(retorno)
    return lista


def OrdernarPorNome(linha):
    return linha.lower().split('\t')[1]


class RetornoAuxiliar(BaseModel):
    Ano: int
    Valor: float


class Retorno(BaseModel):
    Id: int
    Pais: str
    TipoProduto: str
    Dados: List[RetornoAuxiliar]

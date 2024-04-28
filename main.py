from typing import Union

from fastapi import FastAPI
from starlette import status
from starlette.responses import RedirectResponse

import APIs.producao as prod
import APIs.comercializacao as comercializacao
import APIs.processamento as processamento
import APIs.importacao as importacao
import APIs.exportacao as exportacao

app = FastAPI()



@app.get("/", summary="sumary", description="description")
def read_root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@app.get("/producaoList")
def read_item():
    return prod.LerCsv()


@app.get("/processamentoList")
def read_item():
    return processamento.LerCsv()


@app.get("/comercializacaoList")
def read_item():
    return comercializacao.LerCsv()


@app.get("/importacaoList")
def read_item():
    return importacao.LerCsv()


@app.get("/exportacaoList")
def read_item():
    return exportacao.LerCsv()

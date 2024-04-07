from typing import Union

from fastapi import FastAPI

import APIs.producao as prod
import APIs.comercializacao as comercializacao
import APIs.processamento as processamento

app = FastAPI()



@app.get("/", summary="sumary", description="description")
def read_root():
    return {"Hello": "World"}


@app.get("/producaoList")
def read_item():
    return prod.LerCsv()


@app.get("/processamentoList")
def read_item():
    processamento.LerCsv()
    return {"item_id": 'item_id', "q": 'q'}


@app.get("/comercializacaoList")
def read_item():
    return comercializacao.LerCsv()


@app.get("/importacaoList")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/exportacaoList")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

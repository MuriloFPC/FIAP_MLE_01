from typing import Union

from fastapi import FastAPI
from starlette import status
from starlette.responses import RedirectResponse
from fastapi.openapi.docs import get_swagger_ui_html

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
    """
    Retorna dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Produto": "VINHO DE MESA",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 217208604
            },
            {
                "Ano": 1971,
                "Valor": 154264651
            },
            ...
            ]
        }
    ]
    ```
    """
    return prod.LerCsv()


@app.get("/processamentoList")
def read_item():
    """
    Retorna dados de quantidade de uvas processadas no Rio Grande do Sul.


    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Nome": "TINTAS",
            "NomeAmigavel": "TINTAS",
            "TipoProduto": "Viniferas",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 10448228
            },
            ...
            ]
        }
    ]
    ```
    """
    return processamento.LerCsv()


@app.get("/comercializacaoList")
def read_item():
    """
    Retorna dados de comercializaçao de vinhos e derivados no Rio Grande do Sul.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Nome": "VINHO DE MESA",
            "NomeAmigavel": "VINHO DE MESA",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 98327606
            },
            ...
            ]
        }
    ]
    ```
    """
    return comercializacao.LerCsv()


@app.get("/importacaoList")
def read_item():
    """
    Retorna dados de importação de derivados de uva.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Pais": "Africa do Sul",
            "TipoProduto": "Vinhos",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 0
            },
            ...
            ]
        }
    ]
    ```
    """
    return importacao.LerCsv()


@app.get("/exportacaoList")
def read_item():
    """
    Retorna dados de exportaçao de derivados de uva.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "id": 36,
            "País": Mônaco
            "Dados": [
            {
                "Quantidade": 1180759,
                "Valor": 512716
            }
            ...
            ]
        }
    ]
    ```
    """
    return exportacao.LerCsv()

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Documentaçao API - Projeto MLE_01")

from pydantic import BaseModel, HttpUrl


class TariffSchema(BaseModel):
    """
    Описание структуры тарифа.
    """
    url: HttpUrl
    document: str

class ContractSchema(BaseModel):
    """
    Описание структуры контракта.
    """
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа по тарифу.
    """
    tariff: TariffSchema

class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа по контракту.
    """
    contract: ContractSchema
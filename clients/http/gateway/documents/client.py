from httpx import Response
from typing import TypedDict

from clients.http.client import HttpClient
from clients.http.gateway.client import build_gateway_http_client


class TariffDict(TypedDict):
    """
    Описание структуры тарифа.
    """
    url: str
    document: str

class ContractDict(TypedDict):
    """
    Описание структуры контракта.
    """
    url: str
    document: str

class GetTariffDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения документа по тарифу.
    """
    tariff: TariffDict

class GetContractDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения документа по контракту.
    """
    contract: ContractDict


class GetTariffDocumentGatewayHTTPClient(HttpClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """
    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f'/api/v1/documents/tariff-document/{account_id}')

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f'/api/v1/documents/contract-document/{account_id}')

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> GetTariffDocumentGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return GetTariffDocumentGatewayHTTPClient(client=build_gateway_http_client())
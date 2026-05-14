from httpx import Response
from typing import TypedDict

from clients.http.client import HttpClient
from clients.http.gateway.client import build_gateway_http_client


class CardDict(TypedDict):
    """
    Описание структуры карты.
    """
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str

class IssueVirtualCardRequest(TypedDict):
    """
    Структура данных для выпуска виртуальной карты.
    """
    userId: str
    accountId: str

class IssuePhysicalCardRequest(TypedDict):
    """
    Описание структуры ответа выпуска виртуальной карты.
    """
    userId: str
    accountId: str

class CreateVirtualCardResponseDict(TypedDict):
    """
    Описание структуры ответа выпуска виртуальной карты.
    """
    card: CardDict

class CreatePhysicalCardResponseDict(TypedDict):
    """
    Структура данных для выпуска физической карты.
    """
    card: CardDict

class CardsGatewayHTTTPClient(HttpClient):
    """
    Клиент для взаимодействия с /api/v1/cards/ сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> Response:
        """
        Метод для выпуска виртуальной карты.
        :param request: Запрос на создание виртуальной карты (объект IssueCardRequest).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/cards/issue-virtual-card', json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> Response:
        """
        Метод для выпуска физической карты.
        :param request: Запрос на создание физической карты (объект IssueCardRequest).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/cards/issue-physical-card', json=request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> CreateVirtualCardResponseDict:
        request = IssueVirtualCardRequest(userId=user_id, accountId=account_id)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def issue_physical_card(self, user_id: str, account_id: str) -> CreatePhysicalCardResponseDict:
        request = IssuePhysicalCardRequest(userId=user_id, accountId=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTTPClient(client=build_gateway_http_client())
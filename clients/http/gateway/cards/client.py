from httpx import Response
from typing import TypedDict

from clients.http.client import HttpClient


class IssueVirtualCardRequest(TypedDict):
    userId: str
    accountId: str

class IssuePhysicalCardRequest(TypedDict):
    userId: str
    accountId: str

class CardsGatewayClient(HttpClient):
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
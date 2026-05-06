from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HttpClient

class GetAccountsQueryDict(TypedDict):
    """
    Структура данных для получения списка счетов пользователя.
    """
    account: str

class OpenDepositAccountRequest(TypedDict):
    """
    Структура данных для открытия депозитного счета.
    """
    accountId: str

class OpenSavingsAccountRequest(TypedDict):
    """
    Структура данных для открытия сберегательного счета.
    """
    accountId: str

class OpenDebitCardAccountRequest(TypedDict):
    """
    Структура данных для открытия дебетового счета.
    """
    accountId: str

class OpenCreditCardAccountRequest(TypedDict):
    """
    Структура данных для открытия кредитного счета.
    """
    accountId: str

class AccountsGatewayHTTPClient(HttpClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway.
    """
    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get('/api/v1/accounts', params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequest) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post('/api/v1/accounts/open-deposit-account', json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequest) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/accounts/open-savings-account', json=request)

    def open_debit_account_api(self, request: OpenDebitCardAccountRequest) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/accounts/open-debit-card-account', json=request)

    def open_credit_account_api(self, request: OpenCreditCardAccountRequest) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/accounts/open-credit-card-account', json=request)
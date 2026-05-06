from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HttpClient


class OperationsQueryBaseDict(TypedDict):
    """
    Базовая структура данных для query-параметров.
    """
    accountId: str

class OperationsRequestBaseDict(TypedDict):
    """
    Базовая структура данных для тела запроса.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class GetOperationsQueryDict(OperationsQueryBaseDict):
    """
    Структура данных для получения списка операций.
    """
    pass

class GetOperationsSummaryQueryDict(OperationsQueryBaseDict):
    """
    Структура данных для получения сводки по операциям.
    """
    pass

class MakeFeeOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для списанию комиссии.
    """
    pass

class MakeTopUpOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для пополнения счета.
    """
    pass

class MakeCashbackOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для начисления кэшбека.
    """
    pass

class MakeTransferOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для перевода средств.
    """
    pass

class MakePurchaseOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для покупки.
    """
    category: str

class MakeBillPaymentOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для оплаты счетов и регулярных платежей.
    """
    pass

class MakeCashWithdrawalOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для вывода денежных средств.
    """
    pass

class OperationsGatewayHTTPClient(HttpClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """
    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций пользователя.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get('/api/v1/operations', params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получения сводки по операциям.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со сводкой о операциях.
        """
        return self.get('/api/v1/operations/operations-summary', params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id:str) -> Response:
        """
        Выполняет GET-запрос для получения чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными о чеках.
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_api(self, operation_id:str) -> Response:
        """
        Выполняет GET-запрос для информации по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными о операции.
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для снятия комиссии.

        :param request: Запрос на проведение операции списания комиссии (объект MakeFeeOperationRequestDict)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для пополнения счета.

        :param request: Запрос на проведение операции пополнения счета (объект MakeTopUpOperationRequestDict)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для пополнения кэшбека.

        :param request: Запрос на получения кэшбека (объект MakeCashbackOperationRequestDict)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для перевода средств.

        :param request: Запрос на перевод средств (объект MakeTransferOperationRequestDict)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для операции покупки.

        :param request: Запрос на покупку (объект MakePurchaseOperationRequestDict)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для оплату счетов/регулярных платежей.

        :param request: Запрос на оплату счетов/регулярных платежей (объект MakeBillPaymentOperationRequestDict)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request)

    def make_cash_withdraw_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для вывода денежных средств.

        :param request: Запрос на вывод денежных средств (объект MakeCashWithdrawalOperationRequestDict)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-cash-withdrawal-operation', json=request)
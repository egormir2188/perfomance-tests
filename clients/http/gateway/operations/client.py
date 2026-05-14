from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HttpClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека.
    """
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """
    Описание структуры сводки по операциям
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

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
    amount: float
    cardId: str
    accountId: str

class GetOperationsQueryDict(OperationsQueryBaseDict):
    """
    Структура данных для получения списка операций.
    """
    pass

class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа для получения списка операций.
    """
    operations: list[OperationDict]

class GetOperationsSummaryQueryDict(OperationsQueryBaseDict):
    """
    Структура данных для получения сводки по операциям.
    """
    pass

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа для получения сводки по операциям.
    """
    summary: OperationsSummaryDict

class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура ответа для получения чека по операции.
    """
    receipt: OperationReceiptDict

class GetOperationResponseDict(TypedDict):
    """
    Структура ответа для получения информации по операции.
    """
    operation: OperationDict

class MakeFeeOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для списанию комиссии.
    """
    pass

class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа для операции снятия комиссии.
    """
    operation: OperationDict

class MakeTopUpOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для пополнения счета.
    """
    pass

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа для операции пополнения счета.
    """
    operation: OperationDict

class MakeCashbackOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для начисления кэшбека.
    """
    pass

class MakeCashbackOperationResponseDict(TypedDict):
    """
    Структура ответа для операции получения кэшбека.
    """
    operation: OperationDict

class MakeTransferOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для перевода средств.
    """
    pass

class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура ответа для операции перевода.
    """
    operation: OperationDict

class MakePurchaseOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для покупки.
    """
    category: str

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура ответа для операции покупки.
    """
    operation: OperationDict

class MakeBillPaymentOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для оплаты счетов и регулярных платежей.
    """
    pass

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Структура ответа платы счетов и регулярных платежей.
    """
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(OperationsRequestBaseDict):
    """
    Структура данных для вывода денежных средств.
    """
    pass

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура ответа для вывода денежных средств.
    """
    operation: OperationDict

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

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными о чеках.
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_api(self, operation_id: str) -> Response:
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

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request=request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request=request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request=request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request=request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="taxi"
        )
        response = self.make_purchase_operation_api(request=request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request=request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdraw_operation_api(request=request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
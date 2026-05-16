from httpx import Response, QueryParams

from clients.http.client import HttpClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import GetOperationsQuerySchema, GetOperationsSummaryQuerySchema, \
    MakeFeeOperationRequestSchema, MakeTopUpOperationRequestSchema, MakeCashbackOperationRequestSchema, \
    MakeTransferOperationRequestSchema, MakePurchaseOperationRequestSchema, MakeBillPaymentOperationRequestSchema, \
    MakeCashWithdrawalOperationRequestSchema, GetOperationsResponseSchema, GetOperationsSummaryResponseSchema, \
    GetOperationReceiptResponseSchema, GetOperationResponseSchema, MakeFeeOperationResponseSchema, OperationStatus, \
    MakeTopUpOperationResponseSchema, MakeCashbackOperationResponseSchema, MakeTransferOperationResponseSchema, \
    MakePurchaseOperationResponseSchema, MakeBillPaymentOperationResponseSchema, \
    MakeCashWithdrawalOperationResponseSchema


class OperationsGatewayHTTPClient(HttpClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """
    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций пользователя.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get('/api/v1/operations', params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получения сводки по операциям.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со сводкой о операциях.
        """
        return self.get(
            '/api/v1/operations/operations-summary',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

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

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для снятия комиссии.

        :param request: Запрос на проведение операции списания комиссии (объект MakeFeeOperationRequestSchema)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для пополнения счета.

        :param request: Запрос на проведение операции пополнения счета (объект MakeTopUpOperationRequestSchema)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для пополнения кэшбека.

        :param request: Запрос на получения кэшбека (объект MakeCashbackOperationRequestSchema)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для перевода средств.

        :param request: Запрос на перевод средств (объект MakeTransferOperationRequestSchema)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для операции покупки.

        :param request: Запрос на покупку (объект MakePurchaseOperationRequestSchema)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для оплату счетов/регулярных платежей.

        :param request: Запрос на оплату счетов/регулярных платежей (объект MakeBillPaymentOperationRequestSchema)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request.model_dump(by_alias=True))

    def make_cash_withdraw_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для вывода денежных средств.

        :param request: Запрос на вывод денежных средств (объект MakeCashWithdrawalOperationRequestSchema)
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            '/api/v1/operations/make-cash-withdrawal-operation',
            json=request.model_dump(by_alias=True)
        )

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request=request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request=request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request=request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request=request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_purchase_operation_api(request=request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request=request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdraw_operation_api(request=request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
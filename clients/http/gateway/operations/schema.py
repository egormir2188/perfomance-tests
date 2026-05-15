from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from enum import StrEnum

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"

class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека.
    """
    url: HttpUrl
    document: str

class OperationsSummarySchema(BaseModel):
    """
    Описание структуры сводки по операциям
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class OperationsQueryBaseSchema(BaseModel):
    """
    Базовая структура данных для query-параметров.
    """
    account_id: str = Field(alias="accountId")

class OperationsRequestBaseSchema(BaseModel):
    """
    Базовая структура данных для тела запроса.
    """
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class GetOperationsQuerySchema(OperationsQueryBaseSchema):
    """
    Структура данных для получения списка операций.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class GetOperationsResponseSchema(BaseModel):
    """
    Структура ответа для получения списка операций.
    """
    operations: list[OperationSchema]

class GetOperationsSummaryQuerySchema(OperationsQueryBaseSchema):
    """
    Структура данных для получения сводки по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура ответа для получения сводки по операциям.
    """
    summary: OperationsSummarySchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура ответа для получения чека по операции.
    """
    receipt: OperationReceiptSchema

class GetOperationResponseSchema(BaseModel):
    """
    Структура ответа для получения информации по операции.
    """
    operation: OperationSchema

class MakeFeeOperationRequestSchema(OperationsRequestBaseSchema):
    """
    Структура данных для списанию комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции снятия комиссии.
    """
    operation: OperationSchema

class MakeTopUpOperationRequestSchema(OperationsRequestBaseSchema):
    """
    Структура данных для пополнения счета.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции пополнения счета.
    """
    operation: OperationSchema

class MakeCashbackOperationRequestSchema(OperationsRequestBaseSchema):
    """
    Структура данных для начисления кэшбека.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции получения кэшбека.
    """
    operation: OperationSchema

class MakeTransferOperationRequestSchema(OperationsRequestBaseSchema):
    """
    Структура данных для перевода средств.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции перевода.
    """
    operation: OperationSchema

class MakePurchaseOperationRequestSchema(OperationsRequestBaseSchema):
    """
    Структура данных для покупки.
    """
    model_config = ConfigDict(populate_by_name=True)
    category: str = Field(default_factory=fake.category)

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура ответа для операции покупки.
    """
    operation: OperationSchema

class MakeBillPaymentOperationRequestSchema(OperationsRequestBaseSchema):
    """
    Структура данных для оплаты счетов и регулярных платежей.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Структура ответа платы счетов и регулярных платежей.
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationRequestSchema(OperationsRequestBaseSchema):
    """
    Структура данных для вывода денежных средств.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура ответа для вывода денежных средств.
    """
    operation: OperationSchema
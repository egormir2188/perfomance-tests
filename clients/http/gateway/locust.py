from locust import TaskSet, SequentialTaskSet

from clients.http.gateway.users.client import build_user_gateway_locust_http_client, UsersGatewayHTTPClient
from clients.http.gateway.cards.client import build_cards_gateway_locust_http_client, CardsGatewayHTTTPClient
from clients.http.gateway.accounts.client import build_accounts_gateway_locust_http_client, AccountsGatewayHTTPClient
from clients.http.gateway.documents.client import (
    build_documents_gateway_locust_http_client,
    DocumentGatewayHTTPClient
)
from clients.http.gateway.operations.client import (
    build_operations_gateway_locust_http_client,
    OperationsGatewayHTTPClient
)


class GatewayHTPPTaskSet(TaskSet):
    """
    Базовый TaskSet для HTTP-сценариев, работающих с http-gateway.

    Здесь создаются все необходимые API клиенты, которые будут доступны в последующих задачах (task).
    Используется, если порядок выполнения задач внутри таск-сета не имеет значения.
    """
    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient
    documents_gateway_client: DocumentGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTTPClient

    def on_start(self) -> None:
        """
        Метод вызывается перед запуском задач TaskSet.
        Здесь создаются API клиенты с использованием контекста окружения Locust.
        """
        self.users_gateway_client = build_user_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)

class GatewayHTPPSequentialTaskSet(SequentialTaskSet):
    """
    Базовый SequentialTaskSet для HTTP-сценариев, где важен порядок выполнения задач.

    Задачи внутри такого таск-сета будут выполняться строго по очереди — сверху вниз.
    Также здесь инициализируются те же API клиенты, что и в обычном TaskSet.
    """
    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient
    documents_gateway_client: DocumentGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTTPClient

    def on_start(self) -> None:
        """
        Создание API клиентов для последовательного сценария.
        """
        self.users_gateway_client = build_user_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
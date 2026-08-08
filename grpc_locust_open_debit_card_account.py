from locust import User, between, task

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from clients.grpc.gateway.users.client import build_users_gateway_locust_grpc_client, UsersGatewayGRPCClient
from clients.grpc.gateway.accounts.client import build_accounts_locust_gateway_grpc_client, AccountsGatewayGRPCClient


class OpenDebitCardAccountScenarioUser(User):
    host = 'localhost'
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.accounts_gateway_client = build_accounts_locust_gateway_grpc_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account_scenario(self):
        self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user.id)
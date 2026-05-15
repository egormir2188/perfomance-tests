from clients.http.gateway.users.client import build_user_gateway_http_client
from clients.http.gateway.cards.client import build_cards_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client


user_gateway_http_client = build_user_gateway_http_client()
cards_gateway_http_client = build_cards_gateway_http_client()
accounts_gateway_http_client = build_accounts_gateway_http_client()

create_user_response = user_gateway_http_client.create_user()
print('Create user response: ', create_user_response)

open_debit_card_account_response = accounts_gateway_http_client.open_debit_card_account(
    create_user_response.user.id
)
print('Open debit card account response: ',open_debit_card_account_response)

issue_physical_card_response = cards_gateway_http_client.issue_physical_card(
    create_user_response.user.id,
    open_debit_card_account_response.account.id
)
print('Issue physical card response: ', issue_physical_card_response)
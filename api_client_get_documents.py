from clients.http.gateway.users.client import build_user_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

user_gateway_http_client = build_user_gateway_http_client()
accounts_gateway_http_client = build_accounts_gateway_http_client()
documents_gateway_http_client = build_documents_gateway_http_client()

create_user_response = user_gateway_http_client.create_user()
print('Create user response: ', create_user_response)

open_credit_card_account_response = accounts_gateway_http_client.open_credit_card_account(
    create_user_response['user']['id']
)
print('Open debit card account response: ',open_credit_card_account_response)

get_tariff_documents_response = documents_gateway_http_client.get_tariff_document(
    open_credit_card_account_response['account']['id']
)
print('Get tariff documents response: ',get_tariff_documents_response)

get_contract_document_response = documents_gateway_http_client.get_contract_document(
    open_credit_card_account_response['account']['id']
)
print('Get contract document response: ',get_contract_document_response)


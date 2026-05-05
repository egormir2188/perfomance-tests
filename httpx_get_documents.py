import time
import httpx


create_user_payload = {
    "id": "string",
    "email": f"user{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
crate_user_response_data = create_user_response.json()

open_credit_card_account_payload = {
    "userId": crate_user_response_data["user"]["id"]
}
open_credit_card_account_response = httpx.post(
    'http://localhost:8003/api/v1/accounts/open-credit-card-account',
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()

account_id = open_credit_card_account_response_data["account"]["cards"][0]["accountId"]
get_tariff_documents_response = httpx.get(f'http://localhost:8003/api/v1/documents/tariff-document/{account_id}')
get_tariff_documents_response_data = get_tariff_documents_response.json()

print('Get Tariff Documents Response', get_tariff_documents_response_data)
print('Get Tariff Documents Status Code', get_tariff_documents_response.status_code)

get_contract_document_response = httpx.get(f'http://localhost:8003/api/v1/documents/contract-document/{account_id}')
get_contract_document_response_data = get_contract_document_response.json()

print('Get Contract Document Response', get_contract_document_response_data)
print('Get Contract Document Status Code', get_contract_document_response.status_code)
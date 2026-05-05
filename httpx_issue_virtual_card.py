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

open_debit_card_account_payload = {
    "userId": crate_user_response_data["user"]["id"]
}
open_debit_card_account_response = httpx.post(
    'http://localhost:8003/api/v1/accounts/open-debit-card-account',
    json=open_debit_card_account_payload
)
open_debit_card_account_response_data = open_debit_card_account_response.json()

issue_virtual_card_payload = {
    "userId": crate_user_response_data["user"]["id"],
    "accountId": open_debit_card_account_response_data["account"]["cards"][0]["accountId"]
}
issue_virtual_card_response = httpx.post(
    'http://localhost:8003/api/v1/cards/issue-virtual-card',
    json=issue_virtual_card_payload
)
issue_virtual_card_response_data = issue_virtual_card_response.json()

print('Issue Virtual Card Response:', issue_virtual_card_response_data)
print('Issue Virtual Card Status Code:', issue_virtual_card_response.status_code)
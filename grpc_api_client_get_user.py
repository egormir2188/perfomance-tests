from clients.grpc.gateway.users.client import build_user_gateway_grpc_client


users_gateway_grpc_client = build_user_gateway_grpc_client()

create_user_response = users_gateway_grpc_client.create_user()
print('Create user response:', create_user_response)

get_user_response = users_gateway_grpc_client.get_user(user_id=create_user_response.user.id)
print('Get user response:', get_user_response)
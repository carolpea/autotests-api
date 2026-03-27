import httpx


login_payload = {
    "email": "kudra@example.com",
    "password": "Test123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()
print(login_response.status_code)
print(login_response_data)


bearer_token = login_response_data["token"]["accessToken"]
headers = {
    "Authorization": f"Bearer {bearer_token}",
}
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(me_response.status_code)
print(me_response.json())

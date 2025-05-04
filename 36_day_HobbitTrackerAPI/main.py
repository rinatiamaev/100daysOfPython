import requests

TOKEN = "s7sn8snnns6"
USERNAME = "rinatiamaev"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : "s7sn8snnns6",
    "username" : "rinatiamaev",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name" : "my_reading Graph",
    "unit" : "pages",
    "type" : "int",
    "color" : "shibafu"
}


headers = {
    "X-USER-TOKEN" : TOKEN,
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)
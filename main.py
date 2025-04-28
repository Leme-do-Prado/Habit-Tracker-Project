import requests
from datetime import datetime

today = datetime.now()
print(f"Today is {today}!")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_username = "leandrolor"
pixela_user_token = ""

pixela_user_params = {
    "token": pixela_user_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=pixela_user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
graph_id = "leandrosgraph1"

graph_params = {
    "id": graph_id,
    "name": "Pages Read",
    "unit": "page",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": pixela_user_token
}
requests.post(url=graph_endpoint, json=graph_params, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}"
pixel_quantity = str(input("How many pages have you read today?"))
formatted_date = today.strftime("%Y%m%d")

pixel_params = {
    "date": formatted_date,
    "quantity": pixel_quantity,
}

requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)

update_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{formatted_date}"
new_quantity = str(input("What is the new number of pages?"))

new_pixel_params = {
    "quantity": new_quantity,
}

response = requests.put(url=update_endpoint, json=new_pixel_params, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{formatted_date}"
response = requests.delete(url = delete_endpoint, headers=headers)

import requests
import json

url = "http://www.ets100.com/parents/child/home"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

data = {
    "id": "XXX",
    "token": "XXX"
}

response = requests.post(url, headers=headers, data=data)

# 将响应内容解析为 JSON 格式并转化为字典
result = json.loads(response.content.decode())

id = result["data"]["id"]
name = result["data"]["name"]
cover = result["data"]["cover"]
phone = result["data"]["phone"]

print(f"ID: {id}")
print(f"Name: {name}")
print(f"Cover(URL): {cover}")
print(f"Phone: {phone}")

import requests
import json
from datetime import datetime

url = "http://www.ets100.com/parents/homework/list"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

data = {
    "account_id": "XXX",
    "user_id": "XXX",
    "offset": "1",
    "limit": "10",
    "token": "XXX",
    "type": "1"
}

response = requests.post(url, headers=headers, data=data)

# 将响应内容解析为 JSON 格式并转化为字典
result = json.loads(response.content.decode())

# 获取作业信息列表
homework_list = result["data"]["list"]

print("当前查询用户ID: " + data['account_id'])
for homework in homework_list:
    begin_time = datetime.fromtimestamp(int(homework["begin"]))
    end_time = datetime.fromtimestamp(int(homework["end"]))
    begin_time_str = begin_time.strftime('%Y-%m-%d %H:%M:%S')
    end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
    print("作业信息:")
    print("作业 ID：" + homework["id"])
    print("作业名称:" + homework["name"].replace('\n', ' '))
    if str(result["msg"]) == "None":
        print("老师留言: 无")
    else:
        print(f"老师留言: " + str(result["msg"]))
    if homework["point"] == 0:
        print("作业得分: 未完成")
    else:
        print("作业得分: " + str(homework["point"]))
    print("作业总分：" + str(homework["total_point"]))
    print("作业类型: " + homework["set_foreign_type"])
    print("作业开始时间：{}".format(begin_time_str))
    print("作业结束时间：{}".format(end_time_str))

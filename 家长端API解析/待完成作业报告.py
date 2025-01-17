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
data2 = {}


def process_homework_info(homework_id):
    # 更新data2字典中的"homework_id"键的值
    data2["homework_id"] = homework_id

    # 发送POST请求
    url = "http://www.ets100.com/parents/homework/detail"
    print(f"发起请求: {url}")
    print()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.post(url=url, headers=headers, data=data2)
    data2.update(json.loads(response.text))

    # print(data2)

    # 获取作业信息
    homework_info = data2["data"]["homework_info"]
    homework_name = homework_info["name"].replace('\n', ' ')
    total_point = homework_info["total_point"]
    type_name = homework_info["type_name"]
    avg_point = homework_info["avg_point"]
    complete = homework_info["complete"]
    end_time = homework_info["end"]
    highest_score = homework_info["highest_score"]

    # 获取效率之星列表
    efficiency_star_list = data2["data"]["efficiency_star"]
    efficiency_star_str = ''
    for star_info in efficiency_star_list:
        star_name = star_info["name"]
        star_point = star_info["point"]
        star_account_id = star_info["account_id"]
        efficiency_star_str += f'{star_name} ({star_account_id}): {star_point}分 \n'

    # 获取优秀之星列表
    excellent_star_list = data2["data"]["excellent_star"]
    excellent_star_str = ''
    for star_info in excellent_star_list:
        star_name = star_info["name"]
        star_point = star_info["point"]
        star_account_id = star_info["account_id"]
        excellent_star_str += f'{star_name} ({star_account_id}): {star_point}分 \n'

    print("作业相关信息:")
    print(f"作业名称:{homework_name}")
    print(f"作业类型: {type_name}")
    print(f"总分: {total_point}")
    print(f"平均分: {avg_point}")
    print(f"完成人数: {complete}")
    print(f"截止时间: {end_time}")
    print(f"最高分: {highest_score}")
    print(f"效率之星: \n{efficiency_star_str}")
    print(f"优秀之星: \n{excellent_star_str}")
    print()


# 发送POST请求获取数据
response = requests.post(url, headers=headers, data=data)

# 将响应内容解析为 JSON 格式并转化为字典
result = json.loads(response.content.decode())

# 获取作业信息列表
homework_list = result["data"]["list"]

for homework in homework_list:
    begin_time = datetime.fromtimestamp(int(homework["begin"]))
    end_time = datetime.fromtimestamp(int(homework["end"]))
    begin_time_str = begin_time.strftime('%Y-%m-%d %H:%M:%S')
    end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
    print("待完成作业信息:")
    print("作业 ID：" + homework["id"])
    # 往data2里塞一下作业ID
    data2["homework_id"] = homework["id"]
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
    print()

# 读取token.txt文件并生成data字典
try:
    with open("home_work_report_token.txt", "r") as f:
        for line in f:
            key, value = line.strip().split("\t")
            data2[key] = value
except Exception as e:
    print("Failed to read token.txt: %s", e)

print("Successfully read token from file")

# 处理每个作业的详细信息
for homework in homework_list:
    process_homework_info(homework["id"])

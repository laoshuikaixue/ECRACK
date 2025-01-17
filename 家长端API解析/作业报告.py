import json
import requests

data = {}

# 读取home_work_report_token.txt文件并生成data字典
try:
    with open("home_work_report_token.txt", "r") as f:
        for line in f:
            key, value = line.strip().split("\t")
            data[key] = value
except Exception as e:
    print("Error: Failed to read home_work_report_token.txt: %s", e)

print("Successfully read token from file")

# 发送POST请求
url = "http://www.ets100.com/parents/homework/detail"
print(f"发起请求: {url}")
print()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.post(url=url, headers=headers, data=data)
data = json.loads(response.text)

# print(data)

# 获取作业信息
homework_info = data["data"]["homework_info"]
homework_name = homework_info["name"].replace('\n', ' ')
total_point = homework_info["total_point"]
type_name = homework_info["type_name"]
avg_point = homework_info["avg_point"]
complete = homework_info["complete"]
end_time = homework_info["end"]
highest_score = homework_info["highest_score"]

# 获取个人信息
user_name = homework_info["user_name"]

# 获取效率之星列表
efficiency_star_list = data["data"]["efficiency_star"]
efficiency_star_str = ''
for star_info in efficiency_star_list:
    star_name = star_info["name"]
    star_point = star_info["point"]
    star_account_id = star_info["account_id"]
    efficiency_star_str += f'{star_name} ({star_account_id}): {star_point}分 \n'

# 获取优秀之星列表
excellent_star_list = data["data"]["excellent_star"]
excellent_star_str = ''
for star_info in excellent_star_list:
    star_name = star_info["name"]
    star_point = star_info["point"]
    star_account_id = star_info["account_id"]
    excellent_star_str += f'{star_name} ({star_account_id}): {star_point}分 \n'

print("作业相关信息:")
# 获取分数分布情况
distribution_list = data["data"]["distribution"]
for item in distribution_list:
    interval = item['interval']
    count = item['count']
    rate = item['rate']
    interval = interval.replace('[', '').replace(']', '').replace(")", '')
    print(f'得分区间: {interval}，人数: {count} 占比: {rate:.3f}')

# 获取学生个人得分情况 这里只能给已经开通E卡的人获取 所以就没写输出
student_score = data["data"]["student_score"]
student_point = student_score["point"]
complete_count = student_score["complete"]
submit_time = student_score["submit_time"]
use_time = student_score["use_time"]

print(f"作业名称:{homework_name}")
print(f"作业类型: {type_name}")
print(f"总分: {total_point}")
print(f"平均分: {avg_point}")
print(f"完成人数: {complete}")
print(f"截止时间: {end_time}")
print(f"最高分: {highest_score}")
print(f"效率之星: \n{efficiency_star_str}")
print(f"优秀之星: \n{excellent_star_str}")

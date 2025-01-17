# -*- coding: utf-8 -*-
# Time    : 2023/06/03 Edited: 2024/03/16
# Author  : LaoShui
# Warning : 该程序仅供学习交流，严禁用于商业用途，使用者请于24小时内删除

import json
import os
import re
import shutil
import subprocess
import threading
import time
from datetime import datetime

import psutil
import requests
import win32con
import win32gui
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


# 自义定输出
def custom_print(*text):
    dt = datetime.now()
    print(f"{dt.strftime('%Y-%m-%d %H:%M:%S:')}", *text)


# 缓存目录
dir_path = r'C:\Users\Administrator\AppData\Roaming\数字和字符组成的一个长文件夹名'

# 已打开的文件夹路径集合
opened_dirs = set()

# 发起请求Head
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows "
                  "WindowsWechat/WMPF XWEB/8297"
}


# 事件处理器
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory and not os.listdir(event.src_path):
            # 判断是否创建了新试题且该文件夹为空
            custom_print(f"[Info] 发现新试题: {event.src_path}")

            while True:
                window_title = "讯飞E听说中学-作业-首页"
                # 获取窗口句柄
                hwnd = win32gui.FindWindow(None, window_title)
                if hwnd != 0:
                    custom_print("[Info] win32gui 检测到窗体信息")
                    break

            # 停止监控 防止出现奇奇怪怪的报错
            custom_print("[Info] 正在结束文件监控 大约需要30秒")
            observer.stop()
            custom_print("[Info] 结束监控完成 开始解析答案数据")

            # 选择题所在JSON文件目录
            json_file_list = [
                os.path.join(event.src_path, 'content00010001', 'info.json'),
                os.path.join(event.src_path, 'content00010002', 'info.json'),
                os.path.join(event.src_path, 'content00010003', 'info.json'),
            ]

            # 解析选择题JSON
            for i, json_file in enumerate(json_file_list):
                if not os.path.isfile(json_file):
                    print(f"Error: File does not exist: {json_file}")
                    continue
                if i == 0:
                    print("选择题 第1大题:")
                elif i == 1:
                    print("选择题 第2大题-第1小题:")
                elif i == 2:
                    print("选择题 第2大题-第2小题:")
                else:
                    print(f"选择题 第{i}大题:")

                with open(json_file, 'r', encoding='utf-8') as f:
                    try:
                        info = json.load(f)
                        answers = info[1]['code_json_array']
                        answers = json.loads(answers)
                        for ans in answers:
                            print(f"小题{ans['xth']} 答案:{ans['answer']}")
                    except Exception as e:
                        print(f"Error: Failed to read or parse JSON file: {json_file}")
                        print(e)

            discourse_reading_path = os.path.join(event.src_path, 'content00010004', 'info.json')
            with open(discourse_reading_path, 'r', encoding='utf-8') as f:
                drdata = json.load(f)

            # 获取code_value字段
            html_content = ''
            for item in drdata:
                html_content += item['code_value'].replace('’', "'")

            print("语篇朗读内容:")
            print(html_content)
            print()

            file_numbers = ['content00010005', 'content00010006']

            for file_number in file_numbers:
                QA_path = os.path.join(event.src_path, file_number, 'content.json')

                with open(QA_path, 'r', encoding='utf-8') as f:
                    QAdata = json.load(f)

                # 获取问题列表、关键词列表和关键词
                questions = QAdata['info']['question']
                keywords_list = [ques['keywords'].split('|') for ques in questions]
                keywords = set()
                for keyword in keywords_list:
                    keywords.update(keyword)

                # 遍历问题列表获取答案
                for i, question in enumerate(questions):
                    answer_list = question['std']
                    print(f'情景问答问题{i + 1}的答案:')
                    for j, answer in enumerate(answer_list):
                        print(f'{j + 1}. {answer["value"]}'.replace('’', "'"))
                    print(f'情景问答问题{i + 1}的关键词:')
                    print(', '.join(keywords_list[i]))
                    print()

            topic_description_path = os.path.join(event.src_path, 'content00010007', 'content.json')
            with open(topic_description_path, 'r', encoding='utf-8') as f:
                tddata = json.load(f)

            # 获取话题简述要点和范文
            value_list = [ans['value'].replace('</p><p>', '').replace('<p>', '').replace('</p>', '') for ans in
                          tddata.get('info', {}).get('std', [])]

            value_info = tddata['info']['value']
            processed_value = value_info.replace('</br></p><p>', '\n').replace("</p><p>", "\n").replace('’', "'")
            print("话题简述:" + processed_value)
            print()

            for i, value in enumerate(value_list):
                print(f'话题简述示例范文{i + 1}:')
                print(value)
                print()


# 程序路径
program_path = r'E:\Program Files (x86)\ETS\Ets.exe'

# 解析作业报告
report_data = {}

data = {}

# 读取home_work_list_token.txt文件并生成data字典
try:
    with open("home_work_list_token.txt", "r") as f:
        for line in f:
            key, value = line.strip().split("\t")
            data[key] = value
except Exception as e:
    custom_print("Error: Failed to read home_work_list_token.txt: %s", e)

# 检测作业列表
url = "http://www.ets100.com/parents/homework/list"
custom_print(f"[Info] 发起POST请求: {url}")

response = requests.post(url, headers=headers, data=data)
data = json.loads(response.text)

# 将响应内容解析为 JSON 格式并转化为字典
result = json.loads(response.content.decode())

# 获取作业信息列表
homework_list = result["data"]["list"]

if homework_list:
    for homework in homework_list:
        begin_time = datetime.fromtimestamp(int(homework["begin"]))
        end_time = datetime.fromtimestamp(int(homework["end"]))
        begin_time_str = begin_time.strftime('%Y-%m-%d %H:%M:%S')
        end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
        custom_print("作业 ID：" + homework["id"])
        custom_print("作业名称:" + homework["name"].replace('\n', ' '))
        if str(result["msg"]) == "None":
            custom_print("老师留言: 无")
        else:
            custom_print(f"老师留言: " + str(result["msg"]))
        if homework["point"] == 0:
            custom_print("作业得分: 未完成")
        else:
            custom_print("作业得分: " + str(homework["point"]))
        custom_print("作业总分：" + str(homework["total_point"]))
        custom_print("作业类型: " + homework["set_foreign_type"])
        custom_print("作业开始时间：{}".format(begin_time_str))
        custom_print("作业结束时间：{}".format(end_time_str))
        report_data["homework_id"] = homework["id"]
        # 读取home_work_report_token.txt文件并生成data字典
        try:
            with open("home_work_report_token.txt", "r") as f:
                for line in f:
                    key, value = line.strip().split("\t")
                    report_data[key] = value
        except Exception as e:
            custom_print("Error: Failed to read home_work_report_token.txt: %s", e)

        custom_print("Success read home_work_report_token from file")
        custom_print("=" * 50)

        # 发送POST请求
        url = "http://www.ets100.com/parents/homework/detail"
        custom_print(f"[Info] 发起POST请求: {url}")

        response = requests.post(url=url, headers=headers, data=report_data)
        report_data = json.loads(response.text)
        custom_print("[Info] 成功返回作业信息")

        # 获取作业信息
        homework_info = report_data["data"]["homework_info"]
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
        efficiency_star_list = report_data["data"]["efficiency_star"]
        efficiency_star_str = ''
        if len(efficiency_star_list) == 0:
            efficiency_star_str = '暂无人完成'
        else:
            for star_info in efficiency_star_list:
                star_name = star_info["name"]
                star_point = star_info["point"]
                star_account_id = star_info["account_id"]
                # 这里因为有account_id就注释了
                # efficiency_star_str += f"{star_name} ({star_account_id}) - {star_point}分 "
                efficiency_star_str += f"{star_name}-{star_point}分 "

        # 获取优秀之星列表
        excellent_star_list = report_data["data"]["excellent_star"]
        excellent_star_str = ''
        if len(excellent_star_list) == 0:
            excellent_star_str = '暂无人完成'
        else:
            for star_info in excellent_star_list:
                star_name = star_info["name"]
                star_point = star_info["point"]
                star_account_id = star_info["account_id"]
                excellent_star_str += f"{star_name}-{star_point}分 "

        custom_print("=" * 50)

        # 获取学生个人得分情况
        student_score = report_data["data"]["student_score"]
        student_point = student_score["point"]
        complete_count = student_score["complete"]
        submit_time = student_score["submit_time"]
        use_time = student_score["use_time"]

        custom_print(f"作业名称:{homework_name}")
        custom_print(f"作业类型: {type_name}")
        custom_print(f"总分: {total_point}")
        custom_print(f"平均分: {avg_point}")
        # 获取分数分布情况
        distribution_list = report_data["data"]["distribution"]
        for item in distribution_list:
            interval = item['interval']
            count = item['count']
            rate = item['rate']
            interval = interval.replace('[', '').replace(']', '').replace(")", '')
            custom_print(f"得分区间: {interval}，人数: {count} 占比: {rate:.3f}")
        custom_print(f"完成人数: {complete}")
        custom_print(f"截止时间: {end_time}")
        custom_print(f"最高分: {highest_score}")
        print()
        custom_print(f"效率之星: {efficiency_star_str}")
        custom_print(f"优秀之星: {excellent_star_str}")
        print("=" * 50)


# 拦截E卡过期弹窗
def find_and_close_ewindow():
    while True:
        hwnd = win32gui.FindWindow(None, "讯飞E听说中学-E卡提示")  # 这个地方用sqy++获取的
        if hwnd != 0:
            win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            custom_print("[Info] win32gui 检测到窗体信息 已自动关闭E卡过期/到期提示")
        else:
            time.sleep(1)


t = threading.Thread(target=find_and_close_ewindow)
t.start()  # 开启线程，开始查找和关闭窗口
custom_print("[Info] 创建查找E卡过期/到期提示窗体线程")

# 检测程序是否在运行
for proc in psutil.process_iter(['name']):
    if proc.info['name'] == 'Ets.exe':
        custom_print("[Info] 程序已经在运行，结束程序")
        proc.kill()
        break

time.sleep(1)

# 获取缓存目录下所有带数字的文件夹和文件
dirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d)) and re.match(r'\d+', d)]

# 删除所有带数字的文件夹和文件
for d in dirs:
    dir_full_path = os.path.join(dir_path, d)
    custom_print(f"[Info] 删除文件夹: {dir_full_path}")
    shutil.rmtree(dir_full_path)

# 创建观察者对象并启动
observer = Observer()
observer.schedule(MyHandler(), dir_path, recursive=True)
observer.start()

if observer.is_alive():
    custom_print("[Info] 观察者正在运行")
else:
    custom_print("[Info] 观察者未在工作")

time.sleep(0.5)
# 打开程序
subprocess.Popen(program_path)
custom_print("[Info] 已打开程序")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

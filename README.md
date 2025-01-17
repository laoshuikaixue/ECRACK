# ECRACK

## 这个仓库是我初中时期对于科大讯飞E听说中学（ets100）的相关研究 目前已不再使用 停止更新 不保证可用性

## 项目介绍/使用须知

- ECRACK-仅解析.py:
1. 你需要修改代码中的缓存目录 这个目录需要你在`C:\Users\Administrator\AppData\Roaming\`下找到一个由数字和字母组成的文件夹 这个值可以去数据库获取 但是我懒得写了 因为之前是自己用
2. 设置程序路径
3. 如果想要体验完整的功能 你需要创建`home_work_report_token.txt` `home_work_list_token.txt`文件 这是E听说的微信家长端的请求头 包括了`account_id` `user_id` `token`等值 当时使用的是fidder 因此写了对fidder响应格式的解析 你可以手动修改代码构造一个请求头 **（这不是必须的 你完全可以删除掉/忽略这些代码 这就是对家长端信息的基础解析）**
4. 如果试题有变化 你可能需要手动修改代码中的`content00010001`类似的文件夹名称 因为现在不用了也懒得写自动类型判断了
5. 软件数据都是纯本地缓存解析 不存在任何和收发数据有关的操作
6. 代码比较屎 但是我懒得改了 希望能帮助到你
7. 以下是一份完整的程序实际执行输出：
```
2024-01-18 20:19:45: [Info] 发起POST请求: http://www.ets100.com/parents/homework/list
2024-01-18 20:19:45: 作业 ID：35676616
2024-01-18 20:19:45: 作业名称:1月18日听说考试
2024-01-18 20:19:45: 老师留言: 无
2024-01-18 20:19:45: 作业得分: 未完成
2024-01-18 20:19:45: 作业总分：30
2024-01-18 20:19:45: 作业类型: 听说模拟
2024-01-18 20:19:45: 作业开始时间：2024-01-18 20:17:00
2024-01-18 20:19:45: 作业结束时间：2024-01-19 22:00:59
Success 自动获取 第1大题 答案数据:
小题1 答案:C
小题2 答案:C
小题3 答案:B
小题4 答案:C
小题5 答案:A
Success 自动获取 第2大题-第1小题 答案数据:
小题1 答案:B
小题2 答案:B
Success 自动获取 第2大题-第2小题 答案数据:
小题1 答案:C
小题2 答案:A
小题3 答案:A

语篇朗读內容:
Last night I had a very strange dream. I dreamt I met an ET! I asked him where he was from and why he was here. He told me that he was from Mars and he won a competition to visit the earth. I asked him how old he was and he told me he was 500 years old. Then I asked him how long he was going to stay on the earth and when he was going back to Mars. He said he did not know. He liked the earth very much. He asked me if I would like to visit Mars one day. Then I heard my mum calling me loudly, "Wake up, Peter. It's time for school!" What a strange dream!

情景问答第一大题:
问答1的答案:
1. It is large.
2. It’s very large.
3. The new city swimming pool is very large.
4. The new city swimming pool is large.
5. The pool is very large.
6. The pool is large.
7. It is very large.
8. It’s large.
9. It is big.
10. It’s big.
11. It is very big.
12. It’s very big.
13. The new city swimming pool is very big.
14. The new city swimming pool is big.
15. The pool is very big.
16. The pool is big.
问答1的关键词:
Large, big

问答2的答案:
1. Free swimming lessons.
2. There will be free swimming lessons.
3. There will be free swimming lessons in the new water safety program next month.
4. There will be free swimming lessons in the program next month.
5. There will be free swimming lessons in the new water safety program.
6. There will be free swimming lessons in the program.
7. Swimming lessons.
8. There will be swimming lessons.
9. There will be swimming lessons in the new water safety program.
10. There will be swimming lessons in the program.
11. There will be swimming lessons in the new water safety program next month.
12. There will be swimming lessons in the program next month.
13. Free swimming classes.
14. There will be free swimming classes.
15. There will be free swimming classes in the new water safety program.
16. There will be free swimming classes in the program.
17. There will be free swimming classes in the new water safety program next month.
18. There will be free swimming classes in the program next month.
19. Swimming classes.
20. There will be swimming classes.
21. There will be swimming classes in the new water safety program.
22. There will be swimming classes in the program.
23. There will be swimming classes in the new water safety program next month.
24. There will be swimming classes in the program next month.
问答2的关键词:
swimming lessons, swimming classes

情景问答第二大题:
情景问答问题1的答案:
'1. We went to a football match.'
'2. George and I went to a football match last week.'
'3. Last week, George and I watched a football match.'
'4. George and I went to a football match.'
'5. He and I went to a football match.'
'6. We went to a football game.'
'7. George and I went to a football game.'
'8. He and I went to a football game.'
'9. We went to a football match last week.'
'10. He and I went to a football match last week.'
'11. We went to a football game last week.'
'12. George and I went to a football game last week.'
'13. He and I went to a football game last week.'
'14. Last week, we went to a football match.'
'15. Last week, George and I went to a football match.'
'16. Last week, he and I went to a football match.'
'17. Last week, we went to a football game.'
'18. Last week, George and I went to a football game.'
'19. Last week, he and I went to a football game.'
'20. We went to see a football match.'
'21. George and I went to see a football match.'
'22. He and I went to see a football match.'
'23. We went to see a football game.'
'24. George and I went to see a football game.'
'25. He and I went to see a football game.'
'26. We went to see a football match last week.'
'27. George and I went to see a football match last week.'
'28. He and I went to see a football match last week.'
'29. We went to see a football game last week.'
'30. George and I went to see a football game last week.'
'31. He and I went to see a football game last week.'
'32. Last week, we went to see a football match.'
'33. Last week, George and I went to see a football match.'
'34. Last week, he and I went to see a football match.'
'35. Last week, we went to see a football game.'
'36. Last week, George and I went to see a football game.'
'37. Last week, he and I went to see a football game.'
'38. We went to watch a football match.'
'39. George and I went to watch a football match.'
'40. He and I went to watch a football match.'
'41. We went to watch a football game.'
'42. George and I went to watch a football game.'
'43. He and I went to watch a football game.'
'44. We went to watch a football match last week.'
'45. George and I went to watch a football match last week.'
'46. He and I went to watch a football match last week.'
'47. We went to watch a football game last week.'
'48. George and I went to watch a football game last week.'
'49. He and I went to watch a football game last week.'
'50. Last week, we went to watch a football match.'
'51. Last week, George and I went to watch a football match.'
'52. Last week, he and I went to watch a football match.'
'53. Last week, we went to watch a football game.'
'54. Last week, George and I went to watch a football game.'
'55. Last week, he and I went to watch a football game.'
'56. We saw a football match.'
'57. George and I saw a football match.'
'58. He and I saw a football match.'
'59. We saw a football game.'
'60. George and I saw a football game.'
'61. He and I saw a football game.'
'62. We saw a football match last week.'
'63. George and I saw a football match last week.'
'64. He and I saw a football match last week.'
'65. We saw a football game last week.'
'66. George and I saw a football game last week.'
'67. He and I saw a football game last week.'
'68. Last week, we saw a football match.'
'69. Last week, George and I saw a football match.'
'70. Last week, he and I saw a football match.'
'71. Last week, we saw a football game.'
'72. Last week, George and I saw a football game.'
'73. Last week, he and I saw a football game.'
'74. We watched a football match.'
'75. George and I watched a football match.'
'76. He and I watched a football match.'
'77. We watched a football game.'
'78. George and I watched a football game.'
'79. He and I watched a football game.'
'80. We watched a football match last week.'
'81. George and I watched a football match last week.'
'82. He and I watched a football match last week.'
'83. We watched a football game last week.'
'84. George and I watched a football game last week.'
'85. He and I watched a football game last week.'
'86. Last week, we watched a football match.'
'87. Last week, he and I watched a football match.'
'88. Last week, we watched a football game.'
'89. Last week, George and I watched a football game.'
'90. Last week, he and I watched a football game.'
'91. We went to a soccer match last week.'
'92. Last week, we went to a soccer game.'
'93. George and I saw a soccer match last week.'
'94. Last week, he and I saw a soccer game.'
'95. We watched a soccer match last week.'
'96. Last week, George and I watched a soccer game.'
情景问答问题1的关键词:
Went football match, went football game, saw football match, saw football game, watched football match, watched football game, Went soccer match, went soccer game, saw soccer match, saw soccer game, watched soccer match, watched soccer game

情景问答问题2的答案:
'1. Rainy.'
'2. It was rainy.'
'3. It was rainy that day.'
'4. It was raining.'
'5. It was raining that day.'
'6. It was a rainy day.'
'7. It was a rainy day that day.'
'8. That day was a rainy day.'
'9. It rained.'
'10. It rained that day.'
'11. It was wet.'
'12. It was wet that day.'
情景问答问题2的关键词:
Rainy, raining, rained, wet

话题简述:
话题：A Wonderful Trip
要点提示：
1. went to …; had a wonderful time;
2. many things to see and to do; the best part was …;
3. tired but …

话题简述示例范文1:
My family went to Guangzhou last week. We had a wonderful time there. There were many things to see and to do in Guangzhou. The best part was taking a boat trip at night along the Pearl River. The city was very beautiful. After the trip, I felt tired but happy.

话题简述示例范文2:
I went to Nanjing with my parents last summer holiday. We had a wonderful time there. There were many things to see and to do in Nanjing. We listened to Kun Opera and took a boat trip on the lake. The best part was visiting the Confucius Temple. I felt tired but excited at the end of the trip.

话题简述示例范文3:
My parents and I went on a three-day trip to Hong Kong last month. We had a wonderful time there. We visited many places and ate lots of delicious food there. What’s more, we went to some shopping centres to do some shopping. The best part was visiting Hong Kong Disneyland. I had great fun there. I felt tired but very happy after the trip. I will never forget this wonderful trip.
```

- 家长端API解析: 都是一些简单的解析代码 仅供参考

## 后记
顺带提一嘴 当时下载老师布置的作业是不需要E卡的 但是开始练习需要 因此你可以通过替换掉免费练习题达到不开通E卡练习的效果 当然数据也不会上传 这种练习方式需要使用本地引擎 现在不知道这种方式可不可以
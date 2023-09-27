# # A     B       C
# # x     Ideal   Ves
# # a = [[6.0, 10.0, 0.6], [8.0, 20.0, 0.3], [16.0, 30.0, 0.3]]                                                                   a = [
# #Команда (років досвіду)
# #Твітер (кількість фоловерів)
# #Технологія ( тут загалом у кожної своя оцінка)
# #api twitter (можем узнать кто на кого подписан)
# a = [
#     [6.0, 10.0, 0.6],
#     [8.0, 20.0, 0.2],
#     [16.0, 30.0, 0.2]
# ]
# sum = 0
#
# # 1 cycle - for ideal scoring (B * C)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         #print(a[i][j], end=' ')
#         #print(a[i][1] * a[i][2], end=' ')
#         x = a[i][1] * a[i][2]
#         sum += x
#     print(x)
# print('Sum: ', round(sum/3, 1))
# print('')
#
# # 2 cycle - for X scoring (A * C)
# sum = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         #print(a[i][j], end=' ')
#         #print(a[i][1] * a[i][2], end=' ')
#         y = a[i][0] * a[i][2]
#         sum += y
#     # print(y)
#     print("%.2f" % y)
# # print('Sum: ', "%.2f" % sum/3)
# print('Sum: ', round(sum/3, 1))
# print('')

from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token=os.getenv("agg2GtFZwxJHbH7bvMD-cOKUuv9OlkRyA6kfLfjZzKy6qaqHkdzxUxjSTkgBfOqS7j0jog.")

bard = Bard(token=token)

result = bard.get_answer("What is a current stock price of NVDA?")
print(result)
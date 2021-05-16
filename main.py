# # import threading
# # import time
# # import random
# #
# # def worker(number):
# #     sleep = random.randrange(1, 10)
# #     time.sleep(sleep)
# #     print("I'm worker {}, i slept for {} sec".format(number, sleep))
# #
# #     for i in range(5):
# #         t = threading.Thread(target=worker, args=i)
# #         t.start()
# #
# # print("All threads are queued, let's see")
#
#
# def bubble_sort(nums):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 swapped = True
#
#
# list = [3, 5, 2, 0, 8]
# bubble_sort(list)
# print(list)
#
#
# def selection_sort(nums):
#     for i in range(len(nums)):
#         low = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[low]:
#                 low = j
#         nums[i], nums[low] = nums[low], nums[i]
#
#
# selection_sort(list)
# print(list)
#
#
# def inser(nums):
#     for i in range(1, len(nums)):
#         item = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > item:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = item
#
#
# inser(list)
# print(list)
#
# # Piramida_sort
# def heapify(nums, heap_size, root_index):
#     largest = root_index
#     left_child = (2 * root_index) + 1
#     right_child = (2 * root_index) + 2
#
#     if left_child < heap_size and nums[left_child] > nums[largest]:
#         largest = left_child
#
#     if right_child < heap_size and nums[right_child] > nums[largest]:
#         largest = right_child
#
#     if largest != root_index:
#         nums[root_index], nums[largest] = nums[largest], nums[root_index]
#         heapify(nums, heap_size, largest)
#
#
# def heap_sort(nums):
#     n = len(nums)
#     for i in range(n, -1, -1):
#         heapify(nums, n, i)
#
#     for i in range(n - 1, 0, -1):
#         nums[i], nums[0] = nums[0], nums[i]
#         heapify(nums, i, 0)
#
#
# heap_sort(list)
# print(list)
#
#
# #Sortirovka sliyaniem
# def merge(left, right):
#     sorted_list = []
#     left_index = right_index = 0
#
#     left_lenght, right_lenght = len(left), len(right)
#
#     for _ in range(left_lenght + right_lenght):
#         if left_index < left_lenght and right_index < right_lenght:
#             if left[left_index] <= right[right_index]:
#                 sorted_list.append(left[left_index])
#                 left_index += 1
#             else:
#                 sorted_list.append(right[right_index])
#                 right_index += 1
#         elif left_index == left_lenght:
#             sorted_list.append(right[right_index])
#             right_index += 1
#         elif right_index == right_lenght:
#             sorted_list.append(left[left_index])
#             left_index += 1
#     return sorted_list
#
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#
#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])
#     return merge(left_list, right_list)
#
# random_list = [120, 45, 68, 250, 176]
# random_list = merge_sort(random_list)
# print(random_list)
#
#
# def partition(nums, low, high):
#     pivot = nums[(low+high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         nums[i], nums[j] = nums[j], nums[i]
#
# def quick(nums):
#     def _quick(items, low, high):
#         if low < high:
#             split = partition(items, low, high)
#             _quick(items, low, split)
#             _quick(items, split + 1, high)
#
#     _quick(nums, 0, len(nums) - 1)
#
# random_list_of_nums = [22, 5, 1, 18, 99]
# quick(random_list_of_nums)
# print(random_list_of_nums)

# class Instruments(object):
#     symbols = []
#
#     def add(self, symbol: str) -> None:
#         self.symbols.append(symbol)
#
#     def get(self) -> dict:
#         return self.symbols
#
# nasdaq = Instruments()
# nasdaq.add('AMD')
# nasdaq.add('AAPL')
#
# moex = Instruments()
# moex.add('GAZP')
# moex.add('SBER')

# print(moex.get())

from xml.dom.minidom import parseString
# from xml.dom import minidom
# import urllib.request
# import requests
# #
# page = requests.get(
#     'http://www.cbr.ru/scripts/XML_daily.asp').text
# xmldoc = minidom.parse(page)
#
# # source = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp ")
# # xmldoc = minidom.parse(source)
#
# find = ['R01820']
# valutes = xmldoc.getElementsByTagName('Valute')
# for valute in valutes:
#     id = valute.getAttribute("ID")
#     value = valute.getElementsByTagName("Value")[0]
#     if id in find:
#         print (f'Курс йены к рублю = {value.firstChild.data} ')

# JPY = xmldoc.getElementsByTagName('Value')[33]






import requests





import urllib.request
from xml.dom import minidom
from datetime import date,timedelta
import numpy as np
id_list= []
currentDay = date.today()



# for i in range(90):
#     requestedDay = currentDay - timedelta(days=i)
#     source = urllib.request.urlopen(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={requestedDay}")
#     valutes = xmldoc.getElementsByTagName("Valute")
#     for valute in valutes:
#         id = valute.getAttribute("ID")
#         print(id)
#         value = valute.getElementsByTagName("Value")[0]
#         print(value.firstChild.data)
#         id_list.append
#


source = urllib.request.urlopen(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={currentDay}")
xmldoc = minidom.parse(source)
valutes = xmldoc.getElementsByTagName("Valute")



# for valute in valutes:
#         id = valute.getAttribute("ID")
#         value = valute.getElementsByTagName("Value")[0]
#         id_list.append([value.firstChild.data])
#
# a = [[0] * 90 for i in range(len(valutes))]
#
# for valute in valutes:
#     for j in range(90):
#         a[i][0] = i+1
#         a[i][j]= value.firstChild.data
#
# for row in a:
#     print(' '.join([str(elem) for elem in row]))



# r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("</Valute>")
# NAME = 'Гонконгский доллар'
#
# for n in r:
#     if n.count(NAME):
#         nominal = (int(n[n.find('<Nominal>') + len('<Nominal>'):n.find('</Nominal>')]))
#         value = (float(n[n.find('<Value>') + len('<Value>'):n.find('</Value>')].replace(',', '.')))
# print(f"{nominal} {NAME} равен {value} рублей")











# import requests
# city = 'Moscow, RU'
# api_url = 'https://api.openweathermap.org/data/2.5/weather'
#
# params = {
#     'q': city,
#     'appid': 'ddf2b6d9895517e9e700f687e0e0fe86',
#     'units': 'metric'
#
# }

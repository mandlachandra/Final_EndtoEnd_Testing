# from openpyxl import load_workbook
#
# fruits1 = ["apple", "banana", "cherry", "Mango", "Orange"]
# fruits2 = ["apple", "banana", "cherry", "palm", "guava", "pier"]
#
# s1 = set(fruits1)
# s2 = set(fruits2)
#
# common_fruits = s1 & s2
# print("common_fruits",common_fruits)
#
# workbook = load_workbook("C://Users//DELL//OneDrive//Desktop//New Microsoft Excel Worksheet (2).xlsx")
# sheet = workbook.active
# sheet.title = "common_fruits"
#
# #
# sheet.cell(row=1,column=1,value="fruit Name")
#
# for idx, fruit in enumerate(common_fruits,start=2):
#     sheet.cell(row=idx,column=1,value=fruit)
#
# workbook.save("common_fruits.xlsx")
# # print("data written to common_fruits.xlsx")

from openpyxl import load_workbook

fruits1 = ["apple", "banana", "cherry", "Mango", "Orange"]
fruits2 = ["apple", "banana", "cherry", "palm", "guava", "pier"]

s1 = set(fruits1)
s2 = set(fruits2)
common_fruits = s1 & s2
print("common_fruits",common_fruits)

workbook = load_workbook("C://Users//DELL//OneDrive//Desktop//New Microsoft Excel Worksheet (2).xlsx")
sheet = workbook.active
sheet.title = "common_fruits_names"

sheet.cell(row=1,column=1,value="fruit name")

for idx, fruit in enumerate(common_fruits,start=2):
    sheet.cell(row=idx,column=1,value=fruit)

workbook.save("common_fruit_names")







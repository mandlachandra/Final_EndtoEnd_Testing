# #Writing to a Text File
# with open("sample.txt","w") as file:
#     file.write("Hello, this is the first line.\n")
#     file.write("This is the second line.\n")
#
# #Appending to a Text File
# with open("sample.txt","a") as file:
#     file.write("This is an extra line added later.\n")
#
# #Reading from a Text File
# #read the whole line
# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)
#
# #read line by line
# with open("sample.txt","r") as file:
#     for line in file:
#         print(line.strip()) #strip removes extra newline
#
# #read all lines in a list
# with open("sample.txt","r") as file:
#     lines = file.readlines()
#     print(lines) #list of lines
#
# #writing and readling together
# with open("sample.txt","w") as file:
#     file.write("python is awesome.\n")
#     file.write("file handling is esay.\n")
#
# #reading
# with open("sample.txt","r") as file:
#     print(file.read())
#
# #with open() ->It automatically closes the file after use, even if an error occurs
#
# #Example: Count Lines & Words
# filename = "sample.txt"
#
# #initialize counters
# line_count = 0
# word_count = 0
#
# with open(filename,"r") as file:
#     for line in file:
#         line_count +=1
#         word_count +=len(line.split())
#
# print(f"Total lines: {line_count}")
# print(f"Total words: {word_count}")
#
# #count only words
#
# with open("sample.txt") as file:
#     text = file.read()
#     words = text.split()
#     print("Total words:",len(words))
#
# #count only lines
#
# with open("sample.txt","r") as file:
#     lines= file.readlines()
#     print("Total lines:",len(lines))
#
# #Find and replace in a text file
# filename = "sample.txt"
#
# with open(filename,"r") as file:
#     content = file.read()
#
# #replace occurrence
# content = content.replace("python","java")
#
# #write updated content back to the file
# with open(filename,"w") as file:
#     file.write(content)
#
# print("Text replaced successfully")
#
# #Rename a file
# import os
#
# old_name = "old_file.txt"
# new_name = "new_file.txt"
#
# os.rename(old_name,new_name)
# print(f"file renamed from {old_name} to {new_name}")
#
# #move a file
# old_path = "file.txt"
# new_path = "C:/users/dell/documents/file.txt" #new location
# os.rename(old_path,new_path)
# print(f"file moved to {new_path}")

#List all files in a directory
import os

#directory pah
folder_path = "C://Users//DELL//Documents"

files = os.listdir(folder_path)

# files_dict = {i+1: file for i, file in enumerate(files)}
files_dict = {i+1: file for i, file in enumerate(files)}
print(files_dict)

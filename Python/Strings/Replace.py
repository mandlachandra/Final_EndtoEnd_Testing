#1.Replace a word in string
s = "welcome to india"
result1 = s.replace("welcome","welcome"[::-1])
print(result1)

#2.replace only the first occurrence of the word
s1 = "apple apple apple"
print(s1.replace("apple","orange",1))

#3.Replcae all spaces with hyphens
s2 = "hello world python"
print(s2.replace(" ","-"))

#4.Replace vowels with a specific character
#replace all vowels in "welcome" with *
s3 = "welcome"
vowels = "aeiouAEIOU"
for v in vowels:
    s3 = s3.replace(v,"*")

print(s3)

#5.Replace multiple words
#replace "welcome" with "hi" and "india" with "bharat"
s4 = "welcome to india"
s4 = s4.replace("welcome","hi").replace("india","bharat").replace("to","me")
print(s4)

#6.Replace only whole words (not part of other words)
import re

s5 = "cat scatter category"
result = re.sub(r"\bcat\b","dog",s5)
print(result)

#Replace character at a specifi position
#  Replace the 3rd character in "python" with x

s6 = "python"
s6 = s6[:2]+"X"+s6[3:]
print(s6)

#remove all occurrence of a word
s7 = "this is python. python is fun"
print(s7.replace("is",""))

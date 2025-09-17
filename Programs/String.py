#reverse a string

str = "mandla chandra sekhar"
print(str[::-1])

str1 = "chandra"
reversed_s = ''.join(reversed(str1))
print(reversed_s)

#uisng a loop
s = "mandla chandra sekharanc"
rev_s = " "
for c in s:
    rev_s = c + rev_s
print(rev_s)
#....................
#check if palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

#count vowels and constants
def count_vowels_constants(s):
    vowels = "aeiou"
    vowels_count =0
    constant_count =0

    for ch in s:
        if ch.isalpha(): #consider only numbers
            if ch in vowels:
                vowels_count+=1
            else:
                constant_count+=1
    return vowels_count, constant_count

s = "Hello world india 2023"
v,c  = count_vowels_constants(s)
print(f"vowels: {v}, constants: {c}")

#how to remove duplicates
def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result
print(remove_duplicates("programming"))

#capitalize first letter of each word
ss = "mandla chandra sekhar"
result = ss.title()
print(result)

#compress a string
def compress_string(s):

    result = ""
    count =1

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            result +=1
        else:
            result+=s[i-1] + str(count)
            count = 1

    result +=s[-1] + str(count)

    return result

print(compress_string("aaaaaabbbbcccdd"))



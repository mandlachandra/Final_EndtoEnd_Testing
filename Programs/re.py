# import re
#
# s = "hello@!# world 1234"
#
# result = re.sub(r'[^A-Za-z0-9 ]+',s)
# print(result)

def compress_string(s):

    result =""
    count =1

    for i in range(1,len(s)):
        if s[i] ==s[i-1]:
            count+=1
        else:
            result += s[i-1] + str(count)
            count =1

    result +=str(count)+s[-1]
    return result
print(compress_string("aaaaaaaaabbbbbbbccccddd"))
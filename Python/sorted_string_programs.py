#Sort Characters in a String (Alphabetical Order)
# s = "banana"
# sorted_s = ''.join(sorted(s))
# print(sorted_s) #output = aaabnn
#
# #Explanation = sorted(s) returns a list of characters in order, we use join() to convert it back to string
#
# #Sort Words in a Sentence Alphabetically
# sentence = "python is a great language"
# words = sentence.split()
# sorted_words = sorted(words)
# print(sorted_words)
#
# # Sort Words by Length (Ascending or Descending)
# words = "apple manfo kiwi fig banana"
# word = words.split()
# sorted_by_length = sorted(word,key=len)
# print(sorted_by_length)
#
# sorted_desc = sorted(word,key = len,reverse=True)
# print(sorted_desc)
#
# #sort string by frequency of strings
# from collections import Counter
# def sort_by_frequency(s):
#     freq = Counter(s)
#     return ''.join(sorted(s,key=lambda x:(freq[x])))
#
# print(sort_by_frequency("bbbccccnddjdc"))

#sort words with digits at the end(Natural sort)
# import re
#
# def sort_words_with_numbers(sentence):
#     words = sentence.split()
#     return sorted(words,key=lambda x:int(re.findall(r'\d+',x)[0]))
# print(sort_words_with_numbers("kiwi1 mango32 app02 fig36"))

# #sort string in reverse alphabetical order
# s = "openai"
# print(''.join(sorted(s,reverse=True)))

#Sort words in sentence by vowel count
# def count_vowels(word):
#     return sum(1 for char in word if char in 'aeiouAEIOU')
#
# sentence = "hello apple mango and orange"
# words = sentence.split()
# sorted_words = sorted(words, key=count_vowels,reverse=True)
# print(sorted_words)

#Custom Sort: All Vowels First Then Consonants
# def custom_sort(s):
#     return ''.join(sorted(s, key=lambda x: (x not in 'aeiouAEIOU', x)))

# print(custom_sort("education"))

#sort list of strings Ignoring case
# words = ['Banana','apple','mango','kiwi']
# print(sorted(words,key=lambda x:x.lower()))

#Sort a List of Sentences by Number of Words
sentences = [
    "python is great",
    "hello",
    "i love my count india",
    "i am going to rule and i will control my sugar levels and get back by rod back"
]
sorted_sentences = sorted(sentences, key=lambda s : len(s.split()))
print(sorted_sentences)

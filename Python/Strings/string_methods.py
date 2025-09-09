#1. Case Conversion Methods
s = "mandla chandra sekhar"
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())

#2.Searching Methods
print(s.find("d"))
print(s.rfind("a"))
print(s.index("ch"))
print(s.count("a"))
print(s.startswith("mand"))
print(s.endswith("har"))

#modifying methods
print(s.replace("a","@"))
print(s.strip())
print(s.ljust(25,"*"))
print(s.rjust(25,"&"))
print(s.center(25,"-"))

#Splitting & joining
print(s.split("a"))
print('-'.join(s))
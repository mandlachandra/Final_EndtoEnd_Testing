nums = [10,20,30,40]

#1.append()
nums.append(50)
print(nums)

#2.clear()
nums.clear()
print(nums)

#3.copy()
nums = [1,2,3]
copy_nums = nums.copy()
print(copy_nums)

#4.count(x)
nums = [1,2,3,4,5,6,2,4,6,6,6]
print(nums.count(6))

#extend(iterable)
nums = [4,5,6]
nums.extend([8,9])
print(nums)

#index(x[,start[,end]])
nums = [10,20,30]
print(nums.index(20))

#insert(i,x)
nums = [10,40,60]
nums.insert(1,20)
print(nums)

#pop([i])
nums =[4,6,7,8,9]
print(nums.pop())
print(nums.pop(1))
print(nums)

#remove(x)
nums = [10,30,40,60]
nums.remove(30)
print(nums)

#reverse()
nums = [1,2,3,4]
nums.reverse()
print(nums)

#sort()
nums = [13,5,87,9]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
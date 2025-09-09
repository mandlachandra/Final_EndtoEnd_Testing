data = {"a": 1, "b": 2, "c": 3}

# # forward part
# forward = "".join(k * v for k, v in data.items())
#
# # backward part
# backward = "".join(k * v for k, v in reversed(data.items()))
#
# # final output
# output = forward + "-" + backward
# print(output)  # abbccc-cccbba

#forward part
forward = ''.join(k * v for k ,v in data.items())




#backword part
backward = ''.join(k * v for k, v in reversed(data.items()))

output = forward + "-" + backward
print(output)
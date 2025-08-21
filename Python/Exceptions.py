def divide(a,b):
    try:
        result = a/b
        print("result:",result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Execution completed.")

divide(10,2)
divide(5,0)

#Real time use case
try:
    file = open("data.txt","r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("file not found")
finally:
    try:
        file.close()
    except:
        pass
    print("file operation completes")

import math

function = input("Enter the function to get a table with values: ")
result = {}
n = 91

if(function == "sin"):
    for i in range(0, n):
        result[i] = math.sin(i * math.pi / 180)
elif(function == "cos"):
    for i in range(0, n):
        result[i] = math.cos(i * math.pi / 180)
elif(function == "tg"):
    for i in range(0, n):
        result[i] = math.tan(i * math.pi / 180)
elif(function == "ctg"):
    for i in range(0, n):
        sinValue = math.sin(i * math.pi / 180)
        cosValue = math.cos(i * math.pi / 180)
        if(sinValue == 0):
            result[i] = "-"
        else:
            result[i] = cosValue / sinValue
        
print(result)
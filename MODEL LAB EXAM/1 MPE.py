temp = float(input("Enter temperature: "))
if temp <= 20:
    cold = 1
    warm = 0
    hot = 0
elif temp <= 30:
    cold = 0
    warm = 1
    hot = 0
else:
    cold = 0
    warm = 0
    hot = 1
if cold == 1:
    speed = 20
    print("Temperature: Cold")
elif warm == 1:
    speed = 50
    print("Temperature: Warm")
else:
    speed = 100
    print("Temperature: Hot")
print("Fan Speed:", speed, "%")

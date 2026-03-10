temp = int(input("Enter Temperature: "))
hum = int(input("Enter Humidity: "))
rain = int(input("Enter Rainfall: "))
wet = int(input("Enter Leaf Wetness Duration: "))

if hum > 85 and wet > 10:
    print("High Risk")
    if "High Risk" and rain > 100:
        print("Critical Alert")

elif temp >= 20 and temp <= 30 and rain > 50:
    print("Medium Risk")

elif hum < 40 and rain < 10:
    print("Low Risk")

else:
    print("Moderate Risk")


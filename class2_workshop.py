distance = int(input("Enter your distance : "))

if 5<= distance <= 50:
    print("ํYour have to pay 10 bath")
elif 51<= distance <=100:
    print("ํYour have to pay 15 bath")
elif 101<= distance <= 300:
    print("Your have to pay 25 bath")
elif 301<= distance <=500:
    print("Your have to pay 35 bath")
elif distance > 500:
    print("Your have to pay 45 bath")
else:
    print("ไม่ต้องจ่าย")

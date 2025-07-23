# haverice = True
# havespoon = False
# havehand = True

# if haverice:
#     if havespoon:
#         print("กินข้าว")
#     elif haverice:
#         print("กินข้าวเหนียว")


# score = int(input("Enter your score :"))

# if score >=50:
#     if score <= 100:
#         if score >= 80:
#             print("A")
#         if score >= 70:
#             if score <80:
#                 print("B")
#         if score  >= 60:
#             if score < 70:
#                 print("C")
#         if score >=50:
#             if score < 60:
#                 print("D")


# for i in range(1,5):
#     print(i)
#     print("สวัสดี")

# i = 0
# while i <8:
#     print(i)
#     i +=1


# while True:
#     choice = int(input("กรอก 1 เพื่อบวกเลข,กรอก 2 เพื่อออก"))
#     if choice == 1:
#         num = int(input("เลขที่ต้องการจะบวก"))
#         sum = 0
#         for i in range(num):
#             num1 = int(input("กรอกเลข"))
#             sum = sum + num1
#         print(sum)
#     if choice == 2:
#         break


while True:
    blood_monster = 100
    gun = 20
    sword = 10
    boom = 5

    menu = int(input("กด1 เพื่อต่อสู้กับมอนสเตอร์ หรือ กด2 เพื่อออกจากเกม : "))

    if menu == 1:

        number_of_hits = int(input("จะตีกี่ครั้ง : "))
        for i in range(number_of_hits):
            attack = int(input("1.GUN(20) 2.sword(10) 3.boom(5) จงเลือกอาวุธมาสู้ซะ!!! : "))
            a = blood_monster
            gun = 20
            sword = 10
            boom = 5

            if attack == 1:
                blood_monster = a- gun
                print("เลือดมอนเตอร์",blood_monster)
            elif attack == 2:
                blood_monster =a- sword
                print("เลือดมอนเตอร์",blood_monster)
            elif attack == 3:
                blood_monster =a- boom
                print("เลือดมอนเตอร์",blood_monster)

        if blood_monster == 0:
            print("monsterตาย")
        if blood_monster> 0:
            print("ผู้เล่นตาย")
        if blood_monster < 0:
            print("monsterยังไม่ตาย")




    if menu == 2:
        print("ออกจากเกม")
        break


     

        
    

##โปรแกรมคำนวนระยะทาง
'''
0-1 = 35
2-10 = 5.5b/km
11 - 20 = 6.5b/km
21 - 40 = 7.5b/km
41 - 60 = 8.0b/km
61 -80 = 9.0b/km
81 + = 10.5 b/km
'''
import math
while True :

    distance = float(input('กรอกข้อมูล :'))
    distance2 = distance - math.floor(distance)
    distance = math.floor(distance)
    check = {1:5.5,10:6.5,20:7.5,40:8,60:9,80:10.5}

    box = 0

    for i in range(1,distance+1):
        if distance < 0 :
            print('ERROR')
            break
        if i == 1 :
            tx = 35 
        elif i > 1 and i <= 10 :
            tx = 5.5
        elif i >  10 and i <= 20 :
            tx = 6.5
        elif i >  20 and i <= 40 :
            tx = 7.5
        elif i >  40 and i <= 60 :
            tx = 8
        elif i >  60 and i <= 80 :
            tx = 9
        else :
            tx = 10.5

        box += tx 
    if distance in check :
        tx = check[distance]
        extra = distance2 * tx
    else :
        tx = tx
        extra = distance2 * tx

    calculate = round(box + (extra))
    print(f'ระยะทางที่ใช้ในการเดินทาง : {distance+distance2} กิโลเมตร\n ค่าโดยสารรวมเป็น : {calculate} บาท')
    print('---------------------------------------------')



    

    

cal=int(input("1.입력한 수식 계산 2.두 수 사이의 합계 : "))

if cal == 1:
   cal_1 = input("***수식을 입력하세요 : ")
   result_1 = eval(cal_1)
   print(f"결과: {result_1}")
elif cal == 2:
   cal_2_1= int(input("첫번쨰 숫자를 입력하세요: "))
   cal_2_2= int(input("두번쨰 숫자를 입력하세요: "))
   result_2=(cal_2_2 * (cal_2_2 + 1) // 2) - ((cal_2_1 - 1) * cal_2_1 // 2)
   print("%d+....+%d = %d 입니다" % (cal_2_1,cal_2_2,result_2))
else :
   print("잘못된 숫자 입니다")
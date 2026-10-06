##while True:
   ## print("ㅋ ", end= "")
    

##for i  in range(1, 100):
   ## print("for 문을 %d번 실행했습니다." % i)
    ##break

##hap = 0
##a, b = 0, 0

##while True :
    ##a = int(input("더할 첫 번째 수를 입력하세요 : "))
    ##if a ==0 :
       ## break
   ## b = int(input("더할 두 번째 수를 입력하세요 : "))
   ## hap = a + b
   ## print("%d + %d = %d" %(a, b, hap))

##print("0을 입력해 반복문을 탈출했습니다.")

##hap, i = 0, 0

##for i in range(1,101) :
    ##if i %3 == 0 :
       ## continue

    ##hap += i

##print("1~100의 합계(3의 배수 제외) : %d" % hap)


##전역 변수 선언 부분##
i,k, guguline = 0, 0, ""


## 메인 코드 부분##
for i in range(2,10):
    guguline = guguline + ("# %d단 #" % i)


print(guguline)




for i in range(1, 10):
    guguline = ""
    for k in range(2, 10):
        guguline = guguline + str("%2dX %2d= %2d" % (k, i, k * i))
    print(guguline)



##for i in range(1, 51):
    ##print("*" * i)

for i in range(51, 0, -2):
    print(" " * ((51 - i) // 2) + "*" * i)

for i in range(1, 52, 2):
   print(" " * ((51 - i) // 2) + "*" * i)
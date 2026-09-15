##a= input()
##b= input()


##result1 = a*b
##result2 = a+b
##result3 = a-b
##result4 = a/b
##print(a,"*", b, "=" , result1)
##print(a,"+", b , "=" , result2)
##print(a,"-", b , "=" , result3)
## print(a,"/", b , "=" , result4)

##data='안녕' +\
     ##'하세요' +\
    ## '파이선!'
##print(data)

import turtle ##거북이 그래픽 라이브러리를 불러옵니다.
import random ##랜덤 값 생성을 위한 라이브러리


## 함수 선언 부분 ##
def screenRightClick(x, y):
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenLeftClick(x, y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x, y):
    global r,g,b
    tSize= random.randrange(1,10)
    turtle.shapesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()

## 변수 선언 부분 ##
pSize = 10 
r,g,b= 0.0, 0.0, 0.0


## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidClick,2)
turtle.onscreenclick(screenRightClick,3)

    
turtle.done()

    
##t = turtle.Turtle()

##t.speed(3)
##t.pensize(10)
##t.pencolor("red")



##t.shape('arrow')

##t.forward(200)
##t.right(90)
##t.forward(200)
##t.right(90)
##t.forward(200)
##t.right(90)
##t.forward(200)
##t.right(90)
##t.forward(200)

##turtle.done()
import turtle
turtle.title("Prawit's Stupa")
turtle.bgcolor("black")


tao = turtle.Pen()
tao.pencolor("yellow")
tao.shape('turtle')




def Pyramid():
    for i in range(90):
        tao.speed(20)
        tao.forward(i*2)
        tao.right(90)


def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()





def Stupa():
    taowalk = 0
    while taowalk < 90:
        print('เต่าเดินไปแล้ว {} ครั้ง'.format(taowalk))
        taowalk = taowalk + 1
        tao.speed(20)
        tao.forward(1*taowalk)
        tao.right(44)
        if taowalk == 90:
            print('เต่าเหนือยแล้วไม่มีคนพยุง')
    
Go(200,0)
Pyramid()

Go(-150,0)
Stupa()

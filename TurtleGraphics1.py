import turtle
# tạo con rùa-s
# con rùa Tim RED
tim = turtle.Turtle()   # tạo một con rùa
tim.color('red')        # thiết lập màu        
tim.shape('turtle')     # hình  

# con rùa Ngân - PINK

Ngan = turtle.Turtle()
Ngan.color('purple')
Ngan.shape('turtle')

# con ruaf thuws 3
thu3 = turtle.Turtle()
thu3.color('gray')
thu3.shape('turtle')
#thu4 - mauf xanh
thu4 = turtle.Turtle()
thu4.color('green')
thu4.shape('turtle')
#thứ 5 màu xanh dương
thu5 = turtle.Turtle()
thu5.color('blue')
thu5.shape('turtle')

thu6 = turtle.Turtle()
thu6.color('orange')
thu6.shape('turtle')

thu7 = turtle.Turtle()
thu7.color('black')
thu7.shape('turtle')
# đưa các con rùa về vị trí
Ngan.penup()
Ngan.right(180)
Ngan.forward(300)
Ngan.left(90)
Ngan.forward(250)
Ngan.right(180)
Ngan.pendown()

tim.penup()
tim.right(180)
tim.forward(200)
tim.left(90)
tim.forward(250)
tim.right(180)
tim.pendown()

thu3.penup()
thu3.right(180)
thu3.forward(100)
thu3.left(90)
thu3.forward(250)
thu3.right(180)
thu3.pendown()

thu4.penup()
thu4.right(90)
thu4.forward(250)
thu4.right(180)
thu4.pendown()

thu5.penup()
thu5.forward(100)
thu5.right(90)
thu5.forward(250)
thu5.right(180)
thu5.pendown()

thu6.penup()
thu6.forward(200)
thu6.right(90)
thu6.forward(250)
thu6.right(180)
thu6.pendown()

thu7.penup()
thu7.forward(300)
thu7.right(90)
thu7.forward(250)
thu7.right(180)
thu7.pendown()

for x in range(1,23):
	Ngan.forward(x)
	tim.forward(x)
	thu3.forward(x)
	thu4.forward(x)
	thu5.forward(x)
	thu6.forward(x)
	thu7.forward(x)
for x in range(20,29):
	Ngan.forward(x)
	tim.forward(x)
	thu6.forward(x)
for x in range(29,32):
	Ngan.forward(x)

turtle.done()


import turtle

turtle.setup(1920,1080)

def draw_square():
	turtle.shape("square")
	turtle.color("cyan")
	window = turtle.Screen()
	window.bgcolor("lightcoral")
	brad = turtle.Turtle()
	brad.speed("fast")
	for j in range(1,74):	

		for i in range(1,5):
			brad.forward(100)
			brad.right(90)

		for i in range(1):
			brad.circle(200)

		brad.right(5)

	window.exitonclick()

draw_square()
import turtle

def draw_square(brad):
    for i in range(1,5):
        brad.forward(100)
        brad.right(90)

def draw_art():
        
    window=turtle.Screen()
    window.bgcolor("blue")

    #create the turtle brad - draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    draw_square(brad)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

    #create the turtle Angie - Draws a circle

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("black")
    #angie.circle(100)
    

    window.exitonclick()

draw_art()


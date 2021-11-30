import turtle

def circleF(bg, looping, number, array):
    
    turtle.bgcolor(bg)
    turtle.pensize(3)
    turtle.speed(0)

    for i in range(int(looping)):
        for colours in array:
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(10)

    totalShape = int(looping) * int(number)
    print ("There were a total of " + str(totalShape) + " circles drawn!")

    turtle.hideturtle()
    turtle.exitonclick()

def squareF(bg, looping, number, array):

    turtle.bgcolor(bg)
    turtle.speed(0)

    for i in range(int(looping)):
        for colours in array:
            turtle.color(colours)
            turtle.pensize(3)
            turtle.left(10)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)

    totalShape = int(looping) * int(number)
    print ("There were a total of " + str(totalShape) + " squares drawn!")

    turtle.hideturtle()
    turtle.exitonclick()

colourList = []
shapeChoice = input("Would you like to draw circles or square? (circle or square): ").lower()
backGround = input("What would you like the background colour to be?: ").lower()
loop = input("How many times do you want it to loop? (enter an integer): ")
num = input("How many colours do you want to use? ")

while len(colourList) < int(num):
        userChoice = input("Which colours would you like to use? ").lower()
        colourList.append(userChoice) 

if shapeChoice == "circle":
    circleF(backGround, loop, num, colourList)
elif shapeChoice == "square":
    squareF(backGround, loop, num, colourList)

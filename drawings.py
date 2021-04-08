import turtle
Draw=turtle.Turtle()
Draw.pensize(5)

#body​
Draw.penup()
Draw.goto(-70,-70)
Draw.pendown()
Draw.fillcolor("yellow")
Draw.begin_fill()
Draw.forward(200)
Draw.left(90)
Draw.forward(200)
Draw.left(90)
Draw.forward(200)
Draw.left(90)
Draw.forward(200)

Draw.end_fill()


#brownpants​
Draw.fillcolor("#8B4513")
Draw.begin_fill()
Draw.forward(40)
Draw.left(90)
Draw.forward(200)
Draw.left(90)
Draw.forward(40)
Draw.left(90)
Draw.forward(200)
Draw.left(90)
Draw.end_fill()


#shirts​
Draw.fillcolor("white")
Draw.begin_fill()
Draw.forward(20)
Draw.left(90)
Draw.forward(200)
Draw.left(90)
Draw.forward(20)
Draw.left(90)
Draw.forward(200)
Draw.end_fill()

Draw.penup()



#tie​
Draw.left(90)

Draw.forward(18)
Draw.left(90)
Draw.forward(100)
Draw.fillcolor("red")
Draw.begin_fill()
Draw.pencolor("red")
Draw.pendown()
Draw.circle(7)
Draw.end_fill()


Draw.penup()

#eye​
Draw.pencolor("black")
Draw.goto(75,50)
Draw.pendown()
Draw.fillcolor("white")
Draw.begin_fill()
Draw.circle(25)
Draw.end_fill()

Draw.fillcolor("black")
Draw.penup()
Draw.goto(80,60)
Draw.begin_fill()
Draw.circle(10)
Draw.end_fill()

#eye2​
Draw.penup()
Draw.pencolor("black")
Draw.goto(-15,50)
Draw.pendown()
Draw.fillcolor("white")
Draw.begin_fill()
Draw.circle(25)
Draw.end_fill()

Draw.penup()
Draw.goto(-10,60)
Draw.fillcolor("black")
Draw.begin_fill()
Draw.circle(10)
Draw.end_fill()


#smile​
Draw.penup()
Draw.goto(-10,0)
Draw.pendown()
Draw.pensize(5)
Draw.right(90)
Draw.fillcolor("red")
Draw.begin_fill()
Draw.circle(40,180)
Draw.left(90)
Draw.forward(80)
Draw.end_fill()


#teeths​
Draw.fillcolor("white")
Draw.begin_fill()
Draw.left(180)
Draw.forward(25)
Draw.right(90)
Draw.forward(15)
Draw.left(90)
Draw.forward(10)
Draw.left(90)
Draw.forward(15)
Draw.end_fill()


Draw.fillcolor("white")
Draw.begin_fill()
Draw.right(90)
Draw.forward(10)
Draw.right(90)
Draw.forward(15)
Draw.left(90)
Draw.forward(10)
Draw.left(90)
Draw.forward(15)
Draw.end_fill()




style = ('Courier', 50, 'italic')
Draw.penup()
Draw.pensize(5)
Draw.goto(-300,-300)
Draw.write("SpongeBob Squarepants ",font=style)



turtle.done()
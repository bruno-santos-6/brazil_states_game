import turtle

screen = turtle.Screen()
screen.title("Brazil's States Game")
image = "./conversion_png_gif/Brazil_Labelled_Map.gif"
screen.addshape(image)
turtle.shape(image)

screen.exitonclick()
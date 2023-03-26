from turtle import *

#configuracion de colores
title("Sunflower")
hideturtle()
pensize(3)
fillcolor("yellow")
#configuracion de colores


#lineas y figuras
begin_fill()

pencolor("green")
goto(0,0)
goto(50,50)
pencolor("yellow")
circle(30)
pencolor("yellow")
goto(50,70)
pencolor("brown")
circle(10)

pencolor("green")
goto(0,0)
goto(-50,50)
pencolor("yellow")
circle(30)
pencolor("yellow")

goto(-50,70)
pencolor("brown")
circle(10)

pencolor("green")
goto(0,0)
goto(25,100)
pencolor("yellow")

circle(30)
pencolor("yellow")

goto(25,120)
pencolor("brown")
circle(10)

pencolor("green")
goto(0,0)
goto(-25,100)
pencolor("yellow")

circle(30)
pencolor("yellow")

goto(-25,120)
pencolor("brown")
circle(10)

pencolor("green")
goto(0,0)
goto(95,90)
pencolor("yellow")

circle(30)
pencolor("yellow")

goto(95,110)
pencolor("brown")
circle(10)

pencolor("green")
goto(0,0)
goto(-95,90)
pencolor("yellow")

circle(30)
pencolor("yellow")

goto(-95, 110)
pencolor("brown")
circle(10)

pencolor("green")
goto(0,0)
pencolor("yellow")
goto(0,50)
pencolor("yellow")

circle(30)
pencolor("green")

goto(0,25)
pencolor("yellow")
goto(0,70)
pencolor("brown")
circle(10)
goto(0,0)
end_fill()

fillcolor("brown")
begin_fill()
pencolor("brown")
goto(0,25)
goto(-100,25)
goto(0,-100)
goto(100,25)
goto(0,25)
goto(-100,25)
end_fill()



#fin lineas y figuras

exitonclick()

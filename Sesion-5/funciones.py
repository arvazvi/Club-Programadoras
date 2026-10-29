import turtle
import random
import time

def nueva_pantalla(ancho, alto, color_fondo, titulo):
    pantalla = turtle.Screen()
    pantalla.setup(ancho, alto)
    pantalla.bgcolor(color_fondo)
    pantalla.title(titulo)
    pantalla.tracer(0)

    return pantalla

def dibujar_cielo(min_x, min_y, max_x, max_y, min_tamano, max_tamano, color="white", n_estrellas=80):
    lapiz = turtle.Turtle()
    lapiz.hideturtle()
    lapiz.penup()
    for i in range(80):
        lapiz.goto(random.randint(min_x, max_x), random.randint(min_y, max_y))
        lapiz.dot(random.randint(min_tamano, max_tamano), color)

def dibujar_pared(start_x, start_y, tamano, color_top, color_back):
    lapiz = turtle.Turtle()
    lapiz.hideturtle()
    lapiz.penup()
    lapiz.goto(start_x, start_y)
    lapiz.pendown()
    lapiz.pensize(tamano)
    lapiz.color(color_back)
    for lado in range(4):
        lapiz.forward(580)
        lapiz.left(90)
    lapiz.pensize(3)
    lapiz.color(color_top)
    for lado in range(4):
        lapiz.forward(580)
        lapiz.left(90)

def dibujar_marcador():
    marcador = turtle.Turtle()
    marcador.hideturtle()
    marcador.penup()
    marcador.goto(0, 305)
    marcador.color("white")
    marcador.write("REBOTES: 0", align="center", font=("Arial", 18, "bold"))

    return marcador

def nuevo_lapiz():
    lapiz = turtle.Turtle()
    lapiz.hideturtle()
    lapiz.penup()
    return lapiz

def dibujar_chispas(lapiz, centro_x, centro_y, paso, color, n_rayos=12, distancia=4, gravedad=0.15, tamano=12):
    # Dibuja un círculo de chispas que se alejan del centro, caen y se achican según el paso
    for rayo in range(n_rayos):
        lapiz.goto(centro_x, centro_y)
        lapiz.setheading(rayo * 360 / n_rayos)
        lapiz.forward(paso * distancia)
        lapiz.sety(lapiz.ycor() - paso * paso * gravedad)   # gravedad
        lapiz.dot(tamano - paso // 2, color)

def nueva_pelota(color, tamano):
    pelota = turtle.Turtle()
    pelota.shape("circle")
    pelota.color(color)
    pelota.pensize(tamano)
    pelota.setheading(random.randint(0, 360))

    return pelota

def dibujar_fuegos_artificiales(pantalla, lapiz, colores, n_fuegos=6):
    # Lanza varios fuegos artificiales en posiciones y colores al azar
    for fuego in range(n_fuegos):
        centro_x = random.randint(-200, 200)
        centro_y = random.randint(-100, 200)
        color_fuego = random.choice(colores)
        for paso in range(1, 25):
            lapiz.clear()
            dibujar_chispas(lapiz, centro_x, centro_y, paso, color_fuego,
                            n_rayos=18, distancia=6, gravedad=0.2, tamano=14)
            pantalla.update()
            time.sleep(0.02)
    lapiz.clear()

def dibujar_mensaje_final(pantalla, rebotes):
    # Mensaje final con sombra de color
    texto = nuevo_lapiz()
    texto.goto(3, -3)
    texto.color("magenta")
    texto.write("¡JUEGO TERMINADO!", align="center", font=("Arial", 34, "bold"))
    texto.goto(0, 0)
    texto.color("white")
    texto.write("¡JUEGO TERMINADO!", align="center", font=("Arial", 34, "bold"))
    texto.goto(0, -45)
    texto.color("cyan")
    texto.write("Total de rebotes: " + str(rebotes), align="center", font=("Arial", 18, "bold"))
    pantalla.update()

    return texto
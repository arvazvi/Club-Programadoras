import random
import time

import functions as f
import turtle

colores = ["red", "cyan", "magenta", "yellow", "lime", "orange", "deepskyblue"]

pantalla = f.nueva_pantalla(700, 700, "black", "Pinball Neon")
f.dibujar_cielo(-340, -340, 340, 340, 1, 3)
f.dibujar_pared(-290, -290, 10, "navy", "deepskyblue")

# Marcador
marcador = f.dibujar_marcador()
chispas = f.nuevo_lapiz()

# # Lapiz que dibuja las chispas de cada choque
chispas = f.nuevo_lapiz()

chispas.clear()
explosion_x = 0
explosion_y = 0
explosion_color = "white"
explosion_paso = 0

# while True:
#     if explosion_paso < 100:
#         explosion_paso = explosion_paso + 1
#         f.dibujar_chispas(chispas, explosion_x, explosion_y, explosion_paso, explosion_color)
#         pantalla.update()
#         time.sleep(0.01)
#     else:
#         chispas.clear()
#         break


# ---------- La pelota ----------
pelota = f.nueva_pelota("blue", 3)

# Fase 3: preparar el contador de rebotes
rebotes = 0
velocidad = 6
tamano = 1

# # ---------- Bucle infinito ----------
while True:
    pelota.forward(velocidad)

    x = pelota.xcor()
    y = pelota.ycor()

    # Detección de impacto en los bordes
    if x > 280 or x < -280 or y > 280 or y < -280:
        # Fase 1: ángulo de rebote impredecible
        # (apunta hacia el centro y le suma un giro al azar)
        pelota.setheading(pelota.towards(0, 0) + random.randint(-30, 30))

        # Fase 2: personalización visual reactiva
        color_nuevo = random.choice(colores)
        pelota.color(color_nuevo)
        tamano = 2.5            # La pelota "late" al chocar
        velocidad = velocidad + 1

        # Empieza una explosión nueva justo donde chocó
        explosion_x = x
        explosion_y = y
        explosion_color = color_nuevo
        explosion_paso = 0

        # Fase 3: sumar al contador
        rebotes = rebotes + 1
        marcador.clear()
        marcador.write("REBOTES: " + str(rebotes), align="center", font=("Arial", 18, "bold"))

        # Condición para terminar el juego usando break
        if rebotes == 10:
            break

    # La pelota vuelve poco a poco a su tamaño normal
    if tamano > 1:
        tamano = tamano - 0.1
    pelota.shapesize(tamano)

    # Animar las chispas: cada vuelta se alejan, caen y se hacen más pequeñas
    chispas.clear()
    if explosion_paso < 20:
        explosion_paso = explosion_paso + 1
        f.dibujar_chispas(chispas, explosion_x, explosion_y, explosion_paso, explosion_color)

    pantalla.update()
    time.sleep(0.01)

# ---------- Final: fuegos artificiales ----------
pelota.hideturtle()
f.dibujar_fuegos_artificiales(pantalla, chispas, colores)

# # Mensaje final con sombra de color
# funciones.dibujar_mensaje_final(pantalla, rebotes)

turtle.done()

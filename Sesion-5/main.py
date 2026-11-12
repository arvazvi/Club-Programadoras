import random
import time
import turtle
 
import funciones as f
 
colores = ["red", "cyan", "magenta", "yellow", "lime", "orange", "deepskyblue"]
max_rebotes = 20     # Si llegamos a este número de rebotes, ganamos (NUEVO: antes 10)
 
pantalla = f.nueva_pantalla(700, 700, "black", "Pinball Neon")
 
 
def jugar():
    # ---------- El escenario ----------
    f.dibujar_cielo(-340, -340, 340, 340, 1, 3)
    f.dibujar_pared(-290, -290, 10, "navy", "deepskyblue")
    marcador = f.dibujar_marcador()
 
    # Lápiz que dibuja las chispas de cada choque
    chispas = f.nuevo_lapiz()
    explosion_x = 0
    explosion_y = 0
    explosion_color = "white"
    explosion_paso = 20     # 20 = no hay explosión al empezar
 
    # ---------- Las pelotas (NUEVO: una lista) ----------
    pelotas = []                          # lista vacía
    primera = f.nueva_pelota("blue", 3)
    pelotas.append(primera)               # la guardamos en la lista
    max_pelotas = 5                       # cuántas pelotas puede haber como máximo
    rebotes = 0
    velocidad = 6
    tamano = 1
 
    # ---------- El jugador ----------
    jugador = f.nuevo_jugador("white", 0, -220)
    f.activar_teclas(pantalla, jugador)
 
    # Si la pelota nos toca, cambia a False
    gano = True
    jugando = True       # NUEVO: break solo saldría del for, así que usamos esta variable
 
    # ---------- Bucle del juego ----------
    while jugando:
        # NUEVO: repetir todo para CADA pelota de la lista
        for pelota in pelotas:
            pelota.forward(velocidad)
 
            # Si la pelota toca al jugador, perdemos
            if pelota.distance(jugador) < 20:
                gano = False
                jugando = False
 
            x = pelota.xcor()
            y = pelota.ycor()
 
            # Detección de impacto en los bordes
            if x > 280 or x < -280 or y > 280 or y < -280:
                # Ángulo de rebote: hacia el centro más un giro al azar
                pelota.setheading(pelota.towards(0, 0) + random.randint(-30, 30))
 
                # Color nuevo, la pelota "late" y acelera
                color_nuevo = random.choice(colores)
                pelota.color(color_nuevo)
                tamano = 2.5
                velocidad = velocidad + 0.5     # NUEVO: sube más despacio porque hay más pelotas
 
                # Empieza una explosión nueva justo donde chocó
                explosion_x = x
                explosion_y = y
                explosion_color = color_nuevo
                explosion_paso = 0
 
                # Sumar al contador
                rebotes = rebotes + 1
                f.actualizar_marcador(marcador, rebotes, pelotas)   # NUEVO (paso 4)
 
                # Llegamos a la meta: termina el juego
                if rebotes == max_rebotes:
                    jugando = False
 
            # La pelota vuelve poco a poco a su tamaño normal
            if tamano > 1:
                tamano = tamano - 0.1
            pelota.shapesize(tamano)
 
        # NUEVO: cada 4 rebotes entra una pelota más (hasta max_pelotas)
        if rebotes >= len(pelotas) * 4 and len(pelotas) < max_pelotas:
            nueva = f.nueva_pelota(random.choice(colores), 3)
            pelotas.append(nueva)
            f.actualizar_marcador(marcador, rebotes, pelotas)   # NUEVO (paso 4)

        # Animar las chispas
        chispas.clear()
        if explosion_paso < 20:
            explosion_paso = explosion_paso + 1
            f.dibujar_chispas(chispas, explosion_x, explosion_y, explosion_paso, explosion_color)
 
        pantalla.update()
        time.sleep(0.01)
 
    # ---------- Final ----------
    f.esconder_todas(pelotas)     # NUEVO (paso 4): una función que recibe la lista
    chispas.clear()
    if gano:
        # Sobrevivimos: fuegos artificiales
        f.dibujar_fuegos_artificiales(pantalla, chispas, colores)
    # Gane o pierda: mensaje final con sombra de color
    f.dibujar_mensaje_final(pantalla, rebotes)
 
 
# ---------- Repetir el juego cada vez que presionen Enter ----------
while True:
    jugar()
    f.dibujar_mensaje_reiniciar(pantalla)
    f.esperar_enter(pantalla)
 
    # Borramos todo y preparamos la pantalla para la siguiente partida
    pantalla.clear()
    pantalla = f.nueva_pantalla(700, 700, "black", "Pinball Neon")
 

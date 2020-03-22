
import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

def dibujar_fondo():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.ARYLIDE_YELLOW)


class Dibujos:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def dibujo_personaje(self):
        arcade.draw_rectangle_filled(self.position_x + 100, self.position_y, 4, 40, arcade.csscolor.BLACK)  # torso
        arcade.draw_circle_filled(self.position_x + 100, self.position_y + 20, 15, arcade.csscolor.SIENNA)  # cara
        arcade.draw_circle_filled(self.position_x + 95, self.position_y + 25, 2.5, arcade.csscolor.BLACK)  # ojo
        arcade.draw_circle_filled(self.position_x + 110, self.position_y + 25, 2.5, arcade.csscolor.BLACK)  # ojo
        arcade.draw_line(self.position_x + 100, self.position_y - 5, self.position_x + 125, self.position_y - 5,
                         arcade.color.BLACK, 3)
        arcade.draw_line(self.position_x + 100, self.position_y - 5, self.position_x + 75, self.position_y - 5,
                         arcade.color.BLACK, 3)
        arcade.draw_line(self.position_x + 100, self.position_y - 20, self.position_x + 110, self.position_y - 60,
                         arcade.color.BLACK, 3)
        arcade.draw_line(self.position_x + 100, self.position_y - 20, self.position_x + 90, self.position_y - 60,
                         arcade.color.BLACK, 3)

    def dibujo_camello(self):
        arcade.draw_line(self.position_x + 10, 235, self.position_x + 30, 215, arcade.color.BLACK, 4)
        arcade.draw_line(self.position_x - 10, 235, self.position_x - 30, 215, arcade.color.BLACK, 4)
        arcade.draw_ellipse_filled(self.position_x, 250, 70, 40, arcade.csscolor.SANDY_BROWN)  # cuerpo
        arcade.draw_circle_filled(self.position_x + 30, 270, 15, arcade.csscolor.SANDY_BROWN)  # cabeza
        arcade.draw_circle_filled(self.position_x + 25, 280, 2, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(self.position_x + 40, 280, 2, arcade.csscolor.BLACK)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color(arcade.color.BLUE)

        self.jugador = Dibujos(250, 270)
        self.enemigo1 = Dibujos(-20, 280)
        self.enemigo2 = Dibujos(0, 260)
        self.enemigo3 = Dibujos(-50, 240)
        self.camello = Dibujos(260, 290)

    def on_draw(self):
        arcade.start_render()
        dibujar_fondo()
        self.jugador.dibujo_personaje()
        self.camello.dibujo_camello()
        self.enemigo1.dibujo_personaje()
        self.enemigo2.dibujo_personaje()
        self.enemigo3.dibujo_personaje()


    def movimiento_jugador(self, distancia):
        self.jugador.position_x += distancia
        self.camello.position_x += distancia

    def movimiento_enemigo(self, distancia):
        self.enemigo1.position_x += distancia
        self.enemigo2.position_x += distancia
        self.enemigo3.position_x += distancia

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            print("Retrocedemoooooos!!!!")
            self.jugador.position_x -= 10
            self.camello.position_x -= 10
        elif key == arcade.key.RIGHT:
            print("avanzamoooooss!!!!")
            self.jugador.position_x += 10
            self.camello.position_x += 10


def main():
    window = MyGame()
    arcade.run()


main()
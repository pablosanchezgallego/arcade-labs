import arcade
import random

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720


def dibujar_fondo():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.ARYLIDE_YELLOW)


def dibujo_camello(x, y):
    """ Dibujo camello """
    arcade.draw_line(x + 10, 235, x + 30, 215, arcade.color.BLACK, 4)
    arcade.draw_line(x - 10, 235, x - 30, 215, arcade.color.BLACK, 4)
    arcade.draw_ellipse_filled(x, 250, 70, 40, arcade.csscolor.SANDY_BROWN) # cuerpo
    arcade.draw_circle_filled(x + 30, 270, 15, arcade.csscolor.SANDY_BROWN) # cabeza
    arcade.draw_circle_filled(x + 25, 280, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x + 40, 280, 2, arcade.csscolor.BLACK)

def dibujo_personaje(x, y):

    arcade.draw_rectangle_filled(x + 100, y, 4, 40, arcade.csscolor.BLACK) # torso
    arcade.draw_circle_filled(x + 100, y + 20, 15, arcade.csscolor.SIENNA) # cara
    arcade.draw_circle_filled(x + 95, y + 25, 2.5, arcade.csscolor.BLACK) # ojo
    arcade.draw_circle_filled(x + 110, y + 25, 2.5, arcade.csscolor.BLACK) # ojo
    arcade.draw_line(x + 100, y - 5, x + 125, y - 5, arcade.color.BLACK, 3)
    arcade.draw_line(x + 100, y - 5, x + 75, y - 5, arcade.color.BLACK, 3)
    arcade.draw_line(x + 100, y - 20, x + 110, y - 60, arcade.color.BLACK, 3)
    arcade.draw_line(x + 100, y - 20, x + 90, y - 60, arcade.color.BLACK, 3)




def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    dibujar_fondo()
    dibujo_camello(on_draw.jugadorx, on_draw.jugadory)
    dibujo_personaje(on_draw.jugadorx, on_draw.jugadory)
    dibujo_personaje(on_draw.enemigox - 30, on_draw.enemigoy + 20)
    dibujo_personaje(on_draw.enemigox, on_draw.enemigoy)
    ###

# Create a value that our on_draw.snow_person1_x will start at.
on_draw.jugadorx = 250
on_draw.jugadory = 270
on_draw.enemigox = -20
on_draw.enemigoy = 260


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()
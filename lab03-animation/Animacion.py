import arcade
def dibujar_demas():
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
    arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)
    arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)
    arcade.draw_ellipse_filled(300, 150, 210, 90, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_ellipse_filled(300, 150, 200, 80, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(75, 540, 40, arcade.csscolor.YELLOW)
    arcade.draw_circle_filled(500, 200, 30, arcade.csscolor.BLUE)
    arcade.draw_line(470, 200, 530, 200, arcade.color.BLACK, 3)
    arcade.draw_line(500, 170, 500, 230, arcade.color.BLACK, 3)
    arcade.draw_text("Las segundas matrículas\ncuestan más pasta",
                 160, 500,
                 arcade.color.BLACK, 24)

# Inicio de personaje
def dibujar_persona(x, y):
    arcade.draw_rectangle_filled(x, 160, 10, 60, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x, 200, 30, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(x - 10, 208, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x + 10, 208, 5, arcade.csscolor.BLACK)
    arcade.draw_line(x, 160, x + 50, 160, arcade.color.BLACK, 8)
    arcade.draw_line(x, 160, x - 50, 160, arcade.color.BLACK, 8)
    arcade.draw_line(x, 135, x + 20, 80, arcade.color.BLACK, 8)
    arcade.draw_line(x, 135, x - 20, 80, arcade.color.BLACK, 8)
    # Final de personaje




def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    dibujar_demas()
    dibujar_persona(on_draw.persona_x, 140)
    on_draw.persona_x += 1
    if on_draw.persona_x >= 400:
        while on_draw.persona_x > 100:
            on_draw.persona_x -= 1


on_draw.persona_x = 100


def main():
    arcade.open_window(600, 600, "Dibujar con funciones")
    arcade.set_background_color(arcade.color.SKY_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()
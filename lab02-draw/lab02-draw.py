import arcade
arcade.open_window(600, 600, "Hola")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
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
# Inicio de personaje
arcade.draw_rectangle_filled(100, 160, 10, 60, arcade.csscolor.BLACK)
arcade.draw_circle_filled(100, 200, 30, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(90, 208, 5, arcade.csscolor.BLACK)
arcade.draw_circle_filled(110, 208, 5, arcade.csscolor.BLACK)
arcade.draw_line(100, 160, 150, 160, arcade.color.BLACK, 8)
arcade.draw_line(100, 160, 50, 160, arcade.color.BLACK, 8)
arcade.draw_line(100, 135, 120, 80, arcade.color.BLACK, 8)
arcade.draw_line(100, 135, 80, 80, arcade.color.BLACK, 8)
# Final de personaje
arcade.draw_circle_filled(500, 200, 30, arcade.csscolor.BLUE)
arcade.draw_line(470, 200, 530, 200, arcade.color.BLACK, 3)
arcade.draw_line(500, 170, 500, 230, arcade.color.BLACK, 3)


arcade.draw_text("Las segundas matrículas\ncuestan más pasta",
                 160, 500,
                 arcade.color.BLACK, 24)

arcade.finish_render()
arcade.run()
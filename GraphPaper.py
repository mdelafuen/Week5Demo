import arcade

def draw_lines():
    arcade.open_window(800, 800, "lines Demo")
    arcade.set_background_color(arcade.color.FAWN)
    width = arcade.get_window().width
    height = arcade.get_window().height

    arcade.start_render()
    #drawings here
    for location in range(80, width, 80):
        arcade.draw_line(location, 0, location, height, arcade.color.BLACK, 2)
    for horizontal_location in range(80, height, 80):
        arcade.draw_line(0, horizontal_location, width, horizontal_location, arcade.color.BLACK, 2)



    arcade.finish_render()


    arcade.run()



draw_lines()
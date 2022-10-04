my_file=open("nationsPop.txt", "r")
all_lines = my_file.readlines()
for line in all_lines:
    print(line)

import arcade
my_window =arcade.open_window(1000, 900, "Bar Graph")

arcade.set_background_color(arcade.color.BEIGE)
my_text =arcade.Text("Populations of the Largest Pop Countries", 350, 850, arcade.color.BLACK, 18)


arcade.start_render()
my_text.draw()
arcade.finish_render()
arcade.run()

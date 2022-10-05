my_file=open("nationsPop.txt", "r")
all_lines = my_file.readlines()
for line in all_lines:
    print(line)

import arcade
my_window =arcade.open_window(1000, 900, "Bar Graph")

arcade.set_background_color(arcade.color.BEIGE)
my_title =arcade.Text("Populations of the Largest Pop Countries", 350, 850, arcade.color.BLACK, 18)

arcade.start_render()

arcade.draw_line(175,250,970,250, arcade.color.BLACK,3)
arcade.draw_line(175,250,175,850, arcade.color.BLACK,3)
#created my y and x axis above

china=arcade.Text("China", 190, 220, arcade.color.BLACK, 10)
india=arcade.Text("India", 245, 220, arcade.color.BLACK, 10)
USA=arcade.Text("USA",300, 220, arcade.color.BLACK, 10)
indonesia=arcade.Text("Indonesia", 355,220, arcade.color.BLACK, 10)
pakistan=arcade.Text("Pakistan", 430, 220, arcade.color.BLACK, 10)
nigeria=arcade.Text("Nigeria", 490, 220, arcade.color.BLACK, 10)
brazil=arcade.Text("Brazil", 540, 220, arcade.color.BLACK, 10)
bangladesh=arcade.Text("Bangladesh", 580, 220, arcade.color.BLACK, 10)
russia=arcade.Text("Russia", 660, 220, arcade.color.BLACK, 10)
mexico=arcade.Text("Mexico", 710, 220, arcade.color.BLACK, 10)
japan=arcade.Text("Japan", 760, 220, arcade.color.BLACK, 10)
ethipoia=arcade.Text("Ethiopia", 805, 220, arcade.color.BLACK, 10)
philippines=arcade.Text("Philippines", 860, 220, arcade.color.BLACK, 10)
egypt=arcade.Text("Egypt", 930, 220, arcade.color.BLACK, 10)
#above is labelling the x-axis

first=arcade.Text("100M", 135, 255, arcade.color.BLACK, 10)
second=arcade.Text("200M", 135, 315, arcade.color.BLACK, 10)
third=arcade.Text("300M", 135, 375, arcade.color.BLACK, 10)
fourth=arcade.Text("400M", 135, 435, arcade.color.BLACK, 10)
fifth=arcade.Text("500M", 135, 495, arcade.color.BLACK,10)
sixth=arcade.Text("600M", 135, 555, arcade.color.BLACK, 10 )
seventh=arcade.Text("700M", 135, 615, arcade.color.BLACK, 10)
eighth=arcade.Text("800M", 135, 675, arcade.color.BLACK, 10)
nineth=arcade.Text("900M", 135, 735, arcade.color.BLACK, 10)
tenth=arcade.Text("1B", 150, 795, arcade.color.BLACK, 10)
eleventh=arcade.Text("2B", 150, 850, arcade.color.BLACK, 10)
#above is the labels for y-axis


my_title.draw()
china.draw()
india.draw()
USA.draw()
indonesia.draw()
pakistan.draw()
nigeria.draw()
brazil.draw()
bangladesh.draw()
russia.draw()
mexico.draw()
japan.draw()
ethipoia.draw()
philippines.draw()
egypt.draw()
#must do above to make the labels on the x-axis appear

first.draw()
second.draw()
third.draw()
fourth.draw()
fifth.draw()
sixth.draw()
seventh.draw()
eighth.draw()
nineth.draw()
tenth.draw()
eleventh.draw()
#must do above to make the labels on the y-axis appear

arcade.finish_render()
arcade.run()

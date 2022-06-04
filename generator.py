import os
import configparser
import random

current_path = os.path.abspath(os.getcwd())
maps_folder_directory = os.path.join(current_path, "maps files")

config = configparser.ConfigParser()
config.read_file(open('settings.txt'))
map_width = config.get('Settings', 'mapwidth')
map_height = config.get('Settings', 'mapheight')
number_of_map_to_generate = config.get('Settings', 'numberofmapstogenerate')
last_line_id = config.get('Settings', 'lastlineid')
percentage_of_empty_space = config.get('Settings', 'percentageofemptyspace')

map_line_id = int(last_line_id)

loop_number = 0
loop_number2 = 0
loop_number3 = 0

if int(percentage_of_empty_space) <= 15:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 22:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 27:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 33:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 36:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 40:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 43:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".","a", "b"]
elif int(percentage_of_empty_space) <= 47:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".", ".","a", "b"]
elif int(percentage_of_empty_space) <= 49:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".", ".", ".","a", "b"]
elif int(percentage_of_empty_space) >= 50:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".","a", "b"]


if not os.path.exists(maps_folder_directory):
    os.mkdir(maps_folder_directory)

while loop_number <= int(number_of_map_to_generate)-1:
    if map_width == "3v3":
        map_width = 22
        print("detected 3v3 width")
    if map_height == "3v3":
        map_height = 33
        print("detected 3v3 height")
    if map_height == "showdown":
        print("detected showdown height")
        map_height = 60
    if map_width == "showdpwn":
        print("detected showdown width")
        map_width = 60
    map_width = int(map_width)
    map_height = int(map_height)
    loop_number = loop_number + 1
    map1 = open(os.path.join(maps_folder_directory + "/map" + str(random.randint(10000, 99999)) + ".txt"), 'a+')
    i = map1.name.index("/m")
    i2 = map1.name[i+1:]
    i3 = i2.index(".t")
    map_name = str(i2[:i3])
    print(map_name)
    map_line_id = map_line_id + 1
    map1.write("\n" + str(map_line_id) + "," + map_name + ",")
    while loop_number3 < int(map_width) + 2:
        loop_number3 = loop_number3 + 1
        random_tile = random.choice(tile_list)
        map1.write(random_tile)
        if loop_number3 == int(map_width):
            loop_number3 = 0
            break
    map1.write(",")
    while loop_number2 <= int(map_height)+2:
        loop_number2 = loop_number2+1
        map_line_id = map_line_id + 1
        map1.write("\n"+str(map_line_id) + ",,")
        while loop_number3 < int(map_width)+2:
            loop_number3 = loop_number3+1
            random_tile = random.choice(tile_list)
            map1.write(random_tile)
            if loop_number3 == int(map_width):
                loop_number3 = 0
                break
        map1.write(",")
        if loop_number2 == int(map_height)-1:
            map_line_id = int(last_line_id)
            loop_number2 = 0
            break
    map1.close()
print("Maps Generated")

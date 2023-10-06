import os
import configparser
import random
import csv

current_path = os.path.abspath(os.getcwd())
maps_folder_directory = os.path.join(current_path, "maps files")

config = configparser.ConfigParser()
config.read_file(open('settings.txt'))
map_width = config.get('Settings', 'map_width')
map_height = config.get('Settings', 'map_height')
number_of_map_to_generate = int(config.get('Settings', 'number_of_maps_to_generate'))
last_line_id = config.get('Settings', 'last_line_id')
percentage_of_empty_space = int(config.get('Settings', 'percentage_of_empty_space'))
are_spawn_points_3v3_or_showdown = config.get('Settings', 'are_spawn_points_3v3_or_showdown')
number_of_spawn_points = 0
if are_spawn_points_3v3_or_showdown == "showdown":
    number_of_spawn_points = 10
elif are_spawn_points_3v3_or_showdown == "3v3":
    number_of_spawn_points = 10
else:
    exit(print("are_spawn_points_3v3_or_showdown doesn't have a correct value"))
modify_csv_directly = config.get('Settings', 'modify_csv_directly')
if modify_csv_directly == "true":
    if number_of_map_to_generate > 3:
        exit(print("exceeded number of map to generate while modify_csv_directly is true"))
    elif number_of_map_to_generate == 1:
        gamemode_of_map_1 = config.get('Settings', 'gamemode_of_map_1')
    elif number_of_map_to_generate == 2:
        gamemode_of_map_1 = config.get('Settings', 'gamemode_of_map_1')
        gamemode_of_map_2 = config.get('Settings', 'gamemode_of_map_2')
    elif number_of_map_to_generate == 3:
        gamemode_of_map_1 = config.get('Settings', 'gamemode_of_map_1')
        gamemode_of_map_2 = config.get('Settings', 'gamemode_of_map_2')
        gamemode_of_map_3 = config.get('Settings', 'gamemode_of_map_3')

map_line_id = int(last_line_id)
maps_generated = 1
rows_generated = 0
tiles_generated = 0
generated_showdown_spawn_points = 0
map_gamemode = ""

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
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 47:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) <= 49:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".", ".", ".", "a", "b"]
elif int(percentage_of_empty_space) >= 50:
    tile_list = ["M", "X", "C", "Y", "D", "F", "W", "N", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "a", "b"]


if not os.path.exists(maps_folder_directory):
    os.mkdir(maps_folder_directory)

while maps_generated <= int(number_of_map_to_generate):
    if generated_showdown_spawn_points == 10:
        generated_showdown_spawn_points = 0
    if map_width == "3v3":
        map_width = 22
        print("detected 3v3 width")
    if map_height == "3v3":
        map_height = 33
        print("detected 3v3 height")
    if map_height == "showdown":
        print("detected showdown height")
        map_height = 60
    if map_width == "showdown":
        print("detected showdown width")
        map_width = 60
    map_width = int(map_width)
    map_height = int(map_height)

    if modify_csv_directly == "false":
        map1 = open(os.path.join(maps_folder_directory + "/map" + str(random.randint(10000, 99999)) + ".txt"), 'a+')
        i = map1.name.index("/m")
        i2 = map1.name[i+1:]
        i3 = i2.index(".t")
        map_name = str(i2[:i3])
        print(map_name)
        map_line_id = map_line_id + 1
        #generates the first line with map name
        map1.write(str(map_line_id) + "," + map_name + ",")
        while tiles_generated <= int(map_width):
            tiles_generated = tiles_generated + 1
            if are_spawn_points_3v3_or_showdown == "3v3":
                if map_width//4 == tiles_generated:
                    map1.write("2")
                if map_width//2 == tiles_generated:
                    map1.write("2")
                if map_width//(4/3) == tiles_generated:
                    map1.write("2")
                else:
                    random_tile = random.choice(tile_list)
                    map1.write(random_tile)
            else:
                random_tile = random.choice(tile_list)
                map1.write(random_tile)
            if tiles_generated == int(map_width):
                tiles_generated = 0
                break
        map1.write(",")
        while rows_generated <= int(map_height)+2:
            rows_generated = rows_generated+1
            map_line_id = map_line_id + 1
            map1.write("\n"+str(map_line_id) + ",,")
            if are_spawn_points_3v3_or_showdown == "showdown":
                if generated_showdown_spawn_points < 10:
                    map1.write("1")
                    tiles_generated = tiles_generated + 1
                    generated_showdown_spawn_points = generated_showdown_spawn_points + 1
            while tiles_generated <= int(map_width):
                tiles_generated = tiles_generated+1
                if are_spawn_points_3v3_or_showdown == "3v3":
                    if rows_generated == map_height-2:
                        if map_width // 4 == tiles_generated:
                            map1.write("1")
                        if map_width // 2 == tiles_generated:
                            map1.write("1")
                        if map_width // (4 / 3) == tiles_generated:
                            map1.write("1")
                        else:
                            random_tile = random.choice(tile_list)
                            map1.write(random_tile)
                    else:
                        random_tile = random.choice(tile_list)
                        map1.write(random_tile)
                else:
                    random_tile = random.choice(tile_list)
                    map1.write(random_tile)
                if tiles_generated == int(map_width):
                    tiles_generated = 0
                    break
            map1.write(",")
            if rows_generated == int(map_height)-1:
                rows_generated = 0
                break
        map1.close()
    elif modify_csv_directly == "true":
        if maps_generated == 1:
            map_name = gamemode_of_map_1 + str(random.randint(10000, 99999))
            if gamemode_of_map_1 == "lonestar":
                map_gamemode = "SoloBounty"
            elif gamemode_of_map_1 == "showdown":
                map_gamemode = "BattleRoyale"
            elif gamemode_of_map_1 == "gemgrab":
                map_gamemode = "CoinRush"
            elif gamemode_of_map_1 == "heist":
                map_gamemode = "AttackDefend"
            elif gamemode_of_map_1 == "bounty":
                map_gamemode = "BountyHunter"
            elif gamemode_of_map_1 == "brawlball":
                map_gamemode = "LaserBall"
        elif maps_generated == 2:
            map_name = gamemode_of_map_2 + str(random.randint(10000, 99999))
            if gamemode_of_map_2 == "lonestar":
                map_gamemode = "SoloBounty"
            elif gamemode_of_map_2 == "showdown":
                map_gamemode = "BattleRoyale"
            elif gamemode_of_map_2 == "gemgrab":
                map_gamemode = "CoinRush"
            elif gamemode_of_map_2 == "heist":
                map_gamemode = "AttackDefend"
            elif gamemode_of_map_2 == "bounty":
                map_gamemode = "BountyHunter"
            elif gamemode_of_map_2 == "brawlball":
                map_gamemode = "LaserBall"
        elif maps_generated == 3:
            map_name = gamemode_of_map_3 + str(random.randint(10000, 99999))
            if gamemode_of_map_2 == "lonestar":
                map_gamemode = "SoloBounty"
            elif gamemode_of_map_2 == "showdown":
                map_gamemode = "BattleRoyale"
            elif gamemode_of_map_2 == "gemgrab":
                map_gamemode = "CoinRush"
            elif gamemode_of_map_2 == "heist":
                map_gamemode = "AttackDefend"
            elif gamemode_of_map_2 == "bounty":
                map_gamemode = "BountyHunter"
            elif gamemode_of_map_2 == "brawlball":
                map_gamemode = "LaserBall"
        map1 = open(os.path.join(current_path + "/maps.csv"), 'a+')
        print(map_name)
        map_line_id = map_line_id + 1
        #generates the first line with map name
        map1.write("\n"+str(map_line_id) + "," + map_name + ",")
        while tiles_generated <= int(map_width):
            tiles_generated = tiles_generated + 1
            if are_spawn_points_3v3_or_showdown == "3v3":
                if map_width//4 == tiles_generated:
                    map1.write("1")
                if map_width//2 == tiles_generated:
                    map1.write("1")
                if map_width//(4/3) == tiles_generated:
                    map1.write("1")
                else:
                    random_tile = random.choice(tile_list)
                    map1.write(random_tile)
            else:
                random_tile = random.choice(tile_list)
                map1.write(random_tile)
            if tiles_generated == int(map_width):
                tiles_generated = 0
                break
        map1.write(",")
        while rows_generated <= int(map_height)+2:
            rows_generated = rows_generated+1
            map_line_id = map_line_id + 1
            map1.write("\n"+str(map_line_id) + ",,")
            if are_spawn_points_3v3_or_showdown == "showdown":
                if generated_showdown_spawn_points < 10:
                    map1.write("1")
                    tiles_generated = tiles_generated + 1
                    generated_showdown_spawn_points = generated_showdown_spawn_points + 1
            while tiles_generated <= int(map_width):
                tiles_generated = tiles_generated+1
                if are_spawn_points_3v3_or_showdown == "3v3":
                    if rows_generated == map_height-2:
                        if map_width // 4 == tiles_generated:
                            map1.write("2")
                        if map_width // 2 == tiles_generated:
                            map1.write("2")
                        if map_width // (4 / 3) == tiles_generated:
                            map1.write("2")
                        else:
                            random_tile = random.choice(tile_list)
                            map1.write(random_tile)
                    else:
                        random_tile = random.choice(tile_list)
                        map1.write(random_tile)
                else:
                    random_tile = random.choice(tile_list)
                    map1.write(random_tile)
                if tiles_generated == int(map_width):
                    tiles_generated = 0
                    break
            map1.write(",")
            if rows_generated == int(map_height)-1:
                rows_generated = 0
                break
        map1.close()
    maps_generated = maps_generated + 1
print("Maps Generated")

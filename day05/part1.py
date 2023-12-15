import os


def map_values(file, source_dict, dest_dict):
    for line in file:
        if line == "\n":
            break
        dest, source, rangelen = line.split(" ")
        for i in source_dict:
            if i in range(int(source), int(source) + int(rangelen)):
                mapped_dest = int(dest) + (source_dict[i] - int(source))
                source_dict[i] = mapped_dest
                dest_dict[mapped_dest] = mapped_dest
    for value in source_dict.values():
        if value not in dest_dict:
            dest_dict[value] = value
    file.readline()


def main():
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")

    # Seeds
    seeds_dict = {}
    seeds = f.readline()
    curr_seed = 0
    for seed in seeds:
        if seed.isdigit():
            curr_seed = (curr_seed * 10) + int(seed)
        elif not seed.isdigit() and curr_seed != 0:
            seeds_dict[curr_seed] = curr_seed
            curr_seed = 0

    f.readline()
    f.readline()

    # Seed-To-Soil
    soil_dict = {}
    map_values(f, seeds_dict, soil_dict)

    # Soil-To-Fertilizer
    fertilizer_dict = {}
    map_values(f, soil_dict, fertilizer_dict)

    # Fertilizer-To-Water
    water_dict = {}
    map_values(f, fertilizer_dict, water_dict)

    # Water-To-Light
    light_dict = {}
    map_values(f, water_dict, light_dict)

    # Light-To-Temperature
    temp_dict = {}
    map_values(f, light_dict, temp_dict)

    # Temperature-To-Humidity
    humidity_dict = {}
    map_values(f, temp_dict, humidity_dict)

    # Humidity-To-Location
    location_dict = {}
    map_values(f, humidity_dict, location_dict)

    final_locations = []
    for i in seeds_dict:
        soil = seeds_dict[i]
        fertilizer = soil_dict.get(soil, soil)
        water = fertilizer_dict.get(fertilizer, fertilizer)
        light = water_dict.get(water, water)
        temp = light_dict.get(light, light)
        humidity = temp_dict.get(temp, temp)
        location = humidity_dict.get(humidity, humidity)
        final_locations.append(location)

    res = min(final_locations)
    print(res)
    return res


main()

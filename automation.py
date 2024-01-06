# Name: automation.py
# Course: General Business Administration & Accounting
# Author: Ewo-oritse Anita Arubi
# Date: 24th December 2023


# import useful libraries...
import datetime, random, json, os, requests
from geopy.geocoders import Nominatim
from os.path import dirname, realpath
from random import randint

# a preliminary text for config.txt file
def pre_text_for_config():
    pre_text = """# Warning: DO NOT DELETE FILE OR ITS CONTENT!
# This text file serves as a guide to the automation program. It keeps count of the number of automation processes done.
# A completed task is represented by a "|-"; I call it a "pipe-dash" character.
# For example: "|-|-|-|-|-|-|-" tells the automation program that a successful record has been done for seven iterations.
# After a successful automation iteration, the number of "pipe-dash" character gets incremented by 1.
# That is, for instance, it gets updated from "|-|-|-|-|-|-|-" to  "|-|-|-|-|-|-|-|-".
# The next line keeps count of the number of days the automation has kept track of.
# The last line in the file represent the date which the last operation was run.
"""
    return pre_text

# create config.txt file IF NOT EXISTS
def create_config_file_if_not_exist():
    text = pre_text_for_config() + "\n<<<>>>\n\n<<<1>>>\n\n<<<{}>>>".format(datetime.datetime.now().strftime("%d %B %Y"))

    # check if file exists, else create it
    try:
        with open(r'output/config.txt', 'r') as f: f.readlines(1)
    except:
        with open(r'output/config.txt', 'w') as f: f.write(text)
    
    return text

# get the current time
def get_current_time():
    curr_time = datetime.datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
    curr_time = "Timestamp: " + curr_time
    return curr_time

# determine the number & day of last successful automation iterations from config.txt file
def get_config_status():
    # by default
    important_line_1 = ""; important_line_2 = ""

    with open(r'output/config.txt', 'r') as f: lines = f.readlines()

    # only recognize lines beginning with "<<<"
    lines = [line.strip() for line in lines if line.startswith("<<<")]

    # extract useful info
    try:
        # get count of the automation runs
        important_line_0 = lines[0].strip().count("|-")
        # get day of last successful automation run
        important_line_1 = int(lines[1].strip()[3:-3])
        # get date of last successful automation run
        important_line_2 = lines[2].strip()[3:-3]
    except: pass

    return list((important_line_1, important_line_2, important_line_0))

# get number of people on ISS
def people_on_ISS():
    try:
        # get info from API
        response = requests.get("http://api.open-notify.org/astros.json").text
        response_json = json.loads(response)
    except Exception as e: print(e)
        
    # return result
    return response_json["number"]

# get ISS information
def info_about_ISS():
    try:
        # get ISS information from API
        response = requests.get("https://api.wheretheiss.at/v1/satellites/25544").text
        response_json = json.loads(response)

        # get data: latitude, longitude, altitude, and velocity
        iss_lat = response_json["latitude"]
        iss_long = response_json["longitude"]
        iss_alt = response_json["altitude"]
        iss_vel = response_json["velocity"]

        # current country directly under the ISS
        geolocator = Nominatim(user_agent = "anita_app")
        iss_region = geolocator.reverse(str(iss_lat) + "," + str(iss_long))
        if iss_region != None:
            address = iss_region.raw['address']
            iss_region = address.get('state', '') + ", " + address.get('country', '')
        else:
            iss_region = "Not a country."

        # return the extracted data
        data_list = [iss_lat, iss_long, iss_alt, iss_vel, iss_region]
    except Exception as e: print(e)
    
    # return data_list
    return data_list

# get debris information
def info_about_debris(iss_data_list):
    # get object type from from random data
    object_types = ["Satellite", "Debris", "Meteor"]
    object_type = random.choice(object_types)

    # define delta and proximity acceptance for external object
    delta = 5; in_proximity = 2.5

    # retrieve object data
    iss_lat = iss_data_list[0]
    iss_long = iss_data_list[1]
    iss_vel = iss_data_list[3]

    # determine object data
    object_lat = random.uniform(iss_lat, iss_lat+delta)
    object_long = random.uniform(iss_long, iss_long+delta)
    object_vel = random.uniform(iss_vel, iss_vel+5000)

    # determine if object is in proximity, and corresponding action
    if (object_lat - iss_lat <= in_proximity):
        object_in_proximity = True
        action = "Steer horizontally!"
    elif (object_long - iss_long <= in_proximity):
        object_in_proximity = True
        action = "Steer vertically!"
    elif (object_lat - iss_lat <= in_proximity) and (object_long - iss_long <= in_proximity):
        object_in_proximity = True
        action = "Steer horizonatlly and vertically!"
    else:
        object_in_proximity = False
        action = "Do nothing."
        
    # return the extracted data
    data_list = [object_type, object_lat, object_long, object_vel, object_in_proximity, action]
    
    # return response_json, data_list
    return data_list

# get APOD information
def get_APOD():
    try:
        # get info from API
        api_key = "8jUvIWa7r2LSWhSrHKd64GTBkRRhuFgaObd0iBsQ"
        full_url = "https://api.nasa.gov/planetary/apod?api_key={}".format(api_key)
        response = requests.get(full_url).text
        response_json = json.loads(response)
    except Exception as e: print(e)

    # return result
    return response_json

# convert extracted info to text
def info_to_text(pple_on_iss, iss_info, deb_info, apod_info):
    info_str = "=" * 70

    info_str += "\n" + get_current_time() + "\n\n"
    
    info_str += "\nHello,\n"
    info_str += "\nthe ISS, containing {} persons, has the following information:".format(pple_on_iss)
    info_str += "\n\t- latitude, longitude: ({}, {})".format(iss_info[0], iss_info[1])
    info_str += "\n\t- altitude: {} km above ground level".format(iss_info[2])
    info_str += "\n\t- velocity: {} km/h".format(iss_info[3])
    info_str += "\n\t- region directly over: {}".format(iss_info[4])

    info_str += "\n\n...and the nearest object has the following information:"
    info_str += "\n\t- type: {}".format(deb_info[0])
    info_str += "\n\t- latitude, longitude: ({}, {})".format(deb_info[1], deb_info[2])
    info_str += "\n\t- velocity: {} km/h".format(deb_info[3])
    info_str += "\n\t- object in proximity: {}".format(deb_info[4])
    info_str += "\n\t- action: {}".format(deb_info[5])

    info_str += "\n\nAstronomical Picture of the Day (APOD): {}!".format(apod_info['title'])
    info_str += "\n\n"
    return info_str

# update the data file
def update_data_file(_text_str):
    with open("data.txt", "a", encoding="utf-8") as f: f.write(_text_str)
    
# update the images_json file
def update_image_json_file(apod_info):
    text = "=" * 70
    text += "\n{}: Astronomical Picture of the Day".format(datetime.datetime.now().strftime("%d %B %Y"))
    text += "\n\n" + json.dumps(apod_info, indent = 4, sort_keys = True) + "\n\n"
    with open("images_json.txt", "a") as f: f.write(text)

# save Astronomical Picture of the Day to storage location
def save_apod_to_file(apod_info):
    try:       
        # get image url
        image_url = apod_info["url"]

        # define name for image file
        file_prefix = datetime.datetime.now().strftime("%Y_%m_%d")
        file_suffix = apod_info["title"].replace(" ", "_").replace(":","_")
        filename = file_prefix + "_" + file_suffix + ".jpg"

        # get image content, and save to file
        response = requests.get(image_url)
        with open(filename, "wb") as f: f.write(response.content)
    except Exception as e:
        filename = ""
        print(e)

    return filename

# update the record of the automation process
def update_automation_sucesses():
    # read config file
    with open(r'output/config.txt', 'r') as f: lines = f.readlines()

    # by default
    important_line_0 = ""; important_line_2 = ""

    # only recognize lines beginning with "<<<"
    lines = [line.strip() for line in lines if line.startswith("<<<")]

    # extract useful info
    try:
        # to count 'pipe-dash' characters
        important_line_0 = lines[0].strip().count("|-")
        # get date of last successful automation run
        important_line_2 = lines[2].strip()[3:-3]
        # get day of last successful automation run
        important_line_1 = int(lines[1].strip()[3:-3])
    except:
        important_line_1 = 0

    # update all configuration info
    important_line_0 = "<<<" + ("|-" * (important_line_0 + 1)) + ">>>"
    
    curr_date = datetime.datetime.now().strftime("%d %B %Y")
    if curr_date != important_line_2:
        important_line_1 = "<<<" + str(important_line_1 + 1) + ">>>"
    else:
        important_line_1 = "<<<" + str(important_line_1) + ">>>"        

    important_line_2 = "<<<" + (datetime.datetime.now().strftime("%d %B %Y")) + ">>>"

    # update config text
    text = pre_text_for_config()
    text += "\n" + important_line_0 + "\n"
    text += "\n" + str(important_line_1) + "\n"
    text += "\n" + important_line_2

    # write updated config text to file
    with open(r'output/config.txt', 'w') as f: f.write(text)

    return True

# gather all functions
def go():
    return_value = True
    
    try:
        # check IF config.txt EXISTS, else create it
        create_config_file_if_not_exist()
        
        # fetch number and date of last successful automation iterations
        base_path = dirname(realpath(__file__))
        from_config = get_config_status()
        curr_day_num = from_config[0]
        
        # fetch number of people on ISS
        pple_on_iss = people_on_ISS()

        # fetch ISS information
        iss_info = info_about_ISS()

        # fetch debris information
        deb_info = info_about_debris(iss_info)

        # fetch image of the day
        apod_info = get_APOD()
        
        # determine and move into appropriate storage location
        index = 1
        while (curr_day_num > 7):
            index += 1; curr_day_num -= 7
        save_dir = "output/week_" + str(index)
        try: os.mkdir(save_dir)
        except: pass
        finally: os.chdir(save_dir)

        # update data file
        text_string = info_to_text(pple_on_iss, iss_info, deb_info, apod_info)
        update_data_file(text_string)

        # update images_json file, if current date IS NOT last saved date
        curr_date = datetime.datetime.now().strftime("%d %B %Y")
        if from_config[-1] == 0: update_image_json_file(apod_info)
        if curr_date != from_config[1]: update_image_json_file(apod_info)

        # save image into location, return to base path
        save_apod_to_file(apod_info)
        os.chdir(base_path)

        # update number of successful automation iterations
        update_automation_sucesses()
    except Exception as e:
        print("Exception error:", e)
        return_value = False
        
    return return_value

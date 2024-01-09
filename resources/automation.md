# HOW THE AUTOMATION WORKS

## Importing Libraries:
```
import datetime, random, json, os, requests
from geopy.geocoders import Nominatim
from os.path import dirname, realpath
from random import randint
```

The code starts by importing necessary libraries. These include modules for working with dates and times (datetime), generating random numbers (random), handling JSON data (json), interacting with the operating system (os), and making HTTP requests (requests). It also imports specific functionality (Nominatim) from the geopy library for geocoding purposes.

## Preliminary Text for config.txt:

```
def pre_text_for_config():
    pre_text = """# Warning: DO NOT DELETE FILE OR ITS CONTENT!
    # ... (rest of the comments explaining the purpose of the config.txt file)
    """
    return pre_text
```
Defines a function pre_text_for_config that returns a multiline comment explaining the purpose of the config.txt file.

## Creating or Checking config.txt:

```
def create_config_file_if_not_exist():
    text = pre_text_for_config() + "\n<<<>>>\n\n<<<1>>>\n\n<<<{}>>>".format(datetime.datetime.now().strftime("%d %B %Y"))

    try:
        with open(r'output/config.txt', 'r') as f: f.readlines(1)
    except:
        with open(r'output/config.txt', 'w') as f: f.write(text)
    
    return text
```
Defines a function create_config_file_if_not_exist that creates or checks the existence of the config.txt file. If the file doesn't exist, it creates it with the preliminary text.

## Getting Current Time:

```
def get_current_time():
    curr_time = datetime.datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
    curr_time = "Timestamp: " + curr_time
    return curr_time
```
Defines a function get_current_time that returns the current timestamp in a specific format.

## Getting Config Status:

```
def get_config_status():
    # ... (omitted for brevity)
    return list((important_line_1, important_line_2, important_line_0))
```
Defines a function get_config_status that reads information from the config.txt file, extracts relevant data, and returns it in a list.

## Getting Number of People on ISS:

```
def people_on_ISS():
    try:
        response = requests.get("http://api.open-notify.org/astros.json").text
        response_json = json.loads(response)
    except Exception as e: print(e)
        
    return response_json["number"]
```
Defines a function people_on_ISS that retrieves information about the number of people currently on the International Space Station (ISS) using an API.

## Getting ISS Information:

```
def info_about_ISS():
    # ... (omitted for brevity)
    return data_list
```
Defines a function info_about_ISS that retrieves information about the ISS (latitude, longitude, altitude, velocity, and the region directly under the ISS) using another API.

## Getting Debris Information:

```
def info_about_debris(iss_data_list):
    # ... (omitted for brevity)
    return data_list
```
Defines a function info_about_debris that generates random information about an external object (satellite, debris, or meteor) in proximity to the ISS.

## Getting APOD Information:

```
def get_APOD():
    # ... (omitted for brevity)
    return response_json
```
Defines a function get_APOD that retrieves information about the Astronomy Picture of the Day (APOD) using the NASA API.

## Converting Extracted Info to Text:

```
def info_to_text(pple_on_iss, iss_info, deb_info, apod_info):
    # ... (omitted for brevity)
    return info_str
```
Defines a function info_to_text that converts the retrieved information into a formatted text string.

## Updating Data File:

```
def update_data_file(_text_str):
    with open("data.txt", "a", encoding="utf-8") as f: f.write(_text_str)
```
Defines a function update_data_file that appends the formatted text string to a data file.

## Updating Images JSON File:

```
def update_image_json_file(apod_info):
    # ... (omitted for brevity)
```
Defines a function update_image_json_file that appends information about the APOD to an images JSON file.

## Saving APOD to File:

```
def save_apod_to_file(apod_info):
    # ... (omitted for brevity)
    return filename
```
Defines a function save_apod_to_file that saves the APOD image to a file and returns the filename.

## Updating Automation Successes:

```
def update_automation_sucesses():
    # ... (omitted for brevity)
    return True
```
Defines a function update_automation_sucesses that updates the configuration file to record the success of the automation process.

## Main Automation Function:
```
def go():
    return_value = True
    
    try:
        # ... (omitted for brevity)
    except Exception as e:
        print("Exception error:", e)
        return_value = False
        
    return return_value
```
Defines the main function go that orchestrates the entire automation process. It calls various functions to fetch data, update files, and handle exceptions.
Overall, the code is a script for automating the retrieval and processing of information related to the International Space Station (ISS), external objects, and the Astronomy Picture of the Day (APOD). It utilizes several APIs and files to store and organize the obtained data.




# Week 1; 5th Jan.: Unveiling the Wonders of Space Automation
Welcome back, cosmic explorers!
This week, our Python-powered space automation journey kicks off with an exploration of the vast universe. Buckle up as we delve into the intricacies of data fetching, processing, and the magic of the cosmos.

**Setting the Stage: config.txt and Previous Task Insights**
Our cosmic adventure begins with the backbone of our operation - the config.txt file. This essential file is our compass, guiding us through the vastness of space. It keeps a meticulous record of our past tasks, ensuring a smooth continuation of our interstellar exploration.


```
# Create or Check Config File
create_config_file_if_not_exist()

# Fetch Previous Task Info
from_config = get_config_status()
```

## ISS Insights: Beyond Earth's Atmosphere
Our first destination is the International Space Station (ISS), a microgravity laboratory orbiting Earth. Let's harness Python to fetch key details, including the number of astronauts on board and the ISS's current location.


```
# Fetch ISS and Other Info
pple_on_iss = people_on_ISS()
iss_info = info_about_ISS()
deb_info = info_about_debris(iss_info)
apod_info = get_APOD()
```

## From Data to Narrative: Crafting a Cosmic Tale
Now armed with celestial data, it's time to weave it into a cosmic narrative. The info_to_text function converts raw data into a captivating story, making our space exploration journey not only informative but also enjoyable.

```
# Convert Info to Text
text_string = info_to_text(pple_on_iss, iss_info, deb_info, apod_info)

# Update Data File
update_data_file(text_string)
```
As our data file evolves, so does our understanding of the cosmos. Join us next week as we continue to expand our celestial database, enriching our knowledge of space one byte at a time.

Stay curious, space enthusiasts! 🚀🌌
 
 SEE YOU NEXT WEEK.



# Week 2 - 12th Jan.: Celestial Chronicles - Unveiling the Wonders Continues
Greetings, cosmic voyagers! As our Python-powered spacecraft hurtles through the cosmic expanse, we find ourselves in the embrace of Week 2. This week promises an even deeper dive into the celestial wonders that adorn our universe. Buckle up, fellow space enthusiasts, as we embark on another week of interstellar exploration.

**The Art of Updating: Enhancing our Cosmic Gallery**
Our cosmic journey is not just about data; it's an art form. This week, our attention turns to the images_json.txt file, our cosmic art gallery. Here, we meticulously curate the latest wonders from the Astronomy Picture of the Day (APOD).

```
# Update Image Information File
`update_image_json_file(apod_info)`
```

**The Symphony of Cosmic Imagery**
The images we collect aren't mere pixels; they're symphonies composed by the cosmos. Each APOD image captures the visual poetry of our universe, from the intricate dance of nebulae to the distant melodies of galaxies.

This week is a celebration of the aesthetics of space photography. The vibrant hues of celestial bodies, the play of light and shadow in cosmic landscapes – every image is a masterpiece, inviting us to appreciate the artistry inherent in the vastness of space.

## APOD Unveiled: Downloading the Cosmic Canvas
The Astronomy Picture of the Day isn't just a visual treat; it's a cosmic canvas that tells stories of our universe. In Week 2, we download and preserve the latest APOD image, ensuring that each pixel is a brushstroke in the grand artwork of the cosmos.

```
# Save Image File
filename = save_apod_to_file(apod_info)
```

**A Visual Journey Through Space**
Our growing collection of cosmic images is more than a gallery; it's a visual journey through the tapestry of space and time. From the surreal beauty of distant galaxies to the kaleidoscopic swirls of interstellar clouds, each image adds a new chapter to our cosmic narrative.

**Building Bridges to the Stars: A Digital Archive Expands**
Our digital archive is not just a storage space; it's a bridge that connects us to the stars. Each saved image becomes a portal, allowing us to traverse the vastness of space with just a click.

As we wrap up Week 2, our cosmic gallery stands testament to the mesmerizing beauty of the universe. Join us next week as we continue to uncover the mysteries of the cosmos, adding new pages to our digital cosmic diary.

Keep gazing at the stars, intrepid space travelers! 🚀🌌

See you next week, as our journey continues....








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


# HOW TO RUN THE AUTOMATION
## To run the provided automation script, follow these steps:

## Prerequisites:
 - Python Installation:
Ensure that Python is installed on your system. During installation, make sure to check the option to add Python to your system's PATH.

- Dependencies:
Install the required Python packages(External libaries)by running the following command in your terminal or command prompt:

`pip install geopy requests`

## Steps to Run the Automation Script:
- Download the Script:
Download the provided Python script to your computer. Save it with an appropriate filename, e.g., automation.py.
Open a Terminal or Command Prompt:

 - Open a terminal on Linux/Mac or command prompt on Windows.
Navigate to the Script's Directory:

- Use the cd command to navigate to the directory where you saved the script.

Bash
```
cd path/to/script/directory
Run the Script:
```

Execute the script by running the following command:

`python automation.py`

If you're using Python 3, use the following command:

`python3 space_automation.py`

## Review the Output:

The script will start executing the automation tasks, fetching information about the International Space Station (ISS), nearby debris, and the Astronomical Picture of the Day (APOD).
It will generate a human-readable report and update data and image files.
Check Output Files:

The script will create output files, including data.txt and images_json.txt, in the specified storage location (e.g., output/week_X). Additionally, the script will update the config.txt file.

Review the Results:
Open the generated data.txt file to review the synthesized information about the ISS, debris, and APOD.
Check the images_json.txt file for information about the APOD image.
Explore Storage Location:

Navigate to the storage location specified in the script (e.g., output/week_X). Check for saved image files and other relevant data.
Important Notes:
Ensure an internet connection is available as the script fetches real-time data from external APIs.
Any errors or exceptions during script execution will be displayed in the terminal/command prompt.

By following these steps, you should be able to successfully run the provided automation script and explore the generated results and files.













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




# Week 1; 5TH Jan.: Unveiling the Wonders of Space Automation
## Introduction and Libraries Import
The script commences with an essential section where it imports various libraries. This action is pivotal for the script's functionality, as it brings in powerful tools such as datetime for handling time-related operations, random for generating random data, json for working with JSON data, os for interacting with the operating system, and requests for making HTTP requests. Furthermore, it imports specific modules from the geopy library, enhancing its geocoding capabilities.

## Configuration File and Preliminary Text
The script, being a robust automation tool, establishes a structured foundation with the pre_text_for_config() function. This function generates a preliminary text intended for the config.txt file. The config.txt file plays a crucial role in tracking the automation processes. The explanatory comments within this function underscore its significance. The file not only serves as a guide for the automation program but also maintains a count of completed tasks, a representation of which is done through the innovative use of a "pipe-dash" character. This detailed explanation within the code showcases a meticulous approach to documentation and transparency in code design.

## Config File Creation
Continuing with the theme of configuration, the script meticulously checks for the existence of the config.txt file through the create_config_file_if_not_exist() function.
```
# Create or Check Config File
create_config_file_if_not_exist()

# Fetch Previous Task Info
from_config = get_config_status()
```

This function not only ensures the file's presence but also initializes it with default values using the preliminary text generated earlier. This level of attention to detail reflects good coding practices, ensuring that the automation program can seamlessly access and update the necessary configuration information.

## Current Time Retrieval
A subtle yet crucial function, get_current_time(), is introduced to fetch the current timestamp.
```
# get the current time
def get_current_time():
``` 
This timestamp, formatted as a string, includes information about the day, month, year, and precise time, providing valuable insights into when specific operations within the script occurred. The thoughtful inclusion of this function highlights the developer's commitment to logging and tracking temporal aspects of the automation process.

## Config Status Retrieval
The script further solidifies its configuration management capabilities with the get_config_status() function. This function reads and extracts vital information from the config.txt file. It intelligently interprets the "pipe-dash" characters, indicating completed tasks, and retrieves the count of automation runs, the day of the last successful run, and the date of the last operation. Such meticulous tracking and retrieval mechanisms lay the groundwork for comprehensive automation process management.

## ISS Information Retrieval
The script takes a turn towards space exploration, introducing functions like people_on_ISS() and info_about_ISS(). These functions leverage external APIs to fetch real-time information about the International Space Station (ISS).
```
# Fetch ISS and Other Info
pple_on_iss = people_on_ISS()
iss_info = info_about_ISS()
``` 

The former retrieves the number of people currently on the ISS, while the latter provides detailed information about the ISS, including its latitude, longitude, altitude, velocity, and the country directly beneath it. This integration of external APIs demonstrates the script's capability to interact with diverse data sources, enriching its functionality.

## Debris Information Retrieval
The narrative unfolds with the introduction of the info_about_debris() function, simulating the retrieval of information about objects near the ISS. 

`deb_info = info_about_debris(iss_info)`

The script randomly generates data for an object's type, latitude, longitude, and velocity. It then assesses whether the object is in proximity to the ISS and determines a corresponding action. This simulated scenario adds a layer of complexity to the script, showcasing its versatility in handling various situations that may arise during space exploration.

### Week 1 Summary
Week 1 lays a solid foundation, covering the script's initialization, configuration file management, and the retrieval of information about the ISS and nearby debris. The meticulous attention to configuration details, coupled with the integration of external APIs, positions the script as a robust and extensible automation tool for space-related data.

Stay curious, space enthusiasts! 🚀🌌

SEE YOU NEXT WEEK.




# Week 2; 12TH Jan.:Celestial Chronicles - Unveiling the Wonders Continues
## APOD Information Retrieval
The second week of exploration begins with the introduction of the get_APOD() function. 

`apod_info = get_APOD()`

This function, using NASA's API, fetches information about the Astronomical Picture of the Day (APOD). The inclusion of this function broadens the script's scope, transforming it from a focused ISS data retrieval tool to a more holistic space exploration utility.

## Text Generation
With the acquired information about the ISS, debris, and APOD, the script enters the realm of text generation through the info_to_text() function. 
```
# Convert Info to Text
text_string = info_to_text(pple_on_iss, iss_info, deb_info, apod_info)
```

This function consolidates the extracted information into a structured and human-readable text format. The resulting text string serves as a detailed report, providing insights into the current state of the ISS, nearby objects, and the captivating APOD. The inclusion of such text generation capabilities enhances the script's communicative aspect, making it more accessible to users.

## Data and Image File Update
The narrative evolves as the script takes a proactive approach to data and file management. Functions like update_data_file(), update_image_json_file(), and save_apod_to_file() come into play. 
```
# Update Data File
update_data_file(text_string)

# Update Image Information File
update_image_json_file(apod_info)

# Save Image File
filename = save_apod_to_file(apod_info)
```

These functions ensure that the gathered information is not only presented in a human-readable format but also archived systematically. The script writes to data files, updates records of automation successes, and even saves the APOD image to a storage location, adding a layer of persistence to its operations.

### Week 2 Summary
Week 2 unveils the script's expansion into APOD data retrieval, text generation, and systematic file management. The introduction of the main orchestrator, go(), highlights the script's integration of diverse functionalities, making it a cohesive and dynamic space exploration tool.

Keep your eyes on the stars, fellow space travelers! 🌌🚀

SEE YOU IN WEEK 3.



# Week 3; 19TH Jan.:Storage Location Determination
## Adaptive Storage Organization
One of the key features introduced in Week 3 is the adaptive storage location determination mechanism. This functionality aims to dynamically organize data and image files based on the current day number. The purpose is to maintain a well-structured storage hierarchy, enhancing the script's scalability and organization.

## Understanding the Need
As the automation process progresses, data and image files accumulate. To prevent these files from becoming overwhelming and to facilitate easy retrieval, the script intelligently calculates an appropriate storage location for these files. This determination is driven by the current day number, providing a systematic way to categorize files over time.

## Initial Setup
The storage location determination process begins with the calculation of an index. This index represents the week in which the current day falls. The idea is to group files into weekly folders, ensuring a manageable structure.

```
index = 1
while (curr_day_num > 7):
    index += 1
    curr_day_num -= 7
```

Here, a while loop is employed to iterate through the weeks. The index variable increments each time a full week has passed, and the curr_day_num (current day number) decreases accordingly. This loop effectively calculates the week index for the current day.

## Storage Directory Creation
Once the index is determined, the script moves on to create the storage directory. The directory is named in a structured manner to reflect the week number.

```
save_dir = "output/week_" + str(index)
try:
    os.mkdir(save_dir)
except:
    pass
finally:
    os.chdir(save_dir)
```

Here, the os.mkdir() function attempts to create the directory. If the directory already exists, the script gracefully moves on without raising an error. Finally, the script changes its working directory to the newly created (or existing) directory.

## Why Adaptive Storage?
The adaptive storage organization ensures that as the automation process continues over time, files are not lumped into a single directory but are instead organized into weekly folders. This structure makes it easier for users to navigate and manage the growing volume of data and image files.

### Integration with Main Orchestrator (go() Function)
The storage location determination process seamlessly integrates into the main orchestrator, the go() function. After fetching the current day number from the config.txt file, the script utilizes this information to determine the appropriate storage location before executing subsequent tasks.

## Conclusion of Storage Location Determination
Week 3 introduces a thoughtful approach to storage organization, addressing the need for adaptive categorization of data and image files. By dynamically determining storage locations based on the current day number, the script ensures a well-organized and scalable structure for long-term use. This adaptive storage mechanism aligns with best practices for data management, showcasing the script's commitment to efficiency and user-friendly file organization.

SEE YOU IN THE FINAL WEEK, SPACE EXPLORERS! 🚀🌌




# Week 4(Final Week); 26th Jan:Space Insights Automation
Welcome Back Space Explorers!🌟🚀
The fourth and final week of the script's exploration journey culminates with the execution of the main orchestrator, the go() function. In this week, the script brings together all its functionalities to retrieve real-time information about the International Space Station (ISS), nearby debris, and the Astronomical Picture of the Day (APOD). The go() function serves as the central conductor, orchestrating a seamless sequence of tasks that result in a comprehensive report and well-organized storage of data and images.

## Key Elements of the Final Execution
### Initial Configuration Check
The script begins by checking the existence of the crucial config.txt file using the create_config_file_if_not_exist() function. This ensures the script has the necessary configuration file to guide its operations. If the file doesn't exist, the function creates it, initializing it with default values.


```
# Check IF config.txt EXISTS, else create it
create_config_file_if_not_exist()
```

### Retrieval of Current Day Number
The script fetches crucial information from the config.txt file using the get_config_status() function. The current day number is extracted, representing the count of days the automation has been running. This information is essential for determining the appropriate storage location for data and image files.

```
# Fetch number and date of last successful automation iterations
from_config = get_config_status()
curr_day_num = from_config[0]
```

### People on ISS
The script fetches real-time information about the number of people currently on the International Space Station (ISS) using the people_on_ISS() function. This dynamic element adds an extra layer of relevance to the automation process.

```
# Fetch number of people on ISS
pple_on_iss = people_on_ISS()
```

### ISS Information Retrieval
Detailed information about the ISS, including its latitude, longitude, altitude, velocity, and the region directly beneath it, is obtained using the info_about_ISS() function.

```
# Fetch ISS information
iss_info = info_about_ISS()
```

### Debris Information Retrieval
The info_about_debris() function is invoked to simulate the retrieval of information about nearby objects. Random data for an object's type, latitude, longitude, and velocity is generated. The script then assesses whether the object is in proximity to the ISS and determines a corresponding action.

```
# Fetch debris information
deb_info = info_about_debris(iss_info)
```

### APOD Information Retrieval
The script broadens its scope by fetching information about the Astronomical Picture of the Day (APOD) using the get_APOD() function. This function interacts with NASA's API, retrieving details about the captivating image that graces the APOD.

```
# Fetch image of the day
apod_info = get_APOD()
```

### Text Generation
The gathered information about the ISS, nearby debris, and the APOD is then passed to the info_to_text() function. This function synthesizes the data into a structured and human-readable text format.

```
# Generate text
text_string = info_to_text(pple_on_iss, iss_info, deb_info, apod_info)
```

### Data and Image File Update
The script takes proactive steps to update data and image files. Functions like update_data_file(), update_image_json_file(), and save_apod_to_file() ensure that the gathered information is not only communicated in the report but also archived systematically.
```
# Update data file
update_data_file(text_string)
# Update images_json file, if the current date IS NOT the last saved date
curr_date = datetime.datetime.now().strftime("%d %B %Y")
if from_config[-1] == 0:
    update_image_json_file(apod_info)
if curr_date != from_config[1]:
    update_image_json_file(apod_info)
```

### Storage Location Determination
An adaptive approach to storage location determination follows. The script intelligently calculates the appropriate storage location for data and image files based on the current day number.

```
# Determine and move into the appropriate storage location
index = 1
while (curr_day_num > 7):
    index += 1
    curr_day_num -= 7
save_dir = "output/week_" + str(index)
try:
    os.mkdir(save_dir)
except:
    pass
finally:
    os.chdir(save_dir)
```

## Automation Success Update
The final act of the go() function involves updating the config.txt file with the current status of automation successes using the update_automation_successes() function. This function increments the count of completed tasks, updates the date of the last operation, and ensures that the configuration file stays synchronized with the script's execution.

```
# Update the number of successful automation iterations
update_automation_sucesses()
```

## Return Value
The go() function concludes with a return value, indicating the success or failure of the automation process. This return value serves as a crucial indicator for users, providing immediate feedback on the outcome of the script's execution.

```
# Return success indicator
return return_value
```

# Conclusion of Final Script Execution
The final script execution in Week 4 encapsulates the essence of the entire exploration journey. The go() function, acting as the script's main orchestrator, seamlessly integrates various tasks, from real-time data retrieval to text generation, file management, and configuration updates. Its modular design, emphasis on real-time data, and commitment to systematic file organization make it a powerful and dynamic orchestrator, ensuring the script's effectiveness in space-related data automation. The return value serves as a testament to the success or failure of the script's mission, providing users with valuable feedback. The script, through its four-week journey, emerges as a robust and multifaceted automation tool for space-related data.


# Time to Bid Code-voyage and Blast Off! 🚀

Hey Space Cadet,

Our cosmic journey is taking a pit stop! 🛸🛰️ We've surfed the interstellar waves, busted some code moves with the ISS, dodged space debris like pros, and enjoyed the dazzling Astronomical Picture of the Day (APOD) show! 🌠🎉

Our script? Oh, it's been the MVP, fetching data faster than a pizza delivery and organizing files smoother than butter on a hot pancake.

As we drop the cosmic mic on this code party, remember – bugs are just the universe telling you a joke. Keep coding, stay curious, and may your code be as flawless as a cat meme.

Catch you on the flip side of the code galaxy!👋🚀

-  Cosmic Cheers and See Ya Later, Space Coder! 🌌👋














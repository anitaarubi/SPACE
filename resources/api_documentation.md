Welcome to documentation section. This documentations provides sufficient information on how I integrated and utilized the functionalities offered by various  APIs. 

Please refer to the sections below for details on endpoints, parameters, authentication, error handling, and more. For more info, please visit the website URL provided in the respective API sections. 

---
# 1. How Many People Are In Space Right Now

## Description:

This API returns the current number of people in space. When known it also returns the names and spacecraft those people are on. This API takes no inputs.

## Website URL:

http://open-notify.org/Open-Notify-API/People-In-Space/

**Request Example:**

```python
import json, requests

response = requests.get("http://api.open-notify.org/astros.json").text
response_json = json.loads(response)
```

**Response Example:**

```json
{
	"message": "success", 
	"people": [
		{ "name": "Jasmin Moghbeli", 
		"craft": "ISS"}, 
		{ "name": "Andreas Mogensen", 
		 "craft": "ISS"}, 
		{ "name": "Satoshi Furukawa", 
		 "craft": "ISS"}, 
		{ "name": "Konstantin Borisov", 
		 "craft": "ISS"}, 
		{ "name": "Oleg Kononenko", 
		 "craft": "ISS"}, 
		{ "name": "Nikolai Chub", 
		 "craft": "ISS"}, 
		{ "name": "Loral O'Hara", 
		 "craft": "ISS"}], 
	"number": 7
}
```

---

# 2. Where the ISS at?

## Description:

Welcome to the WTIA REST API! Using this service, you can get current, past, or future position of the ISS, get timezone information about a set of coordinates, and also get Two-line element (TLE) data on the ISS.

## Website URL:

https://wheretheiss.at/w/developer

## Endpoints:

### satellites/[id]

**Description:** Returns position, velocity, and other related information about a satellite for a given point in time. [id] is required and should be the NORAD catalog id. For the ISS, that id is 25544.

**URL:** `https://api.wheretheiss.at/v1/satellites/25544`

**Parameters:**

- `units`: Whether to use miles or kilometers. Default is "kilometers".
- `timestamp`: Optionally specify a timestamp for orbital position. Default is "current timestamp".

**Request Example:**

```python
import json, requests

response = requests.get("https://api.wheretheiss.at/v1/satellites/25544").text
response_json = json.loads(response)
```

**Response Example:**

```json
{
    "name": "iss",
    "id": 25544,
    "latitude": 50.11496269845,
    "longitude": 118.07900427317,
    "altitude": 408.05526028199,
    "velocity": 27635.971970874,
    "visibility": "daylight",
    "footprint": 4446.1877699772,
    "timestamp": 1364069476,
    "daynum": 2456375.3411574,
    "solar_lat": 1.3327003598631,
    "solar_lon": 238.78610691196,
    "units": "kilometers"
}
```

## Authentication:

Currently there is no authentication required for accessing the WTIA REST API, but some endpoints likely will allow for authentication in the future. In the meantime, please note the rate limits below.

## Rate Limits:

Currently requests are limited to roughly 1 per second. You can keep track of your usage by looking at the X-Rate-Limit headers returned in each response.

---

# 3. Astronomy Picture of the Day (APOD)

## Description:

[Discover the cosmos!](https://apod.nasa.gov/apod/archivepix.html) Each day a different image or photograph of our fascinating universe is featured, along with a brief explanation written by a professional astronomer.
 
## Website URL:

https://apod.nasa.gov/apod/astropix.html

**Request Example:**

```python
import json, requests

api_key = "DEMO_KEY"
full_url = "https://api.nasa.gov/planetary/apod?api_key={}".format(api_key)
response = requests.get(full_url).text
response_json = json.loads(response)
```

**Response Example:**

```json
{
    "date": "2024-01-15",
    "explanation": "Sometimes, it's the stars that are the hardest to see that are the most interesting. IC 348 is a young star cluster that illuminates surrounding filamentary dust.  The stringy and winding dust appears pink in this recently released infrared image from the Webb Space Telescope. In visible light, this dust reflects mostly blue light, giving the surrounding material the familiar blue hue of a reflection nebula.  Besides bright stars, several cool objects have been located in IC 348, visible because they glow brighter in infrared light.  These objects are hypothesized to be low mass brown dwarfs.  Evidence for this includes the detection of an unidentified atmospheric chemical, likely a hydrocarbon, seen previously in the atmosphere of Saturn. These objects appear to have masses slightly greater than known planets, only a few times greater than Jupiter.  Together, these indicate that this young star cluster contains something noteworthy -- young planet-mass brown dwarfs that float free, not orbiting any other star.",
    "hdurl": "https://apod.nasa.gov/apod/image/2401/IC348_webb_3788.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Star Cluster IC 348 from Webb",
    "url": "https://apod.nasa.gov/apod/image/2401/IC348_webb_960.jpg"
}
```


## Authentication:

Authentication is required for this API usage. Visit https://api.nasa.gov/#signUp to generate your API key.

## Additional Information:

The full documentation for this API can be found in the [APOD API Github repository](https://github.com/nasa/apod-api).

---
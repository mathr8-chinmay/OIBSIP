# Weather Application

## Description
This is a Python-based Weather Application that provides real-time weather information and weather forecasts for any valid city using the WeatherAPI. Users can view the current weather conditions or forecast for up to three days through a simple menu-driven interface.

## Note
Before running this project , create a free WeatherAPI account, get your API key there and enter your own API key when prompted 

## Features
- Displays current weather information.
- Displays weather forecast for up to 3 days.
- Uses WeatherAPI to fetch live weather data.
- Menu-driven interface.
- Validates user input.
- Handles invalid city names.
- Handles invalid menu choices.
- Handles invalid forecast day input.
- Handles API errors such as invalid API key.
- Handles network connection and timeout errors using exception handling.

## Inputs
The program takes the following inputs from the user:
- Weather Option
  - Current Weather
  - Weather Forecast
  - Exit
- City Name
- Number of Forecast Days (1–3)

## Output
The program displays:

### Current Weather
- City Name
- Country
- Local Date & Time
- Temperature
- Feels Like Temperature
- Weather Condition
- Humidity
- Wind Speed
- Pressure
- Visibility
- UV Index
- Air Quality Index (AQI)

### Weather Forecast
- Date
- Weather Condition
- Maximum Temperature
- Minimum Temperature
- Average Temperature
- Average Humidity
- Maximum Wind Speed
- UV Index
- Chance of Rain
- Sunrise Time
- Sunset Time

## Technologies Used
- Python 3
- requests module
- JSON
- WeatherAPI

## How to Run
1. Run the Python file.
2. Select one of the available options:
   - Current Weather
   - Weather Forecast
   - Exit
3. Enter the city name.
4. If Weather Forecast is selected, enter the number of forecast days (1–3).
5. The application displays the requested weather information.

## Example

Input:

Weather Option: Forecast

City: Jaipur

Forecast Days: 3

Output:

Displays the 3-day weather forecast including temperature, weather condition, humidity, wind speed, UV index, chance of rain, sunrise, and sunset information.
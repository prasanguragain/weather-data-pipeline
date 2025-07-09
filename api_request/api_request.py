import requests



api_key="e34280e90bb21b3b014f5198849ace6e"
api_url=f"http://api.weatherstack.com/current?access_key={api_key}&query=Itahari"
def fetch_data():
    print("Fetching whether data from whetherstack API....")
    try:
        response=requests.get(api_url)
        response.raise_for_status()
        print("API response recieved successfully")
        return response.json()
    except requests.exception.RequestException as e:
        print(f"An error occoured:{e}")
        raise


# def mock_fetch_data():
#     return{
#         'request': {
#         'type': 'City',
#         'query': 'Itahari, Nepal',
#         'language': 'en',
#         'unit': 'm',
#         }, 

#         'location':{
#             'name': 'Itahari',
#             'country': 'Nepal', 
#             'region': '', 
#             'lat': '26.667',
#             'lon': '87.283', 
#             'timezone_id': 'Asia/Kathmandu',
#             'localtime': '2025-07-04 06:53', 
#             'localtime_epoch': 1751611980, 
#             'utc_offset': '5.75',
#             },
#         'current': {
#             'observation_time': '01:08 AM', 
#             'temperature': 27, 'weather_code': 116, 
#             'weather_icons': [
#                 'https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'
#                 ],
#             'weather_descriptions': [
#                 'Partly Cloudy '
#                 ],
#             'astro': {
#                 'sunrise': '05:07 AM', 
#                 'sunset': '06:54 PM', 
#                 'moonrise': '01:19 PM', 
#                 'moonset': '12:03 AM', 
#                 'moon_phase': 'Waxing Gibbous', 
#                 'moon_illumination': 61,
#                 }, 
#             'air_quality':{ 
#                 'co': '519.85', 
#                 'no2': '17.575', 
#                 'o3': '51', 
#                 'so2': '3.7', 'pm2_5': '30.71', 
#                 'pm10': '31.82', 
#                 'us-epa-index': '2', 
#                 'gb-defra-index': '2',
#                 },
#             'wind_speed': 7, 
#             'wind_degree': 108, 
#             'wind_dir': 'ESE', 
#             'pressure': 1002, 
#             'precip': 0, 
#             'humidity': 80, 
#             'cloudcover': 47, 
#             'feelslike': 30, 
#             'uv_index': 1, 
#             'visibility': 10, 
#             'is_day': 'yes',
#             }
#         }
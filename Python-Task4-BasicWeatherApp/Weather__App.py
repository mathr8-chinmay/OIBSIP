import requests
print("\n==============================================================================================================")
print("\n=========================================WEATHER APP==========================================================\n")
print("==============================================================================================================")

API_key = input("Enter your API key here : ")

city = input("\n\nEnter City Name : ")
while True:
    

        print("\nSelect the type : ")
        print("1. Current Weather ")
        print("2. Weather forecast")
        print("3. Exit\n\n")
        
        try:
            choice = int(input("Enter your choice : "))
        except:
            print("\nError : Please enter a valid option.")
            continue
            

        if(choice ==1 ):
            try:
                response1 = requests.get("https://api.weatherapi.com/v1/current.json?key=" +API_key+ "&q="+city+"&aqi=yes",timeout=5)
            except requests.exceptions.ConnectionError:
                print("No Internet Connection ")
                print("Please check your Internet ")
                continue
            except requests.exceptions.Timeout:
                print("Connection Time out")
                print("Plrase check your internet")
                continue

            code = (response1.status_code)

            data = response1.json()

            if(code !=200):
                if(code==401):
                    print("\nError Code : ", code)
                    print("Error : ", data['error']['message'])
                    API_key = input("Enter your API key again : ")
                    continue
                print("\nError Code : ", code)
                print("Error : ", data['error']['message'])
                city = input("\nEnter city again : ")
                continue
              
            
            
            print("-----------------------------------------------------------")
            print("\ncity :: ",data['location']['name'])
            print('Current Temprature :: ', data['current']['temp_c'],'°C')# ° = alt + 0176
            print("Feels like :: ", data['current']['feelslike_c'], "°C")
            print("Weather Conditions :: ", data['current']['condition']['text'])
            print("Humidity :: ", data['current']['humidity'],"%")
            print("AQI :: ", data["current"]["air_quality"]['pm2_5'])
            print("Wind Speed (km/h) :: ",data['current']['wind_kph']," Km/hr")
            print("Wind Direction :: ", data['current']['wind_dir'],"\n")

            uv = data['current']['uv']
            print("UV index :: ", uv)

            if (0.0 <= uv <=2.9):
                print("Minimal Risk ")
            elif(2.9 < uv <=5.9): 
                print("Moderate Risk")
            elif(5.9 < uv <=7.9):
                print("High Risk")
                print("Protection is essential")
            elif(7.9 < uv <=10.9):
                print("Very High Risk")
                print("Avoid outdoor sun exposure")
            elif(11 < uv ):
                print("Extreme Risk")
                print("Unprotected Skin can burn in minutes ")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            print("\n\n")
            break
            
            
        
        elif(choice==2):
            while True:
                try:
                    day = int(input("\nEnter number of days for forecast : "))
                except:
                    print("\nError : Letters or decimal numbers are not accepted. Please enter digits only.")
                    print("\nEnter number of days for forecast again")
                    continue
                    
                try:
                    response2 = requests.get("https://api.weatherapi.com/v1/forecast.json?key="+API_key + "&q="+city+"&days="+str(day))
                except requests.exceptions.ConnectionError:
                    print("\nNo Internet connection")
                    print("Please check your Internet")
                    break

                except requests.exceptions.Timeout:
                    print("\nConnection Time Out")
                    print("Please check your Internet connection")
                    break
                
                data = response2.json()

                code = ((response2.status_code))

                if(code !=200):
                    if(code== 401):
                         print("\nError Code : ", code)
                         print("Error : ", data['error']['message'])
                         API_key = input("Enter your API key again : ")
                         continue
                    print("\nError Code : ", code)
                    print("Error : ", data['error']['message'])
                    city = input("\nEnter city again : ")
                    continue

                print("-----------------------------------------------------------")
                print("\nCity :: ", data['location']['name'])
                for i in range(0,day):
                    if(i==0):
                        print("\nDay --1 (Today)")
                    elif(i==1):
                        print("Day --2 (Tommorow)")
                    else:
                        print("Day --", i+1)
                
                    print("Date :: ", data['forecast']['forecastday'][i]['date'])
                    print("Maximum Temperature :: ", data['forecast']['forecastday'][i]['day']['maxtemp_c'],"°C")
                    print("Minimum Temperature :: ", data['forecast']['forecastday'][i]['day']['mintemp_c'],"°C")
                    print("Average Temperature :: ", data['forecast']['forecastday'][i]['day']['avgtemp_c'],"°C")
                    print("Condition :: ", data['forecast']['forecastday'][i]['day']['condition']['text'])
                    print("UV Index :: ", data['forecast']['forecastday'][i]['day']['uv'])
                    print("Chances of Rain :: ", data['forecast']['forecastday'][i]['day']['daily_chance_of_rain'], "%")
                    print("Average Humidity :: ", data['forecast']['forecastday'][i]['day']['avghumidity'],"%")
                    print("Sunrise :: ", data['forecast']['forecastday'][i]['astro']['sunrise'])
                    print("Sunset :: ", data['forecast']['forecastday'][i]['astro']['sunset'])
                    print("\n\n")
                    print("-----------------------------------------------------------")
                break
            print("-----------------------------------------------------------")
            break
            
        elif(choice == 3):
            break

        else:
            print("\nInvalid Choice.")
            print("Please enter a valid option\n")

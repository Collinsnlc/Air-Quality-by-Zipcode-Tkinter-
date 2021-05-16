from tkinter import *
import requests
import json

root = Tk()
root.geometry('400x75')

def ziplookup():
    try:
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=6F33D29B-095C-4D7E-B1F5-6666FA32D929")
        api = json.loads(api_requests.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "yellow"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "orange"
        elif category == "Unhealthy":
            weather_color = "red"
        elif category == "Very Unhealthy":
            weather_color = "purple"
        elif category == "Hazardous":
            weather_color = "dark red"
        root.config(bg=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 15),
                        bg=weather_color)
        myLabel.pack()
    except Exception as e:
        api = "Error..."


# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75052&distance=5&API_KEY=6F33D29B-095C-4D7E-B1F5-6666FA32D929


zip = Entry(root)
zip.pack()

zipButton = Button(root,padx=20,text="Lookup Zipcode",command=ziplookup)
zipButton.pack()

root.mainloop()

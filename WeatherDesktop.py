from tkinter import *
import tkinter as tk
import requests
import pint

HEIGHT = 500
WIDTH = 500


def test_function(entry):
    print("This is the entry:", entry)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        if celcius_button:
            final_str = 'Place: %s \nWeather: %s \nTemperature: %s' % (name, desc, temp)


    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = 'aaeeccb8a4f15b1ade59473d076d57c9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


def get_weatherM(city):
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


weather = Tk()
weather.resizable(width=False, height=False)
weather.attributes('-toolwindow',True)
weather.title("tharki weather.py")

weather.geometry("200x200")
weather.config(bg="#7fe5f0")


entry = Entry(weather, font=10, fg="blue", bg="lime")
entry.pack(fill=X,ipadx=8,pady=10,padx=10)

frame_1 = Frame(weather,bg="#7fe5f0")
celcius_button = Button(frame_1, text="Celsius", font='arial 10 bold', command=lambda: get_weatherM(entry.get()))
celcius_button.pack(side=LEFT,padx=10,pady=10)
celcius_button.config(bg="#ff0067",fg="black")
frame_1.pack()

frame_2 = Frame(weather,bg="#7fe5f0")
label = Label(frame_2,bg="#7fe5f0",fg="#993399",font="15")
label.pack(side=LEFT,padx=10,pady=10)
frame_2.pack()

weather.mainloop()
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city=text1.get()

        geolocation=Nominatim(user_agent="my_weather_app_your_email@example.com")
        location=geolocation.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%I:%M %p")
        clock.config(text=currenttime)
        name.config(text="CURRENT WEATHER")

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7b66ccd847bede39cd5b31cd15422b94"
        jsondata=requests.get(api).json()
        condition=jsondata['weather'][0]['main']
        description=jsondata['weather'][0]['description']
        temp=int(jsondata['main']['temp']-273.15)
        pressure=jsondata['main']['pressure']
        humidity=jsondata['main']['humidity']
        wind=jsondata['wind']['speed']

        t.config(text=(temp,".C"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,".c"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")

        
searchimage=PhotoImage(file="searchim.png")
image=Label(image=searchimage)
image.place(x=20,y=20)

text1=tk.Entry(root,justify='left',width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
text1.place(x=50,y=40)
text1.focus()

searchicon=PhotoImage(file="searchicon.png")
imageicon=Button(image=searchicon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
imageicon.place(x=400,y=34)

logoimage=PhotoImage(file="logo.png")
logo=Label(image=logoimage)
logo.place(x=150,y=100)

frameimage=PhotoImage(file="box.png")
frame=Label(image=frameimage)
frame.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

Label1=Label(root,text="WIND",font=("Heletica",15,"bold"),fg="white",bg="#1ab5ef")
Label1.place(x=120,y=400)

Label2=Label(root,text="HUMIDITY",font=("Heletica",15,"bold"),fg="white",bg="#1ab5ef")
Label2.place(x=250,y=400)

Label3=Label(root,text="DESCRIPTION",font=("Heletica",15,"bold"),fg="white",bg="#1ab5ef")
Label3.place(x=430,y=400)

Label4=Label(root,text="PRESSURE",font=("Heletica",15,"bold"),fg="white",bg="#1ab5ef")
Label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)
root.mainloop()
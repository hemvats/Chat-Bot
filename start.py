import aiml
import os
import requests
import datetime

kernel = aiml.Kernel()

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

f= open("conversations/"+str(datetime.datetime.now())+".txt","w+")

# kernel now ready for use
while True:
	msg=raw_input("Enter your message>> ")
	if "weather" not in msg and "Weather" not in msg and "WEATHER" not in msg :
		str2 = str(kernel.respond(msg))
		print str2
		f.write("User:\t" + msg + "\n"+"Bot:\t"+ str2 + "\n")
	else :
		f.write("User:\t" + msg + "\n")
		api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
		f.write("Bot:\t" + "City Name :" + "\n")
		city = str(raw_input('City Name :'))
		f.write("User:\t"+ city + "\n")
		url = api_address + city
		json_data = requests.get(url).json()
		formatted_data = json_data['weather'][0]['main'] 
		h=json_data['main']['temp']
		a=h-275.15 
		str4=formatted_data+' '
		print("condition is " + str4)
		str3=str(a)
		print("temperature is " + str3)
		f.write("Bot:\t" + "condition is " + str4+ " and temperature is "+ str3 + "\n")
	f.flush()		
f.close()

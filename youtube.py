#Import the library
from pytube import YouTube

#Get the link
link = input("Enter the link: ") #enter your link

#Check the link is valid or not
try:
  yt = YouTube(link) 
except:
  print("Connection Error") #to handle exception

#Process the link to video
stream = yt.streams.first()

#Download the video
try:
  stream.download()
  print('Task Completed!')
except:
  print("Some Error!") #to handle exeption 



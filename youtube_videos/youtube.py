from pytube import YouTube 
link = input("Enter the link: ") #enter your link
try:
  yt = YouTube(link) 
except:
  print("Connection Error") #to handle exception
stream = yt.streams.first()
try:
  stream.download() 
except:
  print("Some Error!") #to handle exeption
print('Task Completed!') 



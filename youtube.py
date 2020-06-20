import youtube_dl
from os import path,system
import sys

def tui():
	print("\033[1;36;49m")
	channel=1;
	while (channel == int(1)): 
		link_of_the_video = input("URL of the YouTube video you want to download:- ") 
		output_name=input("Output filename : ")
		ydl_opts = {'outtmpl':str(output_name)} 
		links = link_of_the_video.strip() 
		with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
			ydl.download([links]) 
		system("ffmpeg -i "+output_name+".webm" + " "+output_name+".wav")
		system("lame "+output_name+".wav"+" "+output_name+".mp3")
		channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))

def help():
	print("\033[1;33;48m")
	print("""
		Usage: python3 youtube.py  [OPTION]... [FILE]...
	Download youtube video in a audio mp3 format.
	Mandatory arguments to long options are mandatory for short options too.
  	-t  or --tui            Running vpdownloader in tui format 
  	-f  or --file           Download all the videos mentioned in the file
  	-ff or --fileformat     Template for the file in -f format
  	-h, --help              For Help.
  		""")

def from_files(filename):
	print("\033[1;32;48m")
	if(path.exists(filename)):
		fp   = open(filename,"r+")
		for line in fp.readlines():
			try:
				line = line.split("\n")[0]
				details=line.split(",")
				print(details[0],":",details[1])
				ydl_opts = {'outtmpl':str(details[0])} 
				link = details[1].strip() 
				with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
					ydl.download([link])
				system("ffmpeg -i "+str(details[0])+".webm" + " "+str(details[0])+".wav")
				system("lame "+str(details[0])+".wav"+" "+str(details[0])+".mp3")
			except:
				print("Some Error Occured!")
		fp.close()
	else:
		print("Error : File Not Found")

def file_format():
	fp=open("demo.txt","r+")
	for line in fp.readlines():
		print(line)

try:
	arg=list(sys.argv)
	if(len(arg) > 3):
		print("More Arguments are passed then Required")
		exit(0)
	elif(len(arg)<2):
		print("vpdownloader works with options only , Refer python3 youtube.py --help to know more.")
	else:
		try:				
			if(arg[1]=="--help" or arg[1]=="-h"):
					help()
			elif(arg[1]=="--file" or arg[1]=="-f"):
				if(arg[2]!=''):
					from_files(arg[2])
				else:
					print("No file found")
			elif(arg[1]=='--tui' or arg[1]=='-t'):
				tui()
			elif(arg[1]=="--fileformat" or arg[1]=="-ff"):
				file_format()
			else:
				print("No such option supported")
		except Exception as e:
			print("Check options wisely")
except KeyboardInterrupt:
	print("User Interuptted the process")
except Exception:
	print("Some Error Occured!") 

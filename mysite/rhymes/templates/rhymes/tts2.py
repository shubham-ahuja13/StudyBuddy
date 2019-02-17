# Python program to convert 
# text to speech 

# import the required module from text to speech conversion 
import win32com.client 

# Calling the Disptach method of the module which 
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 

speaker = win32com.client.Dispatch("SAPI.SpVoice")  

def tts():
	print("Enter the word you want to speak it out by computer") 
	s = input() 
	audio = speaker.Speak(s)
	return audio

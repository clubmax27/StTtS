from gtts import gTTS
import os
import sys
import time
from pygame import mixer
import speech_recognition as sr
import keyboard

def speak(text):
	tts = gTTS(text=text, lang='en-US')

	path = root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
	filename = "abc.mp3"
	path = os.path.join(root_dir, filename)

	tts.save(path) #Save mp3 file

	mixer.init()
	mixer.music.load(path)
	mixer.music.play() #Play the mp3 file

	while mixer.music.get_busy():  #Wait for music to finish playing
		time.sleep(0.1)

	mixer.music.unload() #Unload music to delete the file, or else it thows an error
	os.remove(path)


r = sr.Recognizer()
MicrophoneList = sr.Microphone.list_microphone_names()
for i in range(len(MicrophoneList)):
	print("{0} : {1}".format(i, MicrophoneList[i]))

MicrophoneId = input("Rentrez votre ID de Microphone : ")
Microphone = sr.Microphone(device_index=int(MicrophoneId))

Key = input("Quelle touche du clavier active la reconaissance vocale : ")

while True:  # making a loop
	try:  # used try so that if user pressed other than the given key error will not be shown
		if keyboard.is_pressed(Key):  # if key 'q' is pressed 
			with Microphone as source: 
				r.adjust_for_ambient_noise(source)
				print("Speak!")
				audio_data = r.listen(source) #Get the voice of the user

			result = r.recognize_google(audio_data, language='en-US') #Send the voice to google, and get text result (might throw a UnknownValueError exception)
			print (">", result)
			print("\n")
			speak(result) 
	except sr.UnknownValueError: #If google doesn't recognize speach
		print("Google n'a pas reconnu ce que vous avez dit, désolé \n")

	except: #Should never happen ...
		print()
		print("Oops!", sys.exc_info()[0], "occurred.")
		temp = input("Press enter to exit ....")
		break
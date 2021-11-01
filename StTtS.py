from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import keyboard

def speak(text):
    tts = gTTS(text=text, lang='fr')

    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


r = sr.Recognizer()
MicrophoneList = sr.Microphone.list_microphone_names()
for i in range(len(MicrophoneList)):
	print("{0} : {1}".format(i, MicrophoneList[i]))

MicrophoneId = input("Rentez votre ID de Microphone : ")
Microphone = sr.Microphone(device_index=int(MicrophoneId))

Key = input("Quelle touche du clavier active la reconaissance vocale : ")

while True:  # making a loop
	try:  # used try so that if user pressed other than the given key error will not be shown
		if keyboard.is_pressed(Key):  # if key 'q' is pressed 
			with Microphone as source:
				print("Speak!")
				audio_data = r.listen(source)
			result = r.recognize_google(audio_data, language="fr-FR")
			print (">", result)
			print("\n")
			speak(result)
	except:
		break
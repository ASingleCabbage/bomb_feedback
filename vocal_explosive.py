import speech_recognition as sr
import simpleaudio as sa
import requests

#Sample rate is how often values are recorded
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data)
#here.
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
#Initialize the recognizer
r = sr.Recognizer()

#generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()
print("Detected {} devices {}".format(len(mic_list), mic_list))

#the following loop aims to set the device ID of the mic that
#we specifically want to use to avoid ambiguity.
print("Now we will show you a list of audio input devices; select the one that looks most like your microphone...")
for i, microphone_name in enumerate(mic_list):
    resp = input("Is {} your microphone? [y/n] ".format(microphone_name))
    if resp == 'y':
        device_id = i
        break

def explode_bomb():
    print("explode bomb")
    r = requests.post('https://bomb-explodey.herokuapp.com/explode', json = {"action":"explode"})
    print(r.text)

def listen_mode(mic_source):
	wave_obj = sa.WaveObject.from_wave_file('ding.wav')
	play_obj = wave_obj.play()

	audio = r.listen(mic_source, phrase_time_limit = 3, timeout = 3)
	try:
		text = r.recognize_google(audio)
		print("[LISTEN]: " + text)
		if text == "explode bomb":
			explode_bomb()

	except sr.UnknownValueError:
		print("[LISTEN] Google Speech Recognition could not understand audio")

	except sr.RequestError as e:
		print("[LISTEN] Could not request results from Google Speech Recognition service; {0}".format(e))

	except sr.WaitTimeoutError:
		print("[LISTEN] TIMEOUT")


#use the microphone as source for input. Here, we also specify
#which device ID to specifically look for incase the microphone
#is not working, an error will pop up saying "device_id undefined"
with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
						chunk_size = chunk_size) as source:
	#wait for a second to let the recognizer adjust the
	#energy threshold based on the surrounding noise level
	r.adjust_for_ambient_noise(source)
	while True:
		print("Say Something")
		#listens for the user's input
		audio = r.listen(source, phrase_time_limit = 2)

		try:
			text = r.recognize_google(audio)
			print("you said: " + text)
			if text == 'OK Google':
				print("Entering listen mode")
				listen_mode(source)
				print("Exiting listen mode")

		#error occurs when google could not understand what was said

		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")

		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))

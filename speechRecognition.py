import speech_recognition as sr

recognizer = sr.Recognizer()

def audio_to_text():
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

if __name__ == "__main__":
    result = audio_to_text()
    if result:
        print(f"Transcribed Text: {result}")

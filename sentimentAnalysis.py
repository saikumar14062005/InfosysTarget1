import speech_recognition as sr
from textblob import TextBlob
import streamlit as st

recognizer = sr.Recognizer()

def audio_to_text():
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            st.info("Recognizing...")
            
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            st.error("Timeout: No speech detected.")
            return None
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
            return None

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity  
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, sentiment_score

def main():
    st.title("Speech-to-Text with Sentiment Analysis")

    st.write("Click the button below to start recording your voice:")
    if st.button("Record Audio"):
        st.write("Recording... Please speak!")
        result = audio_to_text()
        if result:
            st.success(f"Transcribed Text: {result}")

            sentiment, score = analyze_sentiment(result)
            st.write(f"Sentiment: **{sentiment}**")
            st.write(f"Sentiment Score: **{score:.2f}**")
        else:
            st.warning("No speech was detected. Please try again.")

if __name__ == "__main__":
    main()

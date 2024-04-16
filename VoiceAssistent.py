import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Sorry, I could not understand that.")
            return None

def main():
    speak("Hello! How can I help you today?")
    while True:
        query = listen()

        if query is not None:
            query = query.lower()

            if 'time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")

            elif 'search' in query:
                speak("What would you like me to search on Wikipedia?")
                search_query = listen()
                if search_query:
                    try:
                        result = wikipedia.summary(search_query, sentences=2)
                        speak(f"According to Wikipedia, {result}")
                    except wikipedia.exceptions.PageError:
                        speak("Sorry, I could not find any information.")
                    except wikipedia.exceptions.DisambiguationError:
                        speak("There are multiple matching results. Please be more specific.")

            elif 'open' in query:
                speak("Sure, which website would you like me to open?")
                website = listen()
                if website:
                    url = f"https://{website.lower()}.com"
                    webbrowser.open(url)
                    speak(f"Opening {website}")

            elif 'exit' in query or 'quit' in query:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()

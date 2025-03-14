import speech_recognition as sr
import webbrowser
import pyttsx3
import requests  # For making HTTP requests
import muscilibrary  # Your music library

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set your DeepSeek API key
DEEPSEEK_API_KEY = "sk-12c4dae428d54d22a8fc4d914cadf0a0"  # Replace with your actual DeepSeek API key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/completions"  # Replace with the actual DeepSeek API endpoint

# Function to convert text to speech
def speech(text):
    engine.say(text)
    engine.runAndWait()

# Function to process commands
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = muscilibrary.music[song]
        webbrowser.open(link)
    else:
        # If the command is not a URL, treat it as a question for DeepSeek
        answer = ask_deepseek(c)
        speech(answer)

# Function to ask DeepSeek API
def ask_deepseek(question):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": question,  # The question you want to ask
        "max_tokens": 50  # Limit the response length
    }
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get('choices', [{}])[0].get('text', 'Sorry, I could not find an answer.')
        else:
            return f"Failed to get an answer. API error: {response.status_code}"
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

# Main function
if __name__ == "__main__":
    speech("Initializing Jarvis")
    while True:
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)

            if "jarvis" in word.lower():
                speech("Yes")
                with sr.Microphone() as source:
                    print("Jarvis activated!")
                    speech("Just order me sir, I am ready to comply")
                    audio = r.listen(source, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(command)
                    processcommand(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"Error: {e}")
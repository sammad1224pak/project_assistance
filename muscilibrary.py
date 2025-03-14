music = {
    "stealth": "https://www.youtube.com/watch?v=U47Tr9BB_wE",
    "march": "https://www.youtube.com/watch?v=Xqeq4b5u_Xw",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D",
    "wolf": "https://www.youtube.com/watch?v=ThCH0U6aJpU&list=PLnrGi_-oOR6wm0Vi-1OsiLiV5ePSPs9oF&index=21"
}
'''import speech_recognition as sr
import webbrowser
import pyttsx3 # text to speech 
import muscilibrary# my page

r= sr.Recognizer()# eak class ha jo speech recoginition functionality lena me help krti ha
engine = pyttsx3.init() # isa pttsx initialize hogay ga

def speech(text):# function define kiya ha
    engine.say(text)
    engine.runAndWait()
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

if __name__ == "__main__":
     speech("initializing jarvis")
     while True:
                 # recognize speech 
       print("recognizing")
       try:
             r = sr.Recognizer()
             with sr.Microphone() as source:
              print("listning!")
              audio = r.listen(source, timeout=2,phrase_time_limit=2)#sunna ha 
             word=r.recognize_google(audio)# recoganize krna ha 
             print(word)

             if "jarvis" in word.lower():
                 speech("ya")
                 with sr.Microphone() as source:
                  print("jarvas activated!")
                  speech("just order me sir am ready to comply")
                  audio = r.listen(source,phrase_time_limit=2)
                  command=r.recognize_google(audio)
                  print(command)
                  processcommand(command)
                  
                 
             
       except sr.UnknownValueError:
            print("could not understand audio")
       except Exception as e:
          print(" error".format(e))
 


   
 

'''
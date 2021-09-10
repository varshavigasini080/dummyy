import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Whom do you wanna know about?")
        audio = r.listen(source)
        print("Recognizing Now .... ")
        try:
            print("{} is a great person. {} inspires us every day.".format(r.recognize_google(audio),r.recognize_google(audio)))
           
        except Exception as e:
            print("Error :  " + str(e))

        
       
if __name__ == "__main__":
    main()
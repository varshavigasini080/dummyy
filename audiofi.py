import speech_recognition as sr 

def main():
    sound="recorded.wav"
    r=sr.Recognizer()
    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print("Converting Audio into Text.........")
        audio=r.listen(source) 
    try:
        print("Content of the audio is:\n"+str(r.recognize_google(audio)).capitalize())
    except Exception as e:
        print("ERROR: "+e)

if __name__ == "__main__":
    main()
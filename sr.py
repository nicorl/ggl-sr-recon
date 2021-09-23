import speech_recognition as sr
 
def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Habla")
 
        audio = r.listen(source)
 
        print("reconociendo .... ")
 
 
        # Metemos el sistema de Google de reconocimiento de voz
 
        try:
            print("Has dicho \n" + r.recognize_google(audio, language="es-ES"))
            print("Audio registrado correctamente \n ")
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
 
 
 
        # Escribe el audio en un fichero
        with open("audio.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
 
if __name__ == "__main__":
    main()
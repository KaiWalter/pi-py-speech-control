import speech_recognition as sr

r = sr.Recognizer()

running = True

while running:

    with sr.Microphone() as source:
        print("COMMAND>")
        audio = r.listen(source)

    command_text = None

    try:
        command_text = r.recognize_google(audio)
        print(f'received [{command_text}]')
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))


    if command_text == "exit":
        running = False


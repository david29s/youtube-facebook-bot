import speech_recognition as spch

record = spch.Recognizer()


if input(str()) == 'go':
    with spch.Microphone() as voice_source:
        print('Start recording...')
        audio = record.listen(voice_source)

        result_text = record.recognize_google(audio)

    try:
        print(result_text)
    except:
        pass


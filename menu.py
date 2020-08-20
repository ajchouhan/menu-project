import os
import pyttsx3
import pywhatkit as pwk
import datetime
i = 1
while i > 0:
    pyttsx3.speak('please tell me how can i help u')
    print('please tell me how can i help you : ', end='')
    a = input()
    if ('do not'in a or 'not'in a or 'does not'in a or 'not open'in a):
        pyttsx3.speak("as follows your cammends")
    else:
        if ('run' in a or 'open' in a) and ('chrome' in a or 'browser' in a or 'google' in a):
            pyttsx3.speak('   opening chrome browser for you')
            os.system('chrome')

        elif (
                'who are you' in a or 'what is your name ' in a or 'tell me about your self' in a or 'tell me about you ' in a or 'introduce yourself' in a):
            pyttsx3.speak('my name is Ajay and i am here to help you in doing any task you can ask anything from me .')
        elif ('run' in a or 'open' in a) and ('notepad' in a or 'text editor' in a):
            pyttsx3.speak('   opening notepad for u')
            os.system('notepad')
        elif ('run' in a or 'open' in a) and ('microsoft edge' in a or 'microsoft browser' in a):
            pyttsx3.speak('   opening microsoft edge  for u')
            os.system('msedge')
        elif ('run' in a or 'open' in a) and ('whatsapp' in a or 'whats app' in a):
            pyttsx3.speak('   opening whatsapp  for u')
            os.system('chrome whatsapp.com')
        elif ('run' in a or 'open' in a) and ('telegram' in a):
            pyttsx3.speak('  opening telegram  for u')
            os.system('chrome telegram.com')
        elif ('run' in a or 'open' in a) and ('instragram' in a or 'instra' in a):
            pyttsx3.speak('  opening instragram  for u')
            os.system('chrome instragram.com')
        elif ('run' in a or 'open' in a) and ('calculater' in a or 'calsi' in a):
            pyttsx3.speak('  opening calculater  for u')
            os.system('chrome https://www.calculator.net/')
        elif ('run' in a or 'open' in a) and ('zoom' in a):
            pyttsx3.speak('   opening zoom  for u')
            os.system('chrome zoom.us')
        elif ('exit' in a or 'close' in a):
            pyttsx3.speak('  closing program')
            break
        elif ('run' in a or 'open' in a) and ('windows media player' in a):
            pyttsx3.speak('  opening windows media player  for u')
            os.system('wmplayer')
        elif ('run' in a or 'open' in a) and ('vlc media player' in a or 'media player' in a or 'vlc' in a):
            pyttsx3.speak('  opening vlc media player  for u')
            os.system('vlc')
        elif ('run' in a or 'open' in a) and ('control panel' in a):
            pyttsx3.speak('  opening control panel  for u')
            os.system('control panel')
        elif ('run' in a or 'open' in a) and ('facebook' in a or 'fb' in a):
            pyttsx3.speak('  opening facebook  for u')
            os.system('chrome facebook.com')
        elif ('run' in a or 'open' in a) and ('youtube' in a or 'youtube.com' in a):
            pyttsx3.speak('  opening youtube for u')
            os.system('chrome youtube.com')
        elif ('play a video' in a or 'open a video' in a or 'play video' in a or 'open video' in a):
            pyttsx3.speak('  which video do u want to play')
            video = input('which video do u want to play : ')
            pyttsx3.speak('  playing video for u')
            pwk.playonyt(video)
        elif ('send' in a or 'text' in a) and (
                'whatsapp message ' in a or 'message by whatsapp' in a or 'message from whatsapp' in a or 'message' in a):
            z = datetime.datetime.today()
            pyttsx3.speak('  plzz enter contect number ')
            contect = input('plz inter contect number : ')
            pyttsx3.speak('  plzz enter message to be sent ')
            msg = input('plz inter message to be sent : ')
            pwk.sendwhatmsg('+91' + contect, msg, z.hour, z.minute + 2)

        elif ('search' in a or 'browse' in a):
            pyttsx3.speak('  plzz tell me what do you want to search ')
            browse = input('what do u want to search : ')
            pyttsx3.speak('searching' + browse + 'on google')
            pwk.search(browse)
        elif ('tell' in a or 'speak' in a):
            pyttsx3.speak('  plzz tell me the topic ')
            topic = input('enter a topic : ')
            speach = pwk.info(topic, 5)
            pyttsx3.speak(speach)
        elif ('date' in a or 'dinak' in a):
            pd = datetime.date.today()
            pyttsx3.speak(pd)
            print(pd)
        elif ('shutdown' in a):
            pyttsx3.speak('closing window')
            print('closing window! in 30 second')
            pwk.shutdown(30)
        elif ('open'in a or 'run'in a) and ('google maps'in a or 'maps'in a):
            pyttsx3.speak('opening google maps')
            os.system('chrome https://www.google.com/maps/@23.2664042,77.4357627,15z')
        elif ('open'in a or 'run'in a or 'today'in a) and ('today weather'in a or ' weather'in a or 'weather report'in a):
            pyttsx3.speak('opening weather report')
            os.system('chrome https://www.google.com/search?q=today+weather&rlz=1C1CHBF_enIN912IN912&oq=today+we&aqs=chrome.1.69i57j0l7.9358j0j7&sourceid=chrome&ie=UTF-8')
        elif ('open'in a or 'run'in a ) and ('amazon.com' in a or 'amazon.in'in a or 'shoping web site' in a or 'shoping site'in a):
            pyttsx3.speak('opening amazon')
            os.system('chrome https://www.amazon.in/ ')
        elif ('open'in a or 'run'in a or 'play'in a) and ('music'in a or 'play music'in a or 'song'in a):
            pyttsx3.speak('playing music for you')
            os.system('chrome https://www.youtube.com/watch?v=E2DPzcMGvKo')
        elif ('hi'in a or 'hello'in a):
            pyttsx3.speak('hello sir wellcome you please assign a task')
            print('hello sir wellcome you please assign a task')
        else:
            pyttsx3.speak(
                'sorry sir i am not able to understand what do you want.  type exit or close to leave the program !')
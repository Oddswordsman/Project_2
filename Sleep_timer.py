#pip install pycaw
#PYTHON CORE AUDIO WINDOWS LIBRARY

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time

sessions = AudioUtilities.GetAllSessions()
print("""***Please Note this python program will not CLOSE your music application 
or STOP the song or video, instead it will just decrease the 
Master Volume until it gets mute and the best thing is that you can 
always unmute the music at anytime after it gets mute***""")
print()
print()


while True:
    application= str(input("Write name of application on which music is playing.(for e.g. - chrome.exe, vlc.exe) = "))
    sleeptime = int(input("""**Minimum time should be 15 seconds**
Time(in seconds) : """))
#    waketime = int(input("After how much time do you want your music "))

    if sleeptime > 14:
        break
    else:
        print("Minimum time should be 15 seconds. Please recheck the input.")

#volume_value = 1


def sleep_timer(name_of_application,volume_value=1):
    while True:
        for session in sessions:
            if session.Process and session.Process.name() == name_of_application:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)

            #    print(volume.GetMasterVolume())
                volume.SetMasterVolume(volume_value,None)
                
        time.sleep(2)
        volume_value -= 0.2

        if volume_value < 0:
            break

def reset_sleep_timer(name_of_application):
        
    while True:
        for session in sessions:
            if session.Process and session.Process.name() == name_of_application:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)

            #    print(volume.GetMasterVolume())
                volume.SetMasterVolume(1,None)
                
        break    

time.sleep(sleeptime-14)

sleep_timer(application)

#input("Press 'Enter' to normalize the master volume of your music player.")
input("Press any key to normalize the master volume of your music player.")


reset_sleep_timer(application)

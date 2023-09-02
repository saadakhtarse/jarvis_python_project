from Body.Speak import Speak
import os
            
# dir_path = os.path.dirname(os.path.realpath(__file__))
def music_search(query):
    dir_path = os.path.dirname(os.path.abspath("C:/JARVIS/Data/music"))

    # name = query.replace('play me a song',"")
    name = query.replace('play song ',"")
    name = query.replace('play music ',"")
    name = query.replace('play me a song ',"")
    name = query.replace('play me a music ',"")

    print(f"Song name: {name.title()}")
    for root, dirs, files in os.walk(dir_path): # root = C:\JARVIS\Data\music ,  files are all fileNames , 
        for file in files:                      # files have each file
            # change the extension from '.mp3' to
            # the one of your choice.
            
            if (name.title() in file and file.endswith('.mp3')):
                print ("-> File Found: "+ root + '/' + str(file))
                os.startfile(os.path.join(root, file))
                Speak("playing music for you...")

        else:
            print("File not found!")
            print(file)


def music_search_demo(query):
    dir_path = os.path.dirname(os.path.abspath("C:/JARVIS/Data/music"))

    # name = query.replace('play me a song',"")
    name = query.replace('play song ',"")
    name = query.replace('play music ',"")
    name = query.replace('play me a song ',"")
    name = query.replace('play me a music ',"")

    print(f"Song name: {name.title()}")
    for root, dirs, files in os.walk(dir_path): # root = C:\JARVIS\Data\music ,  files are all fileNames , 
        for file in files:                      # files have each file
            # change the extension from '.mp3' to
            # the one of your choice.
            
            os.startfile(os.path.join(root, file)) #Will run first sing (FOR DEMO)

            # if (name.title() in file and file.endswith('.mp3')):
            #     print ("-> File Found: "+ root + '/' + str(file))
            #     os.startfile(os.path.join(root, file))
            #     Speak("playing music for you...")

        # else:
        #     print("File not found!")
        #     print(file)

# music_search("Shape Of You")

from googletrans import Translator
import speech_recognition as sr

# PROBLEM & SOLUTION
# Make a class of take_command, not function, make class. 
# Then make language its veriable
# problem was, if i set Language in Take_Command.py, i have to use :anguage as a peramter
# - when ever i have to call take_command()
#  
def take_command(language): #listeninig...
    # take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 0.5 #less the number, more it hears
        audio = r.listen(source,0,6) # 0,6 means cut and listen after every 6 SECONDS 
    
    try:
        print('Recognizing...')
        if language == "hin":
            query = r.recognize_google(audio, language='hi-In') #for Hindi
            query = Translate_urdu_hindi_into_eng(query)
        else:
            query = r.recognize_google(audio, language='eng-in') #for English
            print(f'Me:"{str(query)}"\n')
    except Exception as e:
        # print(e) #show full error
        print("Say that again please...")
        return "None"
    return query


def Translate_urdu_hindi_into_eng(text):
    line = str(text)
    translator = Translator()
    result = translator.translate(line)
    data = result.text
    
    print(f"ME(Urdu/Hindi->English): {data}.")
    return data
    
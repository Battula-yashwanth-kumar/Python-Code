#pip install pywin32
#pip install pywin32

import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("You are my best friend")
    url="https://newsapi.org/v2"
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts= news_dict['article']
    for article in arts:
        speak(article['title'])
        speak(article['content'])
        speak("moving on to next news")
    speak("Thanks for listenign to news")

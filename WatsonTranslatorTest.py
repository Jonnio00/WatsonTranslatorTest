import json
from typing import Text
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from requests.models import Response

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    This function takes english text and returns french translation
    """
    
    result = language_translator.translate(text= englishText, model_id="en-fr").get_result()

    frenchText = result["translations"][0]["translation"]

    print(frenchText)

    return frenchText
     
    

englishToFrench("Hello my name is Terje")

def frenchToEnglish(frenchText):
    """
    This function takes english text and returns french translation
    """

    result = language_translator.translate(text= frenchText, model_id="fr-en").get_result()
    
    englishText = result["translations"][0]["translation"]

    print(englishText)

    return englishText
    
frenchToEnglish("Bonjour mon ami")
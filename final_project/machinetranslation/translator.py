'''
Translator class
'''
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Translate english to french'''
    french_text = language_translator.translate(english_text, model_id=('en-fr'))

    return french_text.result['translations'][0]['translation']

def french_to_english(french_text):
    '''Translate french to english'''
    english_text = language_translator.translate(french_text, model_id=('fr-en'))

    return english_text.result['translations'][0]['translation']

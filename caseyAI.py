import os
import openai
import setup


openai.api_key = os.getenv(setup.AIAPIKEY)

response = openai.Completion.create(
    model = "gpt-3.5-turbo",
    
)
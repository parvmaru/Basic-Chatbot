# -*- coding: utf-8 -*-
"""Chattbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13ebZNX8KrL_ZKkOTzF46_YBopyM3Viw4
"""

from nltk.chat import Chat, reflections
import numpy as np
import random
import string # to process standard python strings



pairs = [
         ['my name is (.*)', ['hi %1,How are you today']],
         ['(hi|hello|hey|holla|hola)', ['Hey there', 'hi there', 'Heyyy']],
         ['(.*)(location|city) ?', 'Mumbai,Pune,Delhi,Maharashtra,Jammu Kashmir'],
         ['how is the weather in (.*)', ['The weather in %1 is amazing like always']],
         ['(.*)who created you ?', ['Parv Maru did using NLTK']],
         ['(.*)help(.*)', ['I can help you']],
         ['(.*) your name ?', ['my name is JARVIS']],
         ['(.*)How is your day ?', ['Good(:']],
         ['I am an  (.*)', ['Good to know that you are %1, Is there anything I can help you with', 'What  profile are you looking for Developer,Tester Support,Data Scientist']],
         ['I want to (.*)', ['You have to choose one of the role out of following \n 1.Developer \n 2.Tester \n 3.Support Functions \n 4.Data Scientist \n 5.Android Developer \n 6.IOS developer']],
         ['(.*) role', ['Why do you think you are so sure to take up %1 role as it is required lot of effort to put in.']],
         ['(help|suggestion|advise)(.*)', ['You need my %1 ,Please tell me how can I %1 you']],
         ['quit', ['Bye have a nice day ahead and take care']],
         ['I love (.*)', ['Its great, we should do what we love']],
         ['(.*)is my favorite subject',['%1 is an interesting subject to learn']]
      


         
         
        
        




]

reflections

my_dummy_reflections = {
    'go' : 'gone', 
    'Hello' : 'Hey there'
}

chat = Chat(pairs, reflections)
chat.converse()
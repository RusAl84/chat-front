
# text = "Красивая мама красиво мыла раму"
# m = Mystem()
# lemmas = m.lemmatize(text)
# print(''.join(lemmas))
# -*- coding: utf-8 -*-
#from importlib import reload
#import sys
#reload(sys)
#import locale
#locale.getpreferredencoding()
from pymystem3 import Mystem
with open("123.txt", encoding='utf-8') as file:
    text = file.read()
    m = Mystem()
    lemmas = m.lemmatize(text)
    #print(''.join(lemmas))
    text2 = ''.join(lemmas)
print(text2)
f = open("new123.txt", 'w', encoding='utf-8')
f.write(text2)
f.close()

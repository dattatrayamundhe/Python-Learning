#pip install googletrans==3.1.0a0 
#(translator[https://py-googletrans.readthedocs.io/en/latest/])

from googletrans import Translator
translator=Translator()
out=translator.translate("Hello! datta you are doing well keep it up",dest="hi")
print(out.text)


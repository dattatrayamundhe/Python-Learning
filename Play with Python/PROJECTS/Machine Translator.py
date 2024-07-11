#import the package
from googletrans import Translator

# Store some text for translation in french language
text = ''' For often, when on my couch I lie
In a vacant or pensive mood,
They blink on that inner eye
What is the happiness of solitude;
And then my heart fills with pleasure,
And dance with the daffodils.  '''

# Create an instance of Translator to use
translator = Translator()

# detect the language
lang = translator.detect(text)
print(lang)
print(' ')

# Call the translate()
translated = translator.translate(text, dest = 'mr')

#print the result
print(translated.text)

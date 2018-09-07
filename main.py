from googletrans import Translator
import random

t = Translator()
languages = ["fr","ja","ko", "so", "Arabic", "Czech"]

iterations = 15

message = input("> ")

current_translation = message
english_version = message

for i in range(iterations):
    language = random.choice(languages)
    print(language)

    current_translation = t.translate(current_translation, dest=language).text
    english_version = t.translate(current_translation, dest='en').text

    print("==========")
    print("Translating into %s:" %(language))
    print(current_translation)
    print("In English:")
    print(english_version)


print("\n\n\n")
print("Finished Translating!")
print(english_version)

import requests
from bs4 import BeautifulSoup

# Send GET request to website
url = "https://www.dictionary.com/e/word-of-the-day/"
response = requests.get(url)

# print(response)

# Create BeatifulSoup object with the response content

wotd_html = BeautifulSoup(response.content, "html.parser")

# Find the word of the day
word = wotd_html.find(class_="otd-item-headword__word").text.strip()

# Find the type of word
word_type = wotd_html.find(class_="luna-pos").get_text()
# Find the pronunciation
pronunciation = wotd_html.find(class_="otd-item-headword__pronunciation").text.strip()

# Find the definition
definition = wotd_html.find(class_="otd-item-headword__pos").find_all("p")[1].get_text()

# split the response of pronunciation into phonetic and IPA
lines = pronunciation.split("\n")
phonetic = lines[0]
IPA = lines[2]


# Print the extracted information
print("Word of the Day:", word)
print("Type of Word:", word_type)
print(phonetic + IPA)
print("Definition:", definition)

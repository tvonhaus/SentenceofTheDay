import requests
from bs4 import BeautifulSoup

# Send GET request to website
url = "https://www.merriam-webster.com/word-of-the-day"
response = requests.get(url)

print(response)

# Create BeatifulSoup object with the response content

wotd_response = BeautifulSoup(response.content, "html.parser")

# print(wotd_response)
# Find the Word of the Day
word = wotd_response.find(class_="word-header-txt").get_text()
# Find word attribute
word_attr = wotd_response.find(class_="main-attr").get_text()
# Find word pronunciation
word_pronunciation = wotd_response.find(class_="word-syllables").get_text()

# Find word definition
word_definition = (
    wotd_response.find(class_="wod-definition-container").find("p").get_text()
)

# Find example sentence of the wotd
word_example = (
    wotd_response.find(class_="wod-definition-container").find_all("p")[1].get_text()
)

entry_division = wotd_response.find(class_="wod-definition-container").find_all("p")[2]
link = entry_division.find("a")
if link:
    entry_url = link["href"]
    print(f"Entry URL: {entry_url}")
else:
    print("Entry link not found.")


print("Word of the day:", word)
print(word_attr)
print("Pronunciation:", word_pronunciation)
print("Definition:", word_definition)
print("Example Sentence:", word_example)
print("Entry URL:", entry_url)


# Send a GET request to the entry URL
entry_response = requests.get(entry_url)

# Create a BeautifulSoup object from the entry response content
entry_soup = BeautifulSoup(entry_response.content, "html.parser")
print(entry_soup)

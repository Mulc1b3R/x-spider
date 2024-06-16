import requests

url = "https://www.virus.com/danger.html"

response = requests.get(url)

if response.status_code == 200:
    with open("webpage_source.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Webpage source saved to webpage_source.txt")
else:
    print("Failed to retrieve the page source. Status Code:", response.status_code)
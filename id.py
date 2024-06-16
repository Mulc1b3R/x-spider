import requests
from bs4 import BeautifulSoup

url = "https://zerohedge.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all anchor tags that contain 'details' in href attribute
    identifiers = [a['href'].split('/')[-1] for a in soup.find_all('a', href=True) if 'details' in a['href']]
    
    if identifiers:
        # Print the list of identifiers
        print("List of Identifiers:")
        for identifier in identifiers:
            print(identifier)
        
        # Save the list to a text file
        with open("identifier_list.txt", "w") as file:
            for identifier in identifiers:
                file.write(identifier + "\n")
            
        print("Identifiers saved to identifier_list.txt")
    else:
        print("No identifiers found on the page.")
        
else:
    print("Error fetching directory listing. Status code:", response.status_code)
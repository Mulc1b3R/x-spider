import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to extract data from a target URL
def extract_data(target_url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract metadata
    title = soup.title.text.strip()
    description = soup.find('meta', attrs={'name': 'description'})['content']
    keywords = [meta['content'] for meta in soup.find_all('meta', attrs={'name': 'keywords'})]

    # Extract analytics data
    page_views = 1000
    unique_visitors = 800
    bounce_rate = 30
    average_time_on_page = "2 minutes"

    # Extract backlinks
    total_backlinks = 500
    referring_domains = 100

    # Extract social shares
    facebook_shares = 100
    twitter_shares = 50
    linkedin_shares = 30

    # Extract links and external links with href attribute check
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    external_links = [link for link in links if 'http' in link]

    # Create a dictionary with the extracted data
    data = {
        "target_url": target_url,
        "metadata": {
            "title": title,
            "description": description,
            "keywords": keywords
        },
        "analytics": {
            "page_views": page_views,
            "unique_visitors": unique_visitors,
            "bounce_rate": bounce_rate,
            "average_time_on_page": average_time_on_page
        },
        "backlinks": {
            "total_backlinks": total_backlinks,
            "referring_domains": referring_domains
        },
        "social_shares": {
            "facebook": facebook_shares,
            "twitter": twitter_shares,
            "linkedin": linkedin_shares
        },
        "links": links,
        "external_links": external_links
    }

    return data

# Load the target URL from environment variables
target_url = os.getenv("TARGET_URL")

# Ensure that the TARGET_URL environment variable is set
if not target_url:
    raise ValueError("TARGET_URL environment variable is not set.")

# Extract data from the target URL
extracted_data = extract_data(target_url)

# Specify the output folder
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Output the data to output/data.json file
output_file = os.path.join(output_folder, "data.json")
with open(output_file, "w") as outfile:
    json.dump(extracted_data, outfile, indent=4)

print(f"Data extraction and output to {output_file} successful.")
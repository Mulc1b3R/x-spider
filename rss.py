import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to download RSS feed from a target URL
def download_rss_feed(target_url):
    response = requests.get(target_url)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download RSS feed from {target_url}")

# Load the target URL from environment variables or specify it here
target_url = os.getenv("TARGET_URL")

# Ensure that the TARGET_URL environment variable is set
if not target_url:
    target_url = "https://cms.zerohedge.com/fullrss2.xml"  # Provide the RSS feed URL here if not set in environment variables

# Download the RSS feed
rss_feed = download_rss_feed(target_url)

# Create the output folder if it doesn't exist
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Save the RSS feed to a file in the output folder
output_file = os.path.join(output_folder, "feed.xml")
with open(output_file, "wb") as file:
    file.write(rss_feed)

print(f"RSS feed downloaded and saved to {output_file}")
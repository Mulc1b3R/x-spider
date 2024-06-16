import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the target URL from environment variables
target_url = os.getenv("TARGET_URL")

if not target_url:
    raise ValueError("TARGET_URL environment variable is not set.")

response = requests.get(target_url)

if response.status_code == 200:
    # Create the output directory if it doesn't exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Save the HTML content to a file
    output_file = os.path.join(output_folder, "directory_listing.html")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print("HTML content saved to directory_listing.html")
else:
    print("Error fetching directory listing. Status code:", response.status_code)
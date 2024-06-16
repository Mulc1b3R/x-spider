import requests
from bs4 import BeautifulSoup
import json

# Function to extract comments data from an article URL that contain 'commentId='
def extract_comments_data(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section containing comments
    comments_section = soup.find('div', class_='comments-section')

    # Extract comments data containing 'commentId='
    comments_data = []
    if comments_section:
        comments = comments_section.find_all('div', class_='comment')
        for comment in comments:
            comment_text = comment.find('p', class_='comment-text').text.strip()
            commenter = comment.find('span', class_='commenter-name').text.strip()
            if 'commentId=' in comment_text:
                comments_data.append({
                    'comment_text': comment_text,
                    'commenter': commenter
                })

    return comments_data

# Set the URL of the article for which to extract comments data
article_url = 'https://zerohedge.com/markets/goldmans-weapons-choice-noisy-summer'  # Update with the correct article URL

# Extract comments data from the article URL containing 'commentId='
comments_data = extract_comments_data(article_url)

# Save the filtered comments data to a JSON file
output_file = 'output/filtered_comments_data.json'
with open(output_file, 'w') as outfile:
    json.dump(comments_data, outfile, indent=4)

print(f"Filtered comments data containing 'commentId=' extracted and saved to {output_file}")
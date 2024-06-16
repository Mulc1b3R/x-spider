import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to extract text content from URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text_content

# Function to save text to a text file
def save_text_to_file(text_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text_content)

# Function to generate word cloud from text
def generate_word_cloud(text_content):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_content)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Target URL
target_url = 'https://www.zerohedge.com/'
# Output filename for text file
output_txt_file = 'output/extracted_text.txt'

# Extract text content from URL
text_content = extract_text_from_url(target_url)

# Save text content to a text file
save_text_to_file(text_content, output_txt_file)

# Generate and display word cloud
generate_word_cloud(text_content)
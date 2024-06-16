import json
import json
import matplotlib.pyplot as plt
import mplcursors

# Load data from output.json
with open('output/output.json', 'r') as file:
    data = json.load(file)

# Extract URL lengths and URLs
url_lengths = [len(item['url']) for item in data]
urls = [item['url'] for item in data]

# Create the bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(urls, url_lengths, color='skyblue')

# Add tooltips for each bar
cursor = mplcursors.cursor(bars)

@cursor.connect("add")
def on_add(sel):
    x, y, width, height = sel.artist[sel.target.index].get_bbox().bounds
    url = urls[sel.target.index]
    length = url_lengths[sel.target.index]
    sel.annotation.set(text=f"URL: {url}\nURL Length: {length}")

plt.xlabel('URL')
plt.ylabel('URL Length')
plt.title('URL Lengths Bar Chart')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
import json
import matplotlib.pyplot as plt
import squarify

# Load data from output.json
with open('output/output.json', 'r') as file:
    data = json.load(file)

# Extract URL lengths
url_lengths = [len(item['url']) for item in data]

# Extract URLs for labeling in the TreeMap
urls = [item['url'] for item in data]

# Create the TreeMap
plt.figure(figsize=(12, 6))
squarify.plot(sizes=url_lengths, label=urls, alpha=0.6)
plt.axis('off')
plt.show()
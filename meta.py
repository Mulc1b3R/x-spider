import json

# Load data from data.json
with open('output/data.json', 'r') as file:
    data = json.load(file)

# Extract links and external links
links = data.get('links', [])
external_links = data.get('external_links', [])

# Format the data pairs as {"url": "link"}
formatted_links = [{"url": link} for link in links]
formatted_external_links = [{"url": link} for link in external_links]

# Combine links and external links into a single list
output_data = formatted_links + formatted_external_links

# Write the output to output.json
output_file = "output/output.json"
with open(output_file, "w") as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Data extraction and output to {output_file} successful.")
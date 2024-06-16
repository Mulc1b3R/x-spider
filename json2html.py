import json

# Load data from data.json
with open('output/data.json', 'r') as file:
    data = json.load(file)

# Extract links and external links
links = data.get('links', [])
external_links = data.get('external_links', [])
target_url = data.get('target_url', '')

# Append target_url to incomplete links
def append_target_url(links, target_url):
    updated_links = []
    for link in links:
        if not link.startswith('http'):
            updated_links.append(target_url + link)
        else:
            updated_links.append(link)
    return updated_links

updated_links = append_target_url(links, target_url)
updated_external_links = append_target_url(external_links, target_url)

# Write the output to output.html
output_file = "output/output.html"
with open(output_file, "w") as html_file:
    html_file.write("<h2>Links:</h2>\n")
    html_file.write("<ul>\n")
    for link in updated_links:
        html_file.write(f"<li>{link}</li>\n")
    html_file.write("</ul>\n")

    html_file.write("<h2>External Links:</h2>\n")
    html_file.write("<ul>\n")
    for link in updated_external_links:
        html_file.write(f"<li>{link}</li>\n")
    html_file.write("</ul>\n")

print(f"Data extraction and output to {output_file} successful.")
import requests
from bs4 import BeautifulSoup
import csv
import re

# URL of the website to scrape
url = "https://petsymposium.org/2025/paperlist.php"

# Send a GET request to the website
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the section containing the accepted papers
accepted_papers = soup.find_all('div', class_='accepted-list')

# Prepare a list to store the extracted titles and authors
papers = []

# Iterate over each paper entry
for paper in accepted_papers:
    items = paper.find_all('li')
    for item in items:
        # Extract the title
        title = item.contents[0].strip()

        # Extract the authors and remove institutions with nested parentheses
        authors_raw = item.find('span').get_text(strip=True)

        # Updated regular expression to remove all content within nested parentheses
        authors_cleaned = re.sub(r'\s*\([^()]*\([^()]*\)[^()]*\)|\s*\([^()]*\)',
                                 '', authors_raw)

        # Split and rejoin authors for proper formatting
        authors_cleaned = ', '.join(
            re.split(r'\s*,\s*', authors_cleaned.strip()))

        # Append the title and cleaned authors to the papers list
        papers.append([title, authors_cleaned])

# Define the CSV file name
csv_file = "pets_2025_crawler.csv"

# Write the extracted data to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Title", "Authors"])
    # Write the paper data
    writer.writerows(papers)

print(f"Data extracted and saved to {csv_file}.")
import requests
from bs4 import BeautifulSoup
import csv
import re
from tqdm import tqdm

BASE_URL = "https://petsymposium.org/popets/"


def get_available_years(session):
    response = session.get(BASE_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    years = [
        (link.text.strip(), BASE_URL + link.get('href'))
        for link in soup.select('div.content a')
        if link.get('href', '').startswith(tuple(map(str, range(2015, 2025))))
    ]
    return years


def extract_papers_for_year(session, year_url):
    response = session.get(year_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    papers = []

    for issue in soup.find_all('h3'):
        ul_tag = issue.find_next_sibling('ul')
        if ul_tag:
            for li in tqdm(ul_tag.find_all('li'), desc="Scraping Papers",
                           unit="paper"):
                title_tag = li.find('a')

                # Skip if the <a> tag contains "Editors' Introduction"
                if title_tag and title_tag.text.strip() == "Editors' Introduction":
                    continue

                authors_tag = li.find('i')

                if title_tag and authors_tag:
                    title = title_tag.text.strip()

                    # Remove institutions from authors (assuming multiple institutions within parentheses)
                    authors_raw = authors_tag.text.strip()
                    authors_cleaned = ', '.join(re.split(r'\s*,\s*',
                                                         re.sub(r'\([^)]*\)',
                                                                '',
                                                                authors_raw)))

                    paper_url = BASE_URL + title_tag['href'].replace('../', '')
                    abstract, keywords = extract_abstract_and_keywords(session,
                                                                       paper_url)
                    papers.append((title, authors_cleaned, abstract, keywords))
    return papers


def extract_abstract_and_keywords(session, paper_url):
    try:
        response = session.get(paper_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the abstract and keywords precisely
        abstract = keywords = ""
        for p in soup.find_all('p'):
            if p.find('b') and 'Abstract:' in p.text:
                abstract = p.text.replace('Abstract:', '').strip()
            elif p.find('b') and 'Keywords:' in p.text:
                keywords = p.text.replace('Keywords:', '').strip()

        return abstract, keywords
    except requests.RequestException as e:
        print(f"Failed to retrieve {paper_url}: {e}")
        return "", ""


def save_to_csv(data, filename='pets_results_crawled.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Year', 'Title', 'Authors', 'Abstract', 'Keywords'])
        writer.writerows(data)


def scrape_pets():
    all_papers = []
    with requests.Session() as session:
        years = get_available_years(session)
        for year, year_url in tqdm(years, desc="Scraping Years", unit="year"):
            papers = extract_papers_for_year(session, year_url)
            all_papers.extend([(year, *paper) for paper in papers])
    save_to_csv(all_papers)
    print("Data saved to pets_results_crawled.csv")


if __name__ == "__main__":
    scrape_pets()

import csv
import re

# Define the search term patterns based on your matrix
title_terms = [
    r"web track.*", r"ad blocker", r"first.*party.*track.*",
    r"third.*party.*track.*"
]
abstract_terms = [
    r"web tracker", r"web tracking", r"ad tracker", r"ad blocking",
    r"first.*party.*track.*", r"third.*party.*track.*",
    r"browser fingerprinting",
    r"web tracker detection"
]
keyword_terms = [
    r"web tracker detection", r"web tracker", r"web tracking",
    r"web privacy", r"web privacy measurement"
]
exclude_title_terms = [r"eye.*"]
include_if_blockchain = [r"blockchain"]


# Function to check if any pattern matches a text
def matches_any_pattern(text, patterns):
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


# Function to apply the search term matrix filter
def filter_row(row):
    title, abstract, keywords = row['Title'], row['Abstract'], row['Keywords']

    # Title, abstract, and keyword condition checks
    title_match = matches_any_pattern(title, title_terms)
    abstract_match = matches_any_pattern(abstract, abstract_terms)
    keyword_match = matches_any_pattern(keywords, keyword_terms)

    # Exclusion condition
    exclude_title = matches_any_pattern(title, exclude_title_terms)
    include_if_title_blockchain = matches_any_pattern(title,
                                                      include_if_blockchain)

    # Apply final logic based on the search matrix
    return (
            (title_match or abstract_match or keyword_match) and
            (not exclude_title or include_if_title_blockchain)
    )


# Function to filter the CSV file based on the matrix and save results
def filter_csv(input_file, output_file='pets_results_filtered.csv'):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
            open(output_file, mode='w', newline='',
                 encoding='utf-8') as outfile:

        # Specify semicolon as the delimiter
        reader = csv.DictReader(infile, delimiter=';')
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames,
                                delimiter=';')
        writer.writeheader()

        # Apply filter row by row
        for row in reader:
            if filter_row(row):
                writer.writerow(row)

    print(f"Filtered data saved to {output_file}")


# Run the filtering function with the input CSV
if __name__ == "__main__":
    filter_csv('pets_results_full.csv')

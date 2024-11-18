import pandas as pd


def find_and_remove_duplicates(file_path, output_path):
    # Read-in csv file
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')
    # Drop columns that are completely empty
    df = df.dropna(axis=1, how='all')

    # Step 1: Remove 'arXiv' entries if they have duplicates in the other databases
    # Split DataFrame into 'arXiv' and 'Published' entries
    arxiv_df = df[df['Database'] == 'arXiv']
    published_df = df[df['Database'] != 'arXiv']

    # Find duplicates based on title
    arxiv_duplicates_title = arxiv_df.merge(published_df, on='Title',
                                            how='inner',
                                            suffixes=('_arXiv', '_published'))

    if not arxiv_duplicates_title.empty:
        print(
            "\nDuplicates for 'arXiv' papers (with matching published versions):")
        grouped_arxiv_duplicates = arxiv_duplicates_title.groupby('Title')
        for title, group in grouped_arxiv_duplicates:
            print(f"\nGroup for Title: {title}")
            print(group)

    # Remove 'arXiv' duplicates identified by matching titles
    df = df[~((df['Database'] == 'arXiv') & (
        df['Title'].isin(arxiv_duplicates_title['Title'])))]

    # Step 2: Identify general duplicates across all databases
    # Check for duplicates using both DOI and title, falling back to title if DOI is missing
    duplicate_groups = df[df.duplicated(subset=['DOI', 'Title'], keep=False)]
    if not duplicate_groups.empty:
        print("\nDuplicates found (grouped by DOI and title):")

        # Group duplicates by DOI and title
        grouped_duplicates = duplicate_groups.groupby(['DOI', 'Title'],
                                                      dropna=False)

        # Display duplicates in groups
        for (doi, title), group in grouped_duplicates:
            print(
                f"\nGroup for DOI: {doi if pd.notna(doi) else 'N/A'}, Title: {title}")
            print(group)

        # Randomly retain one entry for each duplicate group (already handled by `keep='first'` above)
        df_before = df.copy()
        df = df.drop_duplicates(subset=['DOI', 'Title'], keep='first')


        # Calculate the number of duplicates removed
        num_duplicates_removed = len(df_before) - len(df)

        # Step 4: Display summary information
        num_arxiv_removed = len(
            arxiv_duplicates_title) if 'arxiv_duplicates_title' in locals() else 0

    print(f"\nSummary:")
    print(
        f"Number of 'arXiv' duplicates removed (via title matching): {num_arxiv_removed}")
    print(
        f"Number of additional duplicates removed (across all databases): {num_duplicates_removed}")

    # Ask for confirmation to save the file
    save = input("Do you want to save the results? (y/n): ")
    if save.lower() == 'y':
        df.to_excel(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    else:
        print("Changes were not saved.")


# Example usage
file_path = 'lit_review_results/1-identification_phase/review_report/sok_literature_review_report_template.csv'
output_path = 'lit_review_results/1-identification_phase/review_report/sok_literature_review_report_without_duplicates_template.xlsx'
find_and_remove_duplicates(file_path, output_path)

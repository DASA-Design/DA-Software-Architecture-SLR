import pandas as pd

# Configuration constants
CORPUS_FILE_PATH = "corpus-stopwords-data.xlsx"
CORPUS_SHEET_NAME = "corpus terms"
OUTPUT_DIR = "res"

# High frequency stopwords thresholds
HIGH_FREQ_THRESHOLD = 150
HIGH_DOC_COVERAGE = 4
LOW_PEAKEDNESS_THRESHOLD = 0

# Low frequency stopwords thresholds
MAX_LOW_FREQ_THRESHOLD = 3
MIN_DOC_COVERAGE = 1

# Display configuration
HIGH_FREQ_DISPLAY_COUNT = 20
LOW_FREQ_DISPLAY_COUNT = 30
SAMPLE_LIST_SIZE = 50


def load_corpus_data(file_path: str,
                     sheet_name: str) -> pd.DataFrame:
    """load_corpus_data() Load and return corpus data from an Excel file.

    Args:
        file_path (str): The path to the Excel file.
        sheet_name (str): The name of the sheet to load.

    Returns:
        pd.DataFrame: The loaded corpus data.
    """
    xls = pd.ExcelFile(file_path)
    print("Available sheets:", xls.sheet_names)
    df_corpus = xls.parse(sheet_name)
    print("\nCorpus data loaded successfully!")
    print("First few rows:")
    print(df_corpus.head())
    print("\nColumns:", df_corpus.columns.tolist())
    return df_corpus


def get_hfreq_stopwords(df_corpus: pd.DataFrame,
                        freq_threshold: int,
                        doc_coverage: int,
                        peakedness_threshold: float) -> pd.DataFrame:
    """get_hfreq_stopwords() Identify high frequency terms that might be
    stopwords.

    Args:
        df_corpus (pd.DataFrame): The corpus data.
        freq_threshold (int): The frequency threshold.
        doc_coverage (int): The document coverage threshold.
    """
    # peakedness_threshold (float): The relative peakedness threshold.
    print("\n" + "="*60)
    print("HIGH FREQUENCY TERMS ANALYSIS")
    print("="*60)

    # Filter candidate stopwords based on heuristic
    candidates = df_corpus[
        (df_corpus["RawFrequency"] >= freq_threshold) &
        (df_corpus["inDocumentsCount"] >= doc_coverage) &
        (df_corpus["RelativePeakedness"] <= peakedness_threshold)
    ]

    # Sort by frequency for better review
    candidates = candidates.sort_values(by="RawFrequency", ascending=False)

    # Display the candidate terms
    display_columns = [
        "Term",
        "RawFrequency",
        "inDocumentsCount",
        "RelativePeakedness"
    ]
    display_data = candidates[display_columns].head(HIGH_FREQ_DISPLAY_COUNT)

    print(f"\nHigh Freq. Candidate Stopwords (top {HIGH_FREQ_DISPLAY_COUNT}):")
    print(display_data)
    return candidates


def get_lfreq_stopwords(df_corpus: pd.DataFrame,
                        max_freq_threshold: int,
                        min_doc_coverage: int) -> pd.DataFrame:
    """get_lfreq_stopwords() Identify low frequency terms that might be
    stopwords.

    Args:
        df_corpus (pd.DataFrame): The corpus data.
        max_freq_threshold (int): The maximum frequency threshold.
        min_doc_coverage (int): The minimum document coverage threshold.

    Returns:
        pd.DataFrame: The identified low frequency stopwords.
    """

    # printing header for low frequency analysis
    print("\n" + "="*60)
    print("LOW FREQUENCY TERMS ANALYSIS")
    print("="*60)

    # Filter candidate low-frequency stopwords based on heuristic
    candidates = df_corpus[
        (df_corpus["RawFrequency"] <= max_freq_threshold) &
        (df_corpus["RawFrequency"] >= min_doc_coverage) &
        (df_corpus["inDocumentsCount"] >= min_doc_coverage)
    ]

    # Sort by frequency (ascending) to see the least frequent terms first
    candidates = candidates.sort_values(by="RawFrequency", ascending=True)

    # Display the candidate low-frequency terms
    display_columns = [
        "Term",
        "RawFrequency",
        "inDocumentsCount",
        "RelativePeakedness"
    ]
    display_data = candidates[display_columns].head(LOW_FREQ_DISPLAY_COUNT)

    print(f"\nLow Freq. Candidate Stopwords (top {LOW_FREQ_DISPLAY_COUNT}):")
    print(display_data)

    # Print statistics
    print_freq_statistics(df_corpus, candidates, max_freq_threshold)
    return candidates


def print_freq_statistics(df_corpus: pd.DataFrame,
                          candidates: pd.DataFrame,
                          max_threshold: int) -> None:
    """print_freq_statistics() Print statistics about low frequency terms.

    Args:
        df_corpus (pd.DataFrame): The original corpus data.
        candidates (pd.DataFrame): The identified low frequency stopwords.
        max_threshold (int): The maximum frequency threshold.
    """
    total_candidates = candidates.shape[0]
    freq_1_count = df_corpus[df_corpus["RawFrequency"] == 1].shape[0]
    freq_2_count = df_corpus[df_corpus["RawFrequency"] == 2].shape[0]
    freq_3_count = df_corpus[df_corpus["RawFrequency"] == 3].shape[0]
    print("\nLow Frequency Statistics:")
    print(f"Total terms with frequency <= {max_threshold}: {total_candidates}")
    print(f"Terms appearing exactly 1 time: {freq_1_count}")
    print(f"Terms appearing exactly 2 times: {freq_2_count}")
    print(f"Terms appearing exactly 3 times: {freq_3_count}")


def save_stopwords_file(stopwords_lt: list,
                        filename: str,
                        description: str) -> None:
    """save_stopwords_file() Save stopwords list to a file.
    Args:
        stopwords_lt (list): The list of stopwords to save.
        filename (str): The name of the file to save.
        description (str): A description of the stopwords type.
    """
    filepath = f"{OUTPUT_DIR}/{filename}"

    with open(filepath, "w", encoding="utf-8") as f:
        for word in stopwords_lt:
            f.write(f"{word}\n")

    print(f"Saved {len(stopwords_lt)} {description} stopwords to '{filepath}'")


def main():
    """Main function to orchestrate the stopwords analysis."""
    # Load corpus data
    df_corpus = load_corpus_data(CORPUS_FILE_PATH, CORPUS_SHEET_NAME)

    # Get high frequency stopwords
    high_freq_candidates = get_hfreq_stopwords(df_corpus,
                                               HIGH_FREQ_THRESHOLD,
                                               HIGH_DOC_COVERAGE,
                                               LOW_PEAKEDNESS_THRESHOLD)

    # Get low frequency stopwords
    low_freq_candidates = get_lfreq_stopwords(df_corpus,
                                              MAX_LOW_FREQ_THRESHOLD,
                                              MIN_DOC_COVERAGE)

    # Extract stopwords lists
    high_freq_stopwords = high_freq_candidates["Term"].tolist()
    low_freq_stopwords = low_freq_candidates["Term"].tolist()

    # Display sample of low frequency stopwords
    print(f"\nLow Frequency Stopwords List (first {SAMPLE_LIST_SIZE}):")
    print(low_freq_stopwords[:SAMPLE_LIST_SIZE])

    # Save all stopwords to files
    print("\n" + "="*60)
    print("SAVING STOPWORDS TO FILES")
    print("="*60)

    save_stopwords_file(high_freq_stopwords,
                        "high_freq_stopwords.txt",
                        "high frequency")
    save_stopwords_file(low_freq_stopwords,
                        "low_freq_stopwords.txt",
                        "low frequency")

    # Create and save combined stopwords list
    combi_stopwords = high_freq_stopwords + low_freq_stopwords
    save_stopwords_file(combi_stopwords,
                        "combi_stopwords.txt",
                        "combined")

    print(f"\nAnalysis complete! Generated {len(combi_stopwords)} stopwords.")


if __name__ == "__main__":
    main()

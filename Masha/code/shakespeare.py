import csv
import os
import re

INPUT_DIR = os.path.join("data", "shakespeare")
STOPWORDS_PATH = os.path.join(INPUT_DIR, "stopwords.txt")
SHAKESPEARE_PATH = os.path.join(INPUT_DIR, "shakespeare.txt")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "shakespeare_report.csv")

NUM_LINES_TO_SKIP = 246
LAST_LINE_START = "End of this Etext"


def load_stopwords():
    """Load the stopwords from the file and return a set of the cleaned stopwords."""

    stopwords = set()
    # Open the stopwords file for reading - r for read , w for write , etc.

    # encoding - different types of character sets - engl etc - different mapping - file just bytes - decod into char
    with open("data/shakespeare/stopwords.txt", "r", encoding="utf-8") as file:
        filetext = file.readlines()
        # Read each line (stopword) from the file
        for line in filetext:
            # Clean the stopword by removing leading/trailing whitespace and converting to lowercase
            cleaned_stopword = line.strip().lower()
            # taking all cap letters convert to lower
            clean_text = re.sub(r'\s+', '', cleaned_stopword)
            # all white spaces (new lines) replace with single space
            text_with_only_spaces = re.sub(r"[^a-zA-Z\s']", " ", clean_text)
            # Add the cleaned stopword to the set
            stopwords.add(text_with_only_spaces)

    print(stopwords)
    return stopwords


def load_shakespeare_lines():
    """Loads every line in the dataset that was written by Shakespeare as a list of strings."""

    shakespeare_no_att = None
    shakespeare_lines = []

    # open file path for reading:
    with open("data/shakespeare/shakespeare.txt", "r") as file:
        shakespeare_no_att = file.read()

    # remove attribution paragraphs:
    # while loop excute code until code turns false
    while '<<' in shakespeare_no_att:
        # finding position of carrots - index
        x, y = shakespeare_no_att.index('<<'), shakespeare_no_att.index('>>')
        # everything from beginning string up to <<, given by post. x, then after two arrow sign until end of string
        shakespeare_no_att = shakespeare_no_att[0:x] + shakespeare_no_att[y + 2:]

    # split text by William Shakespear:
    shakespeare_no_header = shakespeare_no_att.split('by William Shakespeare')[1:]

    # remove ending line: - for loop one line - going thru different lists getting everything before the end
    shakespeare_no_end = (x.split('THE END')[0] for x in shakespeare_no_header)

    for x in shakespeare_no_end:
        clean_text = re.sub('[^A-Za-z\s]', '', x)
        text_with_only_spaces = re.sub("\s+", " ", x)
        shakespeare_lines.append(text_with_only_spaces.split())
    return shakespeare_lines


def get_shakespeare_words(shakespeare_lines):
    """Takes the lines and makes a list of lowercase words."""

    words = []

    for line in shakespeare_lines:
        for word in line:
            # Extract words using a regular expression that matches words with or without quotes/apostrophes
            word_cleaned = re.sub(r'[^\w\']+', '', word)

            # Check if the cleaned word is not empty after removing special characters
            if word_cleaned:
                # Convert each word to lowercase and add it to the list
                words.append(word_cleaned.lower())
    print(words)
    return words


def count_words(words, stopwords):
    """Counts the words that are not stopwords.
    returns a dictionary with words as keys and values."""

    word_counts = dict()

    for word in words:
        # Check if the word is not a stopword
        if word not in stopwords:
            # If the word is not in the dictionary, add it with a count of 1
            if word not in word_counts:
                word_counts[word] = 1
            else:
                # If the word is already in the dictionary, increment its count by 1
                word_counts[word] += 1
    print(word_counts)
    return word_counts


def sort_word_counts(word_counts):
    """Takes a dictionary or word counts.
    Returns a list of (word, count) tuples that are sorted by count in descending order."""

    # Use sorted function with a custom sorting key to sort by count in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(sorted_word_counts)
    return sorted_word_counts


def write_word_counts(sorted_word_counts, path):
    """Takes a list of (word, count) tuples and writes them to a CSV."""

    with open(path, mode='w+', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Word', 'Count'])

        # Write each (word, count) tuple as a row in the CSV file
        for word, count in sorted_word_counts:
            writer.writerow([word, count])

    print(OUTPUT_PATH)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    stopwords = load_stopwords()

    shakespeare_lines = load_shakespeare_lines()
    shakespeare_words = get_shakespeare_words(shakespeare_lines)

    word_counts = count_words(shakespeare_words, stopwords)
    word_counts_sorted = sort_word_counts(word_counts)

    write_word_counts(word_counts_sorted, OUTPUT_PATH)
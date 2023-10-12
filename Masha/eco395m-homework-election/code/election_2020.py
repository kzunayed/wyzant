import csv
import os

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report.csv")


def count_votes(path):
    counts = {}
    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            try:
                if row['year'] == '2020':
                    year, state_code, candidate, votes = int(row['year']), row['state_po'], row['candidate'], int(row['candidatevotes'])
                    key = (year, state_code, candidate)
                    counts[key] = counts.get(key, 0) + votes
            except ValueError:
                pass
    return counts



def get_rows(counts):
    rows = []
    for key, value in counts.items():
        rows.append({'year': key[0],
                     'state_code': key[1],
                     'candidate': key[2],
                     'votes': value})
    return rows


def sort_rows(rows):
    sorted_by_state = sorted(rows, key=lambda x: x['state_code'])
    rows_lex_ordered = sorted(sorted_by_state, key=lambda x: (x['state_code'], -x['votes']))
    return rows_lex_ordered


def write_rows(rows):
    fieldnames = ['year', 'state_code', 'candidate', 'votes']

    with open(OUTPUT_PATH, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    counts = count_votes(IN_PATH)
    rows = get_rows(counts)
    sorted_rows = sort_rows(rows)
    write_rows(sorted_rows)

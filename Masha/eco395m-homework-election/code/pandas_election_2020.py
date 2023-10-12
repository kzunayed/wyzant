import os
import pandas as pd

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report_pandas.csv")

if __name__ == "__main__":
    df = pd.read_csv(IN_PATH)
    df_2020 = df[df['year'] == 2020]
    df_filtered = df_2020[['year', 'state_po', 'candidate', 'candidatevotes']]
    df_renamed = df_filtered.rename(columns={'state_po': 'state_code', 'candidatevotes': 'votes'})

    grouped_data = df_renamed.groupby(['year', 'state_code', 'candidate'], as_index=False).agg({'votes': 'sum'})
    grouped_data['votes'] = grouped_data['votes'].astype(int)

    sorted_data = grouped_data.sort_values(by=['state_code', 'votes'], ascending=[True, False])

    sorted_data.to_csv(OUTPUT_PATH, index=False)

import pandas as pd
import json
import os

def aggregate_crossref_data(directory):
    # Initialize an empty list to store the data
    data_frames = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                df = convert_to_dataframe(json_data)
                data_frames.append(df)
    
    # Concatenate all DataFrames
    combined_df = pd.concat(data_frames, ignore_index=True)
    return combined_df

def convert_to_dataframe(data):
    return pd.json_normalize(data)

def expand_lists_to_columns(df):
    for column in df.columns:
        if df[column].apply(lambda x: isinstance(x, list)).any():
            df = df.explode(column).reset_index(drop=True)
    return df


def expand_rows_to_columns(df):
    return pd.concat([df.drop([col], axis=1).join(pd.DataFrame(df[col].tolist(), index=df.index)) for col in df.columns if df[col].apply(lambda x: isinstance(x, dict)).any()], axis=1)


def tidy_columns(df):
    # Keep only the fields we are interested in exploring
    result = df[['DOI', 'member', 'is-referenced-by-count', 'reference', 'reference-count']]
    return result

def export_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    directory = '/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/sample_dataset'
    combined_df = aggregate_crossref_data(directory)
    
    combined_df = expand_lists_to_columns(combined_df)
    combined_df = expand_rows_to_columns(combined_df)
    combined_df_trim = tidy_columns(combined_df)

    output_file = '/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/aggregated_data_expanded_rows.csv'
    output_file = '/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/aggregated_data_expanded_rows_trim.csv'
    export_to_csv(combined_df, output_file)
    export_to_csv(combined_df_trim, output_file)

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

def export_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    directory = '/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/sample_dataset'
    combined_df = aggregate_crossref_data(directory)
    
    # combined_df = expand_lists_to_columns(combined_df)
    # combined_df = expand_rows_to_columns(combined_df)
    
    output_file = '/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/aggregated_data_expanded_rows_v2.csv'
    export_to_csv(combined_df, output_file)
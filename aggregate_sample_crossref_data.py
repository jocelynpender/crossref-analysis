import pandas as pd
import json
import os

def aggregate_crossref_data(directory):
    # Initialize an empty list to store the data
    data = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                data.append(json_data)

    # Convert the list of JSON objects to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

def export_to_csv(df, output_file):
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    directory = '/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/sample_dataset'
    df = aggregate_crossref_data(directory)
    
    output_file = '/Users/jocelynpender/Documents/02 - AREAS/Career/2025 Update/Crossref/interview-prep/sample-data/aggregated_data.csv'
    export_to_csv(df, output_file)
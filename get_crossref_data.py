import requests
import pandas as pd

def get_crossref_data(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return pd.json_normalize(data)
    else:
        return None

if __name__ == "__main__":
    doi = "10.1016/j.jacc.2017.11.012"  # Example DOI
    data = get_crossref_data(doi)
    
    if data is not None:
        print(data)
    else:
        print("Failed to retrieve data")
import requests

def get_crossref_data(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    doi = "10.1038/nphys1170"  # Example DOI
    data = get_crossref_data(doi)
    
    if data:
        print(data)
    else:
        print("Failed to retrieve data")
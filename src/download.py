
# This script downloads the Synthea sample data from the Synthetic Health GitHub repository.
# The data is in FHIR format and is used to test the FHIR server.

import requests
import os


class SyntheaDataDownloader:
    def __init__(self, url, zip_filename, extract_to='./data/extracted'):
        self.url = url
        self.zip_filename = zip_filename
        self.extract_to = extract_to

    def download_and_extract(self):
        # Download the file
        # ONly download if the zip file doesn't exist
        if not os.path.exists(self.zip_filename):
            self.download()
            self.extract()
        else:
            print(f'{self.zip_filename} already exists.')
            # extract if the json files in the ./data folder is empty, filter for json files
            if not any([f.endswith('.json') for f in os.listdir(self.extract_to)]):
                self.extract()


    def download(self):
        print(f'Downloading {self.url} to {self.zip_filename}')
        r = requests.get(self.url)
        with open(self.zip_filename, 'wb') as f:
            f.write(r.content)
        print(f'{self.zip_filename} downloaded.')

        # Extract the file
    def extract(self):
        import zipfile
        with zipfile.ZipFile(self.zip_filename, 'r') as zip_ref:
            zip_ref.extractall(self.extract_to)
        print(f'{self.zip_filename} extracted to {self.extract_to}')

# Usage
if __name__ == "__main__":
    # download from smart on fhir
    # Download the Synthea sample data in FHIR R4 json format
    # https://github.com/smart-on-fhir/sample-bulk-fhir-datasets/archive/refs/heads/100-patients.zip
    url = 'https://github.com/smart-on-fhir/sample-bulk-fhir-datasets/archive/refs/heads/100-patients.zip'
    # Create the data folder
    downloader = SyntheaDataDownloader(url, './data/sample-bulk-fhir-data.zip')
    downloader.download_and_extract()

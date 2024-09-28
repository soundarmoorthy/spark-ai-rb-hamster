
# This script downloads the Synthea sample data from the Synthetic Health GitHub repository.
# The data is in FHIR format and is used to test the FHIR server.

import requests
import os

class SyntheaDataDownloader:
    def __init__(self, url, zip_filename, extract_to='./data'):
        self.url = url
        self.zip_filename = zip_filename
        self.extract_to = extract_to

    def download_and_extract(self):
        # Download the file
        response = requests.get(self.url, allow_redirects=True)
        with open(self.zip_filename, 'wb') as file:
            file.write(response.content)

        # Extract the file
        os.system(f'unzip {self.zip_filename} -d {self.extract_to}')

# Usage
if __name__ == "__main__":
    url = 'https://synthetichealth.github.io/synthea-sample-data/downloads/latest/synthea_sample_data_fhir_latest.zip'
    downloader = SyntheaDataDownloader(url, 'synthea_sample_data_fhir_r4_sep2019.zip')
    downloader.download_and_extract()
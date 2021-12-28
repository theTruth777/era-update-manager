import requests


class Networking:

    def __init__(self):
        self.headers = {
            'User-Agent': 'ERA Update Manager',
        }

    def download_era(self):
        url_download = 'https://era.sh/download/linux'
        return requests.get(url_download, headers=self.headers, stream=True)

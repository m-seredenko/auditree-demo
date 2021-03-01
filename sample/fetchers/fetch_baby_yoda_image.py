import requests

from compliance.fetch import ComplianceFetcher
from compliance.evidence import store_raw_evidence


BABY_YODA_IMAGE_URL = 'https://www.abc.net.au/cm/rimage/11851850-3x2-large.jpg'


class BabyYodaImageFetcher(ComplianceFetcher):
    @property
    def title(self):
        return 'Baby Yoda Image'

    @store_raw_evidence('images/baby_yoda.png')
    def fetch_baby_yoda_image(self):
        return requests.get(BABY_YODA_IMAGE_URL).content

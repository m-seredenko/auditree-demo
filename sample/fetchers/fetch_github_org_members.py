import json
import os
import requests

from compliance.fetch import ComplianceFetcher
from compliance.evidence import store_raw_evidence


class GithubOrganizationMembersFetcher(ComplianceFetcher):
    @property
    def title(self):
        return 'Github Organization Members'

    @store_raw_evidence('results/github_org_members.json')
    def fetch_org_members(self):
        auth_token = os.getenv('GITHUB_API_TOKEN')
        org = os.getenv('GITHUB_ORG')

        if not any([auth_token, org]):
            raise AssertionError('You have to specify all required params')

        members = []
        inx = 1
        while True:
            response = requests.get(
                f'https://api.github.com/orgs/{org}/members?page={inx}',
                headers={
                    'Authorization': f'token {auth_token}',
                },
            )
            fetched_users = response.json()
            if not fetched_users:
                break

            members += fetched_users
            inx += 1

        return json.dumps(members)

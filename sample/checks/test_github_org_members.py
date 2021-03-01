import csv
import io
import json

from compliance.check import ComplianceCheck
from compliance.evidence import with_raw_evidences, ReportEvidence, DAY


class GithubOrganizationMembersCheck(ComplianceCheck):
    @property
    def title(self):
        return 'Github Organization Members'

    @with_raw_evidences('results/github_org_members.json')
    def test_org_members(self, evidence):
        file = io.StringIO(newline='')
        writer = csv.writer(file)

        for member in json.loads(evidence.content):
            values = member.values()
            writer.writerow(values)

        file.seek(io.SEEK_SET)
        csv_body = file.read()

        report_evidence = ReportEvidence(
            'github_org_members.csv',
            'results',
            DAY,
            'Github Organization Members'
        )
        report_evidence.set_content(csv_body)
        self.locker.add_evidence(report_evidence)

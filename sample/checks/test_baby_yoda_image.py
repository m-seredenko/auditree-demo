from compliance.check import ComplianceCheck
from compliance.evidence import ReportEvidence, with_raw_evidences, DAY


class BabyYodaImageCheck(ComplianceCheck):
    @property
    def title(self):
        return 'Baby Yoda Image'

    @with_raw_evidences('images/baby_yoda.png')
    def test_baby_yoda_image(self, raw_evidence):
        if not raw_evidence.content:
            raise AssertionError('Unable to find fetched image')

        report_evidence = ReportEvidence(
            'baby_yoda.png',
            'images',
            DAY,
            'Baby Yoda Image',
        )
        report_evidence.binary_content = True
        report_evidence.set_content(raw_evidence.content)
        self.locker.add_evidence(report_evidence)

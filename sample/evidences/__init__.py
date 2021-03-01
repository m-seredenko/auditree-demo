from compliance.config import get_config
from compliance.evidence import DAY, ReportEvidence, RawEvidence


get_config().add_evidences(
    [
        RawEvidence(
            'github_org_members.json',
            'results',
            DAY,
            'Github Organization Members'
        ),
        RawEvidence(
            'baby_yoda.png',
            'images',
            DAY,
            'Baby Yoda Image',
            binary_content=True
        ),
    ]
)


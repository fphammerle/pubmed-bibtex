import re

import pubmed_bibtex


def test_version():
    assert re.match(r'^\d+\.\d+\.', pubmed_bibtex.__version__)

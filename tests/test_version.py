import re

import pubmed_bibtex


def test_version() -> None:
    assert re.match(r"^\d+\.\d+\.", pubmed_bibtex.__version__)

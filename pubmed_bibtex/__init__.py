"""
Generate BibTeX Entries for PubMed Publications

This module utilizes the API of TeXMed,
a BibTeX interface for PubMed.

TeXMed was written by Arne Muller
https://www.bioinformatics.org/texmed/

Command Line Example:
$ pubmed-bibtex 31025164
@Article{pmid31025164,
   Author="...",
   Title="...",
   Journal="...",
   ...
}

Python Example:
>>> from pubmed_bibtex import bibtex_entry_from_pmid
>>> print(bibtex_entry_from_pmid(123456789))
"""
import html.parser
import re

import requests

from pubmed_bibtex.version import __version__

_TEXMED_URL_PATTERN = 'https://www.bioinformatics.org/texmed/cgi-bin' \
                      '/list.cgi?PMID={pmid}&linkOut'


class _TeXMedHtmlParser(html.parser.HTMLParser):

    def __init__(self):
        self.bibtex_entry = None
        super().__init__()

    @staticmethod
    def _strip_bibtex_entry(data: str) -> str:
        return re.sub(r'\n\% \d+\s?\n', '', data).strip() + '\n'

    def handle_data(self, data: str) -> None:
        if 'Author' in data:
            self.bibtex_entry = self._strip_bibtex_entry(data)

    def error(self, message) -> None:
        raise Exception(message)  # pragma: no cover


def bibtex_entry_from_pmid(pmid: str) -> str:
    assert pmid.isdigit(), pmid
    resp = requests.get(_TEXMED_URL_PATTERN.format(pmid=pmid))
    resp.raise_for_status()
    parser = _TeXMedHtmlParser()
    parser.feed(resp.text)
    return parser.bibtex_entry

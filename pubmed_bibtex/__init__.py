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

Copyright (C) 2019 Fabian Peter Hammerle <fabian@hammerle.me>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
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

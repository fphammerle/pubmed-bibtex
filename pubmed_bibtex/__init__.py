"""
Generate BibTeX Entries for PubMed Publications

This module utilizes the API of TeXMed,
a BibTeX interface for PubMed.

TeXMed was written by Arne Muller
https://www.bioinformatics.org/texmed/
"""
import argparse
import html.parser
import re

import requests

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


def bibtex_entry_from_pmid(pmid: str) -> str:
    assert pmid.isdigit(), pmid
    resp = requests.get(_TEXMED_URL_PATTERN.format(pmid=pmid))
    resp.raise_for_status()
    parser = _TeXMedHtmlParser()
    parser.feed(resp.text)
    return parser.bibtex_entry


def _main():
    argparser = argparse.ArgumentParser(
        description=__doc__.strip(),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    argparser.add_argument('pmid')
    args = argparser.parse_args()
    print(bibtex_entry_from_pmid(pmid=args.pmid),
          end='')

if __name__ == '__main__':
    _main()

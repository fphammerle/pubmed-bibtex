import logging
import unittest.mock
import urllib.error

import pytest

import pubmed_bibtex

# pylint: disable=wrong-import-order; false positive
from conftest import TEST_BIBTEX_ENTRY, TEST_PMID


def test_bibtex_entry_from_pmid() -> None:
    assert pubmed_bibtex.bibtex_entry_from_pmid(pmid=TEST_PMID) == TEST_BIBTEX_ENTRY


@unittest.mock.patch.object(
    pubmed_bibtex,
    "_TEXMED_URL_PATTERN",
    "https://www.bioinformatics.org/texmed/cgi-bin/42.cgi",
)
def test_bibtex_entry_from_pmid_not_found() -> None:
    with pytest.raises(urllib.error.HTTPError, match=r"^HTTP Error 404: Not Found$"):
        pubmed_bibtex.bibtex_entry_from_pmid(pmid=TEST_PMID)


def test_bibtex_entry_from_pmid_retry(caplog) -> None:
    with unittest.mock.patch(
        "pubmed_bibtex._TeXMedHtmlParser.feed"
    ) as feed_mock, caplog.at_level(logging.WARNING):
        assert pubmed_bibtex.bibtex_entry_from_pmid(pmid=TEST_PMID, retries=2) is None
    assert feed_mock.call_count == 3
    assert caplog.record_tuples == [
        ("pubmed_bibtex", logging.WARNING, "attempt #1/3 to fetch bibtex entry failed"),
        ("pubmed_bibtex", logging.WARNING, "attempt #2/3 to fetch bibtex entry failed"),
        ("pubmed_bibtex", logging.ERROR, "attempt #3/3 to fetch bibtex entry failed"),
    ]

from pubmed_bibtex import bibtex_entry_from_pmid

from conftest import TEST_PMID, TEST_BIBTEX_ENTRY


def test_bibtex_entry_from_pmid():
    assert bibtex_entry_from_pmid(pmid=TEST_PMID) == TEST_BIBTEX_ENTRY

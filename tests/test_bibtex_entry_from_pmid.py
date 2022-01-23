from pubmed_bibtex import bibtex_entry_from_pmid

# pylint: disable=wrong-import-order; false positive
from conftest import TEST_BIBTEX_ENTRY, TEST_PMID


def test_bibtex_entry_from_pmid() -> None:
    assert bibtex_entry_from_pmid(pmid=TEST_PMID) == TEST_BIBTEX_ENTRY

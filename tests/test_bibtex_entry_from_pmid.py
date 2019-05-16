import subprocess
import unittest.mock

from pubmed_bibtex import bibtex_entry_from_pmid, _main

TEST_PMID = '31025164'
TEST_BIBTEX_ENTRY = r"""@Article{pmid31025164,
   Author="Egger, F.  and Hofer, C.  and Hammerle, F. P.  and Lofler, S.  and Nurnberg, M.  and Fiedler, L.  and Kriz, R.  and Kern, H.  and Huber, K. ",
   Title="{{I}nfluence of electrical stimulation therapy on permanent pacemaker function}",
   Journal="Wien. Klin. Wochenschr.",
   Year="2019",
   Month="Apr",
   Note={[DOI:\href{https://dx.doi.org/10.1007/s00508-019-1494-5}{10.1007/s00508-019-1494-5}] [PubMed:\href{https://www.ncbi.nlm.nih.gov/pubmed/31025164}{31025164}] }
}
"""


def test_bibtex_entry_from_pmid():
    assert bibtex_entry_from_pmid(pmid=TEST_PMID) == TEST_BIBTEX_ENTRY


def test_main(capsys):
    with unittest.mock.patch('sys.argv', ['', TEST_PMID]):
        _main()
    out, err = capsys.readouterr()
    assert not err
    assert out == TEST_BIBTEX_ENTRY


def test_script():
    proc_info = subprocess.run(['pubmed-bibtex', TEST_PMID],
                               check=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    assert not proc_info.stderr
    assert proc_info.stdout == TEST_BIBTEX_ENTRY.encode()

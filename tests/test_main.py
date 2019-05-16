import subprocess
import unittest.mock

import pubmed_bibtex
from pubmed_bibtex.__main__ import main

from conftest import TEST_PMID, TEST_BIBTEX_ENTRY


def test_main(capsys):
    with unittest.mock.patch('sys.argv', ['', TEST_PMID]):
        main()
    out, err = capsys.readouterr()
    assert not err
    assert out == TEST_BIBTEX_ENTRY


def test_script_module():
    proc_info = subprocess.run(['python', '-m', 'pubmed_bibtex', TEST_PMID],
                               check=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    assert not proc_info.stderr
    assert proc_info.stdout == TEST_BIBTEX_ENTRY.encode()


def test_script():
    proc_info = subprocess.run(['pubmed-bibtex', TEST_PMID],
                               check=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    assert not proc_info.stderr
    assert proc_info.stdout == TEST_BIBTEX_ENTRY.encode()


def test_version():
    proc_info = subprocess.run(['pubmed-bibtex', '--version'],
                               check=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    assert not proc_info.stderr
    assert proc_info.stdout == pubmed_bibtex.__version__.encode() + b'\n'

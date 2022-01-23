import subprocess
import unittest.mock

import _pytest.capture

import pubmed_bibtex
from pubmed_bibtex.__main__ import _main

# pylint: disable=wrong-import-order; false positive
from conftest import TEST_BIBTEX_ENTRY, TEST_PMID


def test__main(capsys: _pytest.capture.CaptureFixture) -> None:
    with unittest.mock.patch("sys.argv", ["", TEST_PMID]):
        _main()
    out, err = capsys.readouterr()
    assert not err
    assert out == TEST_BIBTEX_ENTRY


def test_script_module() -> None:
    proc_info = subprocess.run(
        ["python", "-m", "pubmed_bibtex", TEST_PMID],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert not proc_info.stderr
    assert proc_info.stdout == TEST_BIBTEX_ENTRY.encode()


def test_script() -> None:
    proc_info = subprocess.run(
        ["pubmed-bibtex", TEST_PMID],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert not proc_info.stderr
    assert proc_info.stdout == TEST_BIBTEX_ENTRY.encode()


def test_version() -> None:
    proc_info = subprocess.run(
        ["pubmed-bibtex", "--version"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert not proc_info.stderr
    assert proc_info.stdout == pubmed_bibtex.__version__.encode() + b"\n"

pubmed-bibtex
=============

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
.. image:: https://github.com/fphammerle/pubmed-bibtex/workflows/tests/badge.svg
    :target: https://github.com/fphammerle/pubmed-bibtex/actions
.. image:: https://ipfs.io/ipfs/QmP8k5H4MkfspFxQxdL2kEZ4QQWQjF8xwPYD35KvNH4CA6/20230429T090002+0200/s3.amazonaws.com/assets.coveralls.io/badges/coveralls_100.svg
    :target: https://github.com/fphammerle/pubmed-bibtex/actions
.. image:: https://img.shields.io/pypi/v/pubmed-bibtex.svg
    :target: https://pypi.org/project/pubmed-bibtex/#history
.. image:: https://img.shields.io/pypi/pyversions/pubmed-bibtex.svg
    :target: https://pypi.org/project/pubmed-bibtex/

Python Script & Module to Generate BibTeX Entries for PubMed
Publications

Utilizes the API of TeXMed, a BibTeX interface for PubMed.

TeXMed was written by Arne Muller https://www.bioinformatics.org/texmed/

pubmed-bibtex is currently unmaintained & archived cause TeXMed's exporter
skips german umlaute & possibly other non-ascii characters
(see `example <https://web.archive.org/web/20230512115423/https://www.bioinformatics.org/texmed/cgi-bin/list.cgi?PMID=31025164>`_)

Install
-------

.. code:: sh

    pip3 install --user pubmed-bibtex

Usage
-----

.. code:: sh

    $ pubmed-bibtex 31025164
    @Article{pmid31025164,
       Author="...",
       Title="...",
       Journal="...",
       ...
    }

or

.. code:: python

    from pubmed_bibtex import bibtex_entry_from_pmid
    print(bibtex_entry_from_pmid(123456789))

Tests
-----

.. code:: sh

    pip3 install --user pipenv
    git clone https://github.com/fphammerle/pubmed-bibtex.git
    cd pubmed-bibtex
    pipenv run pylint freesurfer_surface
    pipenv run pytest --cov=freesurfer_surface

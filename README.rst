pubmed-bibtex
=============

Python Script & Module to Generate BibTeX Entries for PubMed
Publications

Utilizes the API of TeXMed, a BibTeX interface for PubMed.

TeXMed was written by Arne Muller https://www.bioinformatics.org/texmed/

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

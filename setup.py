import pathlib

import setuptools

setuptools.setup(
    name="pubmed-bibtex",
    use_scm_version={
        "write_to": pathlib.Path(__file__).parent.joinpath(
            "pubmed_bibtex", "version.py"
        ),
        # `version` triggers pylint C0103
        "write_to_template": "__version__ = '{version}'\n",
    },
    description="Generate BibTeX Entries for PubMed Publications",
    long_description=pathlib.Path(__file__)
    .parent.joinpath("README.rst")
    .read_text(encoding="utf8"),
    author="Fabian Peter Hammerle",
    author_email="fabian@hammerle.me",
    url="https://github.com/fphammerle/pubmed-bibtex",
    license="GPLv3+",
    keywords=[
        "article",
        "bibtex",
        "citation",
        "journal",
        "latex",
        "publication",
        "pubmed",
        "reference",
        "research",
        "tex",
        "texmed",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        # .github/workflows/python.yml
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Utilities",
    ],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pubmed-bibtex = pubmed_bibtex.__main__:_main",
        ],
    },
    # >=3.6 for variable type hints
    python_requires=">=3.7",  # python<3.7 untested
    install_requires=[],
    setup_requires=["setuptools_scm"],
    tests_require=[
        "pylint>=2.3.0,<3",
        "pytest<5",
        "pytest-cov<3,>=2",
    ],
)

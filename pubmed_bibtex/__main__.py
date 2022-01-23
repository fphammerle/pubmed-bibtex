"""
Generate BibTeX Entries for PubMed Publications

Copyright (C) 2019 Fabian Peter Hammerle <fabian@hammerle.me>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse

import pubmed_bibtex

__version__ = pubmed_bibtex.__version__


def _main() -> None:
    argparser = argparse.ArgumentParser(
        description=pubmed_bibtex.__doc__.strip(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    argparser.add_argument(
        "--version", action="version", version=pubmed_bibtex.__version__
    )
    argparser.add_argument("pmid")
    args = argparser.parse_args()
    print(pubmed_bibtex.bibtex_entry_from_pmid(pmid=args.pmid), end="")


if __name__ == "__main__":
    _main()

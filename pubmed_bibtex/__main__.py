import argparse

import pubmed_bibtex

def main():
    argparser = argparse.ArgumentParser(
        description=pubmed_bibtex.__doc__.strip(),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    argparser.add_argument('pmid')
    args = argparser.parse_args()
    print(pubmed_bibtex.bibtex_entry_from_pmid(pmid=args.pmid),
          end='')

if __name__ == '__main__':
    main()

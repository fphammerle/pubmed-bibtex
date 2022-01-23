# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2022-01-23
### Added
- GPLv3+ license

### Changed
- `bibtex_entry_from_pmid` raises `urllib.error.HTTPError`
  instead of `requests.exceptions.HTTPError`
  (replaced [requests](https://pypi.org/project/requests/) with python's `urllib.request`)

### Removed
- compatibility with `python3.5` & `python3.6`

### Fixed
- return type hint of function `bibtex_entry_from_pmid`

## [0.1.0] - 2019-05-16

[Unreleased]: https://github.com/fphammerle/pubmed-bibtex/compare/1.0.0...HEAD
[1.0.0]: https://github.com/fphammerle/pubmed-bibtex/compare/0.1.0...1.0.0
[0.1.0]: https://github.com/fphammerle/pubmed-bibtex/releases/tag/0.1.0

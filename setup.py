import os

import setuptools

import pubmed_bibtex


LONG_DESCRIPTION = pubmed_bibtex.__doc__.lstrip()

setuptools.setup(
    name='pubmed-bibtex',
    use_scm_version={
        'write_to': os.path.join('pubmed_bibtex', 'version.py'),
        # `version` triggers pylint C0103
        'write_to_template': "__version__ = '{version}'\n",
    },
    description=LONG_DESCRIPTION.split(sep='\n', maxsplit=1)[0],
    long_description=LONG_DESCRIPTION,
    author='Fabian Peter Hammerle',
    author_email='fabian@hammerle.me',
    url='https://github.com/fphammerle/pubmed-bibtex',
    # TODO add license
    keywords=[
        'article',
        'bibtex',
        'citation',
        'journal',
        'latex',
        'publication',
        'pubmed',
        'reference',
        'research',
        'tex',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Utilities',
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pubmed-bibtex = pubmed_bibtex:_main',
        ],
    },
    python_requires='>=3.5',
    install_requires=[
        'requests>=2,<3',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    tests_require=[
        'pylint>=2.3.0,<3',
        'pytest<5',
        'pytest-cov<3,>=2',
    ],
)
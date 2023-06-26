from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'K Anonymity for Text first Try'
LONG_DESCRIPTION = 'A package that takes a dataframe with a corpus and return an anonymized corpus'

# Setting up
setup(
    name="Kanon4txt_try",
    version=VERSION,
    author="Liortrieman (Lior Trieman)",
    author_email="<liortr30@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # NEED TO ADD HERE ALL REQUIREMENTS!!!!!

    install_requires=["ipython==8.10.0",
                      "joblib==1.2.0",
                      "matplotlib==3.7.0",
                      "numpy==1.23.5",
                      "pandas==1.5.3",
                      "scikit_learn==1.2.1",
                      "scipy==1.10.1",
                      "setuptools==65.5.0",
                      "tqdm==4.64.1"],
    keywords=['python', 'corpus', 'stopwords', 'DBSCAN', 'generalization', 'reduction'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",

    ]
)

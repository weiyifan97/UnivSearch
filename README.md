# UnivSearch
A project aiming to find the most mentioned Universities on Quanta Magazine.

All build for **python 3**.
## Usage

Using a dedicated [virtual env](https://docs.python.org/3/tutorial/venv.html) is highly recommended.
```Shell
# Install dependencies
pip install scrapy requests bs4

# Clone this repository
git clone git@github.com/1fanwee/UnivSearch.git
cd UnivSearch
mkdir data && mkdir data/pages

# Getting names of universities from univ.cc
python getUniversities.py

# Getting urls of QM stories from Hacker News
# This is done through Hacker News Search API
python getQMLinks.py

# Scrape story content and store under data/pages
scrapy crwal QMcontent

# Analyze (using parallel processing)
python count_future.py
```

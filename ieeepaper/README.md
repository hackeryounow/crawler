### Overview
The Crawler is to retrieve a paper's references from IEEE Xplore.

### How to use
```
python .\crawl_citation.py -h
usage: crawl_citation.py [-h] [--paper_ids PAPER_IDS [PAPER_IDS ...]] [--save_dir SAVE_DIR]

Scrape Paper References from IEEE Xplore

optional arguments:
  -h, --help            show this help message and exit
  --paper_ids PAPER_IDS [PAPER_IDS ...]
                        List of IEEE paper IDs to scrape references for (default: ["8607062"])
  --save_dir SAVE_DIR   IEEE paper ID to scrape references for (default: H:\)
```
**a demo of the crawler**
```
 python .\crawl_citation.py --paper_ids 8675169 9667306 --save_dir references
```
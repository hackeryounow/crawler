### Overview

The Crawler is to retrieve a IEEE Fellow list from IEEE Fellow Directory.

### How to use

1. Download [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/).

2. Set Variables, including `path`, `driver_path`， `start_page`
```
python .\felllow.py -h
usage: felllow.py [-h] [--fellow_path FELLOW_PATH] [--chrome_driver_path CHROME_DRIVER_PATH] [--start_page START_PAGE]

Scrape Fellow List

optional arguments:
  -h, --help            show this help message and exit
  --fellow_path FELLOW_PATH
                        Path to save the Fellow list
  --chrome_driver_path CHROME_DRIVER_PATH
                        Path to the ChromeDriver executable
  --start_page START_PAGE
                        URL of the start page to scrape
```


   

   
import json
import re
import time

import requests

headers = {
        'Referer': 'https://ieeexplore.ieee.org/document/8361406/citations?tabFilter=papers',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.159 Safari/537.36",
        'Host': 'ieeexplore.ieee.org',
    }
session = requests.Session()
count = 100


def crawl_citation(paper_id):
    citation_url = f"https://ieeexplore.ieee.org/rest/document/{paper_id}/citations"

    url = citation_url
    start = 1
    citation_papers = []
    while True:
        if start >= 31:
            url = f"{citation_url}?count={count}&start={start}&type=ieee"
        resp = session.get(url, headers=headers)
        print("Citations Crawling ...")
        if resp.status_code == 200:
            resp = resp.json()
            ieee_citation = resp.get("paperCitations", None)
            if ieee_citation is not None:
                print(ieee_citation)
                related_papers = ieee_citation.get("ieee", None)
                citation_papers.extend(related_papers)
            else:
                break
        time.sleep(1)
        start = 31 if start < 31 else start + count
    print("Citations Crawling finished!")
    return citation_papers


def fetch_citation(paper_id):
    raw_citations = crawl_citation(paper_id)
    citations = []
    for raw_citation in raw_citations:
        citation = {
            "displayText": raw_citation["displayText"],
            "ieeeLink": raw_citation["links"]["documentLink"]
        }
        citations.append(citation)
    return citations


def crawl_authors(url, headers):
    url = f"{url}/authors#authors"
    resp = requests.get(url, headers=headers)
    authors = None
    if resp.status_code == 200:
        pattern = re.compile(r"^(.*)xplGlobal.document.metadata=(.*)$", re.MULTILINE)
        line = pattern.findall(resp.text)
        info = json.loads(line[0][1].replace(";", ""))
        authors = info.get("authors", None)
        # Abstract Address：https://ieeexplore.ieee.org/author/{id}
    time.sleep(3)
    return authors


def fetch_authors(url):
    url = f"https://ieeexplore.ieee.org/{url}"
    raw_authors = crawl_authors(url, headers)
    authors = []
    for raw_author in raw_authors:
        first_name = raw_author.get("firstName", "")
        second_name = raw_author.get("lastName", "")
        bio = raw_author.get("bio", None)
        bio = None if bio is None else bio.get("p", None)
        affiliation = raw_author.get("affiliation", None)
        authors.append({
            "name": raw_author.get("name", None),
            "affiliation": affiliation if affiliation is None else affiliation[0],
            "ieee_id": raw_author.get("id", None),
            "rname": f"{first_name}, {second_name}",
            "bio": bio
        })
    time.sleep(3)
    return authors


def crawl_biography(author_id, url="https://ieeexplore.ieee.org/rest/author/"):
    url = f"{url}{author_id}"
    resp = requests.get(url, headers=headers)
    bio = None
    if resp.status_code == 200:
        author_info = resp.json()[0]
        affiliations = author_info.get("currentAffiliations", None)
        bio = author_info.get("bioParagraphs", None)
        topics = author_info.get("topics", None)
        name = author_info.get("preferredName", None)
    time.sleep(3)
    return bio


def save_file(paper_id, content):
    with open(f"H:/{paper_id}.md", "a+", encoding="utf-8") as f:
        f.write(content + "\n\n")


def crawl_paper(paper_idx):
    print(f"Paper Index: {paper_idx} ...")
    papers = fetch_citation(paper_idx)
    for (paper_id, paper) in enumerate(papers):
        print(f"Citation Index: {paper_idx} - {paper_id} ...")
        ref = paper["displayText"]
        save_file(paper_idx, f"- [ ] {ref}")
        authors = fetch_authors(paper["ieeeLink"])
        for (author_id, author) in enumerate(authors):
            name = author.get("name", " ")
            rname = author.get('rname', "None")
            a_id = author.get("ieee_id", "None")
            affiliation = author.get("affiliation", " ")
            save_file(paper_idx, f"  Author: {name}")
            save_file(paper_idx, f"  AuthorInFList: {rname}")
            save_file(paper_idx, f"  Affiliation: {affiliation}")
            if a_id is None:
                bio = author["bio"]
            else:
                link = "https://ieeexplore.ieee.org/rest/author/" + a_id
                save_file(paper_idx, f"  Link: {link}")
                bio = crawl_biography(a_id)
            bio_info = f"  Biography: "

            if bio is not None:
                for bio_p in bio:
                    bio_info = bio_info + f"  {bio_p}"
            save_file(paper_idx, bio_info)


if __name__ == '__main__':
    "Given a IEEE Paper ID, you can crawl all the citations of the paper"
    # paper_ids = [8884234, 8436039, 8489986, 8675169, 9667306, 8908666, 8607062, 8892573]
    paper_ids = [8607062]
    for paper_idx in paper_ids:
        crawl_paper(paper_idx)


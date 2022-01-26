# WebScraper
[![codecov](https://codecov.io/gh/MarkTLite/WebScraper/branch/main/graph/badge.svg?token=KS779CNL3Z)](https://codecov.io/gh/MarkTLite/WebScraper)
![Test status](https://github.com/MarkTLite/WebScraper/actions/workflows/pytester.yml/badge.svg)
[![Build Status](https://app.travis-ci.com/MarkTLite/WebScraper.svg?branch=main&status=unknown)](https://app.travis-ci.com/MarkTLite/WebScraper.svg?branch=main)


## Description

This repo has code which takes input rom a companies.txt file containing a list of company names and
for each company name, the program:
<ol>
<li>Gets the google search results of the company name
<li>Gets all result URLs and picks the Homepage
<li>On the Homepage, picks out the email and writes to the output.txt file.
</ol>

## Additional Information
> Tests have been written in test_app.py

> Added CI workflow which tests for all the functionality and updates the coverage badge


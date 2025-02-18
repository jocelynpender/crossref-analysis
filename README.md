This repository contains data and code to support my preliminary explorations of Crossref data to assess correlations between depositing references and citation counts. Do members or records with the “reference” field have on average more or less incoming citations than members or records without?

Context: Consider this example metadata record in our API. It represents a research output. Note the following fields:

- “DOI” - the DOI identifier of the record, in this case 10.1016/j.jacc.2017.11.012
- “member” - the identifier of the Crossref member that deposited this record, in this case 78 (here is the corresponding member's record)
- “is-referenced-by-count” - the number of incoming citations, i.e. how many other research outputs cite 10.1016/j.jacc.2017.11.012
- “reference” - the list of bibliographic references (outgoing citations) included in this record
Not all records have a “reference” field, for example see this one. If this field is absent, it means that either there are no references included in the research output, or there are references but they were not deposited with us by the Crossref member.

Problem: We would like to explore correlations between depositing references and citation counts. Do members or records with the “reference” field have on average more or less incoming citations than members or records without?

Data sources: Over 160M records in our database. This data can be accessed through the API. Monthly data dumps are also available.


---
Category (two values): With the reference field / without the reference field
Numerical continuous integer: Number of incoming citations

I chose the last question. I liked this problem because if the analysis shows that depositing references is correlated or related to increases in incoming citations, this finding can be used as incentive to motivate data contributors and data providers to provide references in their submissions.
- A way to incentivize data providers to participate in strong metadata submission practices
- May contribute to their works being more easily found by machine data crawling, thus humans would eventually cite them more as a result

What is the mechanism? Maybe this demonstrates that works are more likely to be found and cited if references are registered with Crossref (i.e. participation in the world of linked data - you can be found more easily by all the data sources).



- What data would you need to answer the questions and how can it be gathered using available data sources?

Crossref scholarly works metadata is needed to answer the question, given is relates to better understanding Crossref citation and reference data. There is plenty of metadata in each Crossref record to play with, and given the analysis relates to understanding Crossref data itself, this is the data source needed.
Python is a convenient way to request data from APIs, given it is a fully fledged programming language with API requests functions and the pandas library which facilitates data transformation and investigation.

To better understand the data, I pulled a few sample records from Crossref's API using Python. However, given the dataset is over 160M million records, for exploratory purposes this quickly gets out of hand and as a user, it is simply not feasible to retrieve anywhere close to all data using Crossref's API, and if I tried, I'd probably overload Crossref's servers which simply wouldn't be very kind.

Instead, I downloaded a sample Crossref dataset using a torrent file (April 2024 data). These files came in json format, in 100 files. I exported the JSON files, then pushed all the data into one csv using Python.

If I wanted to run the analysis over all Crossref data, the technique would certainly be different.

I may investigate what it looks like to retrieve a data dump and push it into a lightweight database like SQLite. That way, I could connect my data analysis tool (be it Python, or a BI tool) directly to the database and have access to all data.

It may be interesting to pull reference data from a different source to evaluate what missing data from Crossref looks like, e.g., https://opencitations.net/index/coci/api/v1 OpenCitations index. E.g., how many instances exist in which there are actually no references in the work vs. none deposited?

- What kind of tools or techniques would you use to answer the questions? How would you communicate the findings?
Tools I'd use to pull the data:
- Python
- If needed, pull entire dump and leverage SQLite + doi2sqlite
- Other databases: Snowflake, postgres

Tools to transform the data:
- Python

Tools to analyze the data:
- Python, BI tools to quickly explore, Jupyter notebook

Techniques to answer stated questions:
- Boxplots, descriptive statistics
- t-tests, other tests as needed
- Log transformation, linear regression
- Bar charts

  
First, I tend to explore the data with no direction - plotting things arbitrary to see what trends I can find and what story lines to pull. I like using BI tools (e.g., Tableau) to do this.

To communicate my findings, I always try to build a streamlined path of discovery to take the viewer on. Pulling on the most relevant or significant threads I found in my explorations. A combination of plots, charts, high-level metrics, with words, descriptions, callouts and clear visualization would assist to direct the viewer towards what I want them to understand.

- What kind of tools would you use for a one-off analysis? What if we wanted to monitor the situation over time?

One-off:
- APIs to pull sampling of data, Python, Jupyter notebok, scripts, RStudio, R notebook, Tableau/Power BI, 
Monitor the situation over time:
- Build a data warehouse with data needed for the analysis (e.g., snowflake), aggregations of the data for easy exploration, BI dashboard for monitoring, dbt for transformations, Azure data science tools (ADF), Azure machine learning, AWS tools - more so, data engineering tools


- What do you see as the biggest challenge and what are some limitations?

Challenges:
- Based on my very quick analysis, I noticed that there are many outliers - mega-publications that are cited significantly more frequently than others. The dataset appears unbalanced (extremely long tail, skewed), and number of citations (incoming) are not normally distributed. This possess some challenges towards what analysis techniques apply, given many assume a normal distribution of data (would invalidate assumptions).
- The data volume is huge which poses a huge challenge towards performing an exhaustive analysis. Likely, a data pipeline would have to be developed that aggregates the data before storing it for use in such investigations.
- The question of whether missing data should be true zeros or not is always a challenge!


- Are there any interesting additional questions or paths we might want to explore?

I'd like to explore whether the trends I found in the sample dataset apply across all 160 million records, whether the findings will be different within domains (I assume there are different norms of behaviour in different research domains).
As well, how these trends/findings change over time. The familiarity with depositing data & overall open science culture will definitely be different over time as more scientists recognize the importance of linked and machine interpretable data. As well, best practices may have emerged and become more embedded in norms and culture.
As well, the differences between publishers. Do some publishers / members behave differently, and do the trends hold?
There's certainly a time factor here in terms of number of incoming citations: the number of times a paper or work is cited will increase over time, and is directly related to the year of publication. We may wish to normalize the data with some sort of model/relationship of # citations over time since year of publication.

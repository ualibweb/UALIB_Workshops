# Data Reuse Notes

Dataset for Today to create a Co-author Network
“UA_pubmed_authors.tsv” dataset: 

rows are PMID articles, and columns are the article authors. The following
EDirect script was used to collect the data:

esearch -db pubmed -query "(\"university of alabama\"[AFFL] AND tuscaloosa[AFFL])" | \
efetch -format xml | \
xtract -pattern PubmedArticle -element MedlineCitation/PMID -block Author -def "N/A" -element LastName
Initials > UA_pubmed_authors.tsv

The Bibliographic data is credited to NCBI and NLM. Please see the NCBI Website and Data Usage Policies
and Disclaimers for more information regarding the data: https://www.ncbi.nlm.nih.gov/home/about/policies

The results return hits with any author with a “University of Alabama” AND “Tuscaloosa” aﬃliation
somewhere in the aﬃliation ﬁeld (1 or more authors). A few warnings:

- This is a quick demo dataset
- We did not cleanup false positive hits (e.g., University of Alabama Birmingham and a Tuscaloosa company would match our query)
- We did not disambiguate or normalize author names - to do that, we would recommend looking at something like ORCID or Scopus Author IDs

Take home message: If you are doing this for real research, you need to spend some time cleaning up and normalizing data!



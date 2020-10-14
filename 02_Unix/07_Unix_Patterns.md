# Pattern Searching

**Lesson Navigation**

1. [Introduction and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/01_Unix_Introduction.md)
2. [Navigating Files and Directories](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/02_Unix_Navigating.md)
3. [Viewing Files and Counting](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/03_Unix_Viewing_Counting.md)
4. [Sorting and Finding Duplicates](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/04_Unix_Sorting_Duplicates.md)
5. [Merging Files and Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/05_Unix_Merging.md)
6. [Comparing Files](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/06_Unix_Comparing.md)
7. [Pattern Searching](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/07_Unix_Patterns.md)
8. [Repeating Tasks with Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/08_Unix_Loops.md)

## Finding or Filtering Specific Lines

A useful utility for finding patterns in files is `grep`. The `grep` utility prints lines that match an input pattern to the standard output. In this brief introduction, our pattern will be a regular word, however `grep` can find highly complex patterns in files with the use of [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression). 

Navigate back to the `/Udata/PubMed` folder:

```console

user@computer:~$ cd /home/user/Desktop/Udata/PubMed

```
Let's use `grep` to find all lines containing "biology" in the PubMed_Search_combined.txt file:

```console

user@computer:~$ grep "biology" PubMed_Search_combined.txt
26895861	Letcher	PM	An ultrastructural study of Paraphysoderma sedebokerense (Blastocladiomycota), an epibiotic parasite of microalgae.	Fungal biology	2016	120	3	324-37
26638196	DeCaro	JA	Beyond catecholamines: Measuring autonomic responses to psychosocial context.	American journal of human biology : the official journal of the Human Biology Council	2016	28	3	309-17
26593149	Decaro	JA	Household-level predictors of maternal mental health and systemic inflammation among infants in Mwanza, Tanzania.	American journal of human biology : the official journal of the Human Biology Council	2016	28	4	461-70
26567016	Chen	FR	Hypothalamic pituitary adrenal activity and autonomic nervous system arousal predict developmental trajectories of children's comorbid behavior problems.	Developmental psychobiology	2016	58	3	393-405
...
...
30257078	Adl	SM	Revisions to the Classification, Nomenclature, and Diversity of Eukaryotes.	The Journal of eukaryotic microbiology	2019	66	1	4-119
30136386	Urakawa	H	Ecological response of nitrification to oil spills and its impact on the nitrogen cycle.	Environmental microbiology	2019	21	1	18-33
30099810	Lehnen	LP	Cytochemical Localization of Polyphenol Oxidase Activity in K2-Bodies of Saprolegnia ferax Secondary Zoospores.	The Journal of eukaryotic microbiology	2019	66	3	404-412

```

Note that by default `grep` will match "biology" within words such as "microbiology". If we want to prevent this behavior, we can add the `-w` option to match whole words:

```console

user@computer:~$ grep -w "biology" PubMed_Search_combined.txt

```
Further, `grep` is case sensitive, so if we want to match "biology" OR "Biology" we can add the `-i` option to ignore case:

```console

user@computer:~$ grep -w -i "biology" PubMed_Search_combined.txt

```

`grep` results can be piped to another `grep` command. For example, we can take the above `grep` command and pipe it to `grep` to find matches for "Powell":

```console

user@computer:~$ grep -w -i "biology" PubMed_Search_combined.txt | grep "Powell"
28606351	Powell	MJ	Ultrastructural characterization of the host-parasite interface between Allomyces anomalus (Blastocladiomycota) and Rozella allomycis (Cryptomycota).	Fungal biology	121	6-7	561-572
30709516	Powell	MJ	Ultrastructure of early stages of Rozella allomycis (Cryptomycota) infection of its host, Allomyces macrogynus (Blastocladiomycota).	Fungal biology	2019	123	2	109-116
30342620	Powell	MJ	Zopfochytrium is a new genus in the Chytridiales with distinct zoospore ultrastructure.	Fungal biology	2018	122	11	1041-1049
30709516	Powell	MJ	Ultrastructure of early stages of Rozella allomycis (Cryptomycota) infection of its host, Allomyces macrogynus (Blastocladiomycota).	Fungal biology	2019	123	2	109-116
```
---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

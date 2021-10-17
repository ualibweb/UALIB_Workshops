# grep

**Lesson Navigation**

  1. [Introduction](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/01_Unix2_Introduction.md)
  2. [cat, tac, head, and tail](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/02_Unix2_cat_tac_head_tail.md)
  3. [wc and nl](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/03_Unix2_wc_and_nl.md)
  4. [sort, uniq, and cut](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/04_Unix2_sort_uniq_cut.md)
  5. [split and shuf](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/05_Unix2_split_and_shuf.md)
  6. [paste and join](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/06_Unix2_paste_and_join.md)
  7. [tr and sed](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/07_Unix2_tr_and_sed.md)
  8. [grep](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/08_Unix2_grep.md)
  9. [diff and comm](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix2_fall_2021/09_Unix2_diff_and_comm.md)

# grep

A utility for finding patterns in files is `grep`. The `grep` utility prints lines that match an input pattern to the standard output. 

Navigate back to the `/Udata2/PubMed` folder:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/PubMed

```

First, combine the PubMed search files into one file using `cat`:

```console

user@computer:~$ cat PubMed_Search*.txt > PubMed_Search_combined.txt

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

In the above examples, we searched for literal word patterns, however `grep` can find highly complex patterns in files through the use of [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression). Here is a basic example:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/Filter
user@computer:~$ grep 'InChI=1S/C[0-9][0-9]H[0-9][0-9]N2' CID2734162_sim1000.inchi
InChI=1S/C15H28N2/c1-2-3-4-5-6-7-8-9-10-11-13-17-14-12-16-15-17/h12,14-15H,2-11,13H2,1H3
InChI=1S/C13H24N2/c1-2-3-4-5-6-7-8-9-11-15-12-10-14-13-15/h10,12-13H,2-9,11H2,1H3
InChI=1S/C11H20N2/c1-2-3-4-5-6-7-9-13-10-8-12-11-13/h8,10-11H,2-7,9H2,1H3
InChI=1S/C10H18N2/c1-2-3-4-5-6-8-12-9-7-11-10-12/h7,9-10H,2-6,8H2,1H3
InChI=1S/C12H22N2/c1-2-3-4-5-6-7-8-10-14-11-9-13-12-14/h9,11-12H,2-8,10H2,1H3
InChI=1S/C21H40N2/c1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-19-23-20-18-22-21-23/h18,20-21H,2-17,19H2,1H3
InChI=1S/C10H19N2.ClH/c1-3-4-5-6-7-12-9-8-11(2)10-12;/h8-10H,3-7H2,1-2H3;1H/q+1;/p-1
InChI=1S/C10H19N2/c1-3-4-5-6-7-12-9-8-11(2)10-12/h8-10H,3-7H2,1-2H3/q+1
InChI=1S/C11H21N2.ClH/c1-4-5-6-7-8-13-10-9-12(3)11(13)2;/h9-10H,4-8H2,1-3H3;1H/q+1;/p-1
InChI=1S/C11H21N2/c1-4-5-6-7-8-13-10-9-12(3)11(13)2/h9-10H,4-8H2,1-3H3/q+1
InChI=1S/C12H23N2.ClH/c1-3-4-5-6-7-8-9-14-11-10-13(2)12-14;/h10-12H,3-9H2,1-2H3;1H/q+1;/p-1
InChI=1S/C12H23N2/c1-3-4-5-6-7-8-9-14-11-10-13(2)12-14/h10-12H,3-9H2,1-2H3/q+1
InChI=1S/C14H27N2.ClH/c1-3-4-5-6-7-8-9-10-11-16-13-12-15(2)14-16;/h12-14H,3-11H2,1-2H3;1H/q+1;/p-1
InChI=1S/C14H27N2/c1-3-4-5-6-7-8-9-10-11-16-13-12-15(2)14-16/h12-14H,3-11H2,1-2H3/q+1
...
...
```
The above regular expression `InChI=1S/C[0-9][0-9]H[0-9][0-9]N2` matches InChI strings (`InChI=1S/`) that start with the molecular formula `CnnHnnN2`, where `n` is a digit.

## References and Further Reading

* [GNU grep Manual](https://www.gnu.org/software/grep/manual/grep.html#Regular-Expressions)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

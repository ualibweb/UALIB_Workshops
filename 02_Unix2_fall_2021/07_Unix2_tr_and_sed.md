# tr and sed

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

# tr

`tr` translates or deletes characters. It can be useful for cleaning data and simple transformations. Navigate to the `/Udata2/Sorting` folder with `cd`:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/Sorting

```

First, isolate the first column of `molecules.smi` using `cut`:

```console

user@computer:~$ cut -f1 molecules.smi
CC1C[C@H]2CC=CC[C@H]2CC1C
CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C
CC/C=C/1\CCC2CC(CCC2C1)C
CC1CC2CCCC=C2C(C1(C)C)(C)C
CCC[C@@H]1CCC(C2=CCCC=C12)C
CC1CCCCC1C2=CC=CCC2
CC1C[C@H]2CC=CC[C@H]2CC1C
CC/C=C/1\CCC2CC(CCC2C1)C
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C
```

Next, let's say we needed to delete all `@` characters. We can do this with `tr` and the `-d` option:

```console

user@computer:~$ cut -f1 molecules.smi | tr -d '@'
CC1C[CH]2CC=CC[CH]2CC1C
CC1=CCC[C]2([CH]1C[CH](CC2)C(=C)C)C
C[CH]1CC[CH](C2=CC(=C)CCC12)C(C)C
CC/C=C/1\CCC2CC(CCC2C1)C
CC1CC2CCCC=C2C(C1(C)C)(C)C
CCC[CH]1CCC(C2=CCCC=C12)C
CC1CCCCC1C2=CC=CCC2
CC1C[CH]2CC=CC[CH]2CC1C
CC/C=C/1\CCC2CC(CCC2C1)C
C[CH]1CC[CH](C2=CC(=C)CCC12)C(C)C
```

Another use of `tr` is to replace characters. Let's say we wanted to isolate the first hash of the InChiKey in column 2, and then replace the `-` with `#`:

```console

user@computer:~$ cut -f2 molecules.smi | cut -c1-15 | tr '-' '#'
MERJPGYKGRUPDP#
OZQAPQSEYFAMCY#
RNDFUOKDULDZPR#
WSTKIWSHWCBHED#
WLZHEXZCQNVIOB#
UUIJJZRFSATZAR#
ONWJTPPDINXBJV#
MERJPGYKGRUPDP#
WSTKIWSHWCBHED#
RNDFUOKDULDZPR#
```

Another use-case of `tr` is for preparing text for text analysis. For example, we can select the titles from the `PubMed_Search_2015.txt` file and then lowercase all text:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/PubMed
user@computer:~$ cut -f4 PubMed_Search_2015.txt | tr '[:upper:]' '[:lower:]'
caregiver and care recipient characteristics as predictors of psychotropic medication use in community-dwelling dementia patients.
exploring rating quality in rater-mediated assessments using mokken scale analysis.
malingering by proxy: a literature review and current perspectives.
us mortality: influence of race, geography and cardiovascular risk among participants in the population-based regards cohort.
facile and high-yielding synthesis of tam biradicals and monofunctional tam radicals.
the effect of social support on quality of life in older adults receiving cognitive behavioral therapy
...
...

```

Finally, if we wanted all of the titles on one continuous line, we can pipe the results to `tr` again, and replace the newline character (`\n`) with a space:

```console

user@computer:~$ cut -f4 PubMed_Search_2015.txt | tr '[:upper:]' '[:lower:]' | tr '\n' ' '
caregiver and care recipient characteristics as predictors of psychotropic medication use in community-dwelling dementia patients. exploring rating quality in rater-mediated assessments using mokken scale analysis. malingering by proxy: a literature review and current perspectives. us mortality: influence of race, geography and cardiovascular risk among participants in the population-based regards cohort. facile and high-yielding synthesis of tam biradicals and monofunctional tam radicals. the effect of social support on quality of life in older adults receiving cognitive behavioral therapy. ...
```

# sed

`sed` can perform text transformations. It works on strings, in contrast to characters like in `tr`. We'll look at two basic use-cases. First, navigate to `/Udata2/toolkit_process` folder with `cd`:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/toolkit_process

```

Next, let's replace the string `InChI` with `StandardInChI` on each line in the file `tool_process01.inchi`. According to the `info` document for `sed` , we can do this with the substitute notation `'s/REGEXP/REPLACEMENT/[FLAGS]/'`:

```console

user@computer:~$ sed 's/InChI/StandardInChI/' tool_process01.inchi
StandardInChI=1S/H	0
StandardInChI=1S/H/i1+0	1
StandardInChI=1S/H/i1+1	2
StandardInChI=1S/H/i1+2	3
StandardInChI=1S/H/i1+3	4
StandardInChI=1S/H/i1+4	5
StandardInChI=1S/H/i1+5	6
StandardInChI=1S/H/i1+6	7
StandardInChI=1S/He	8
StandardInChI=1S/He/i1-1	9
...
...
```

Rather than using `sed` for simple literal find/replace string operations, a more powerful use-case would be to use a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) to match a pattern. Navigate to `/Udata2/Elements_Isotopes` and view the `IUPAC_elements_isotopes.smi` file with `head`: 

```console

user@computer:~$ cd /home/user/Desktop/Udata2/Elements_Isotopes
user@computer:~$ head -n20 IUPAC_elements_isotopes.smi 
[H]	0
[1H]	1
[2H]	2
[3H]	3
[4H]	4
[5H]	5
[6H]	6
[7H]	7
[He]	8
[3He]	9
[4He]	10
[5He]	11
[6He]	12
[7He]	13
[8He]	14
[9He]	15
[10He]	16
[Li]	17
[4Li]	18
[5Li]	19
```

This file is a list of all IUPAC elements and isotopes in SMILES format. Let's say, however, we wanted a list of only the standard elements, eliminating the isotope specifications. We can do this using a regular expression and `sed` as follows:

```console

user@computer:~$ sed '/^\[[0-9]/d' IUPAC_elements_isotopes.smi 
[H]	0
[He]	8
[Li]	17
[Be]	28
[B]	41
[C]	55
[N]	71
[O]	88
[F]	106
[Ne]	125
[Na]	146
[Mg]	168
[Al]	191
[Si]	215
[P]	239
[S]	264
[Cl]	289
[Ar]	315
[K]	341
...
...
```

The regular expression pattern, `^\[[0-9]` matches lines that start with `[` followed by any digit. The `d` flag in `sed` says to delete any lines matching the pattern. This is hard to find in the `sed` documentation, but there is an example in section 3.1 of the online `sed` documentation (link below).

## References and Further Reading

* [GNU Coreutils - tr](https://www.gnu.org/software/coreutils/manual/coreutils.html#tr-invocation)
* [GNU sed](https://www.gnu.org/software/sed/manual/sed.html)

Two excellent videos on `tr` and `sed`:

* [Learning Sed is Beneficial For Linux Users](https://www.youtube.com/watch?v=EACe7aiGczw)
* [Two Powerful Command Line Utilities 'cut' And 'tr'](https://www.youtube.com/watch?v=_0IFtMFYroU)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

# wc and nl

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

# wc

A useful utility is `wc`, which counts the number of lines, words, and byte counts in text files. Let's try to use `wc` on one of the files in the `/Udata2/PubMed` folder:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/PubMed

```

```console

user@computer:~$ wc PubMed_Search_2015.txt
  383  9756 68017 PubMed_Search_2015.txt

```

Each PubMed_search file represents a separate sample PubMed search saved with one record per line. So, if we want to quickly find the number of records in each of the files in the `/Udata2/PubMed` folder, we can use `wc` with the `-l` option for lines only, and a wildcard, `*` for all .txt files in the folder:

```console

user@computer:~$ wc -l PubMed*.txt
   383 PubMed_Search_2015.txt
   393 PubMed_Search_2016.txt
   479 PubMed_Search_2017.txt
   566 PubMed_Search_2018.txt
   575 PubMed_Search_2019.txt
  2396 total

```

Another example use-case of `wc` is to quickly spot errors in lengths of files. For example, the .inchi files in the `/Udata2/toolkit_process` folder represent the output of a computation from a script. A successful script run should have exactly 125 lines, meaning that all of the input data lines were processed and saved. Let's take a look:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/toolkit_process

```

```console

user@computer:~$ wc -l tool_process*.inchi
  125 tool_process01.inchi
  125 tool_process02.inchi
  125 tool_process03.inchi
   99 tool_process04.inchi
  125 tool_process05.inchi
  125 tool_process06.inchi
  125 tool_process07.inchi
  125 tool_process08.inchi
  974 total

```

We can quickly see that the tool_process04.inchi file has an issue. This is quite useful, particularly when you may have 100s of files to check.


# nl

`nl` numbers lines of files. It can be useful, for example, to quickly add an index column to a data file. Let's try this with the `molecules.smi` file in the `/Udata2/Sorting` folder:


```console

user@computer:~$ cd /home/user/Desktop/Udata2/Sorting

```

```console

user@computer:~$ nl molecules.smi
     1	CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
     2	CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C	OZQAPQSEYFAMCY-SOUVJXGZSA-N	10726905
     3	C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125
...
...
```

The option `-n` with `ln` format is useful to remove the leading space:

```console

user@computer:~$ nl molecules.smi -n ln

```

We can also combine `nl` with pipes, for example, to number the lines of our previous `wc` analysis:

```console
user@computer:~$ wc -l PubMed*.txt | nl -n ln
1     	   383 PubMed_Search_2015.txt
2     	   393 PubMed_Search_2016.txt
3     	   479 PubMed_Search_2017.txt
4     	   566 PubMed_Search_2018.txt
5     	   575 PubMed_Search_2019.txt
6     	  2396 total

```

## References and Further Reading

* [GNU Coreutils - wc](https://www.gnu.org/software/coreutils/manual/coreutils.html#wc-invocation)
* [GNU Coreutils - nl](https://www.gnu.org/software/coreutils/manual/html_node/nl-invocation.html)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

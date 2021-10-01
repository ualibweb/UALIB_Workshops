# Viewing Files and Counting

**Lesson Navigation**

1. [Introduction and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/01_Unix_Introduction.md)
2. [Navigating Files and Directories](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/02_Unix_Navigating.md)
3. [Viewing Files and Counting](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/03_Unix_Viewing_Counting.md)
4. [Sorting and Finding Duplicates](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/04_Unix_Sorting_Duplicates.md)
5. [Merging Files and Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/05_Unix_Merging.md)
6. [Comparing Files](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/06_Unix_Comparing.md)
7. [Pattern Searching](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/07_Unix_Patterns.md)
8. [Repeating Tasks with Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/08_Unix_Loops.md)

## Viewing Text Files

One way to view text files is to print the content to standard output (your terminal window) using `cat`. Let's take a look at the CID_51351709_similar.txt file located in the `/Udata/View` folder. First, use `cd` to change your directory to the folder:

```console

user@computer:~$ cd /home/user/Desktop/Udata/View

```
We can then use the `cat` utility to print the content to standard output:

```console

user@computer:~$ cat CID_51351709_similar.txt
CC.CC1CCC2CC(=C(CC2C1)C=C)C=C	154673141	232.400
CC1CCCCC1C2=CC=CCC2	154546688	176.300
CC1CCCC2C1=CC=C3C2C=CC=C3	154307178	198.300
CCC1=CC=C2C(C1)C(CCC2(C)C)(C)C	154280750	218.380
CC1C(=C)CCC2C1=CC=CC2	154236167	160.250
CC(=C)C1CCC2CCC=CC2C1	153974464	176.300
CC1CCC(C2C1C(C=CC2C)C)C	153940528	192.340
[2H]C1C=CC2=CC=C3C(C(C(C(C3(C2(C1([2H])[2H])[2H])[2H])([2H])[2H])([2H])C)([2H])[2H])([2H])[2H]	153707997	212.390
[2H]C1C=C2C(C(C(C(C2(C(C1([2H])[2H])([2H])[2H])[2H])([2H])[2H])([2H])[2H])([2H])C)([2H])C	153707996	176.360
CC1CCC(CC1)C2=CC(C(C=C2)C)C	153688226	204.350
CC1CCC(C2C1C(=CC=C2C)C)C	153685997	190.320
C[C@@H]1CCCC2C1C=CC=C2	153645273	148.240
CC(C)C1CCCC2C1C(=CC=C2)C(C)C	153428729	218.380
CC(C)C1C2C=CC=CC2C(C3C1C=CC=C3)C(C)C	153306371	268.400
CCCC1CC(C2C(C(C(=CC2C1C)CCC)C)C)C	153303907	276.500
CC1CC(C2CC(=CC(C2C1C)C)C)C	153303900	206.370
...
...
```

It is usually a good idea to look at a preview of the file first, so we don't unnecessarily print 1000s of lines to the standard output with `cat`. Instead of `cat`, we can use `head` to view the first 10 lines:

```console

user@computer:~$ head CID_51351709_similar.txt
CC.CC1CCC2CC(=C(CC2C1)C=C)C=C	154673141	232.400
CC1CCCCC1C2=CC=CCC2	154546688	176.300
CC1CCCC2C1=CC=C3C2C=CC=C3	154307178	198.300
CCC1=CC=C2C(C1)C(CCC2(C)C)(C)C	154280750	218.380
CC1C(=C)CCC2C1=CC=CC2	154236167	160.250
CC(=C)C1CCC2CCC=CC2C1	153974464	176.300
CC1CCC(C2C1C(C=CC2C)C)C	153940528	192.340
[2H]C1C=CC2=CC=C3C(C(C(C(C3(C2(C1([2H])[2H])[2H])[2H])([2H])[2H])([2H])C)([2H])[2H])([2H])[2H]	153707997	212.390
[2H]C1C=C2C(C(C(C(C2(C(C1([2H])[2H])([2H])[2H])[2H])([2H])[2H])([2H])[2H])([2H])C)([2H])C	153707996	176.360

```

Further, we can specify the number of lines printed to standard output with `head` by adding the `-n` option followed by a digit. For example, the first 4 lines:

```console

user@computer:~$ head -n 4 CID_51351709_similar.txt
CC.CC1CCC2CC(=C(CC2C1)C=C)C=C	154673141	232.400
CC1CCCCC1C2=CC=CCC2	154546688	176.300
CC1CCCC2C1=CC=C3C2C=CC=C3	154307178	198.300
CCC1=CC=C2C(C1)C(CCC2(C)C)(C)C	154280750	218.380

```

Alternatively, you can use the program `less` to view the file in parts, allowing scrolling or arrow key navigation:

```console

user@computer:~$ less CID_51351709_similar.txt

```

Use `q` to exit `less`.


## Counting

A useful utility is `wc`, which counts the number of lines, words, and byte counts in text files. Let's try to use `wc` on one of the files in the `/Udata/PubMed` folder:

```console

user@computer:~$ cd /home/user/Desktop/Udata/PubMed

```

```console

user@computer:~$ wc PubMed_Search_2015.txt
  383  9756 68017 PubMed_Search_2015.txt

```

Each PubMed_search file represents a separate sample PubMed search saved with one record per line. So, if we want to quickly find the number of records in each of the files in the `/Udata/PubMed` folder, we can use `wc` with the `-l` option for lines only, and a wildcard, `*` for all .txt files in the folder:

```console

user@computer:~$ wc -l *.txt
   383 PubMed_Search_2015.txt
   393 PubMed_Search_2016.txt
   479 PubMed_Search_2017.txt
   566 PubMed_Search_2018.txt
   575 PubMed_Search_2019.txt
  2396 total

```

Another example use-case of `wc` is to quickly spot errors in lengths of files. For example, the .inchi files in the `/Udata/toolkit_process` folder represent the output of a computation from a script. A successful script run should have exactly 125 lines, meaning that all of the input data lines were processed and saved. Let's take a look:

```console

user@computer:~$ cd /home/user/Desktop/Udata/toolkit_process

```

```console

user@computer:~$ wc -l *.inchi
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

## References and Further Reading

* [GNU Coreutils - cat: Concatenate and write files](https://www.gnu.org/software/coreutils/manual/coreutils.html#cat-invocation)
* [GNU Coreutils - head: Output the first part of files](https://www.gnu.org/software/coreutils/manual/coreutils.html#head-invocation)
* [less program](https://en.wikipedia.org/wiki/Less_(Unix))
* [GNU Coreutils - wc: Print newline, word, and byte counts](https://www.gnu.org/software/coreutils/manual/coreutils.html#wc-invocation)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

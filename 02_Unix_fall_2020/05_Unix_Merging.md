# Merging Files and Data

**Lesson Navigation**

1. [Introduction and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/01_Unix_Introduction.md)
2. [Navigating Files and Directories](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/02_Unix_Navigating.md)
3. [Viewing Files and Counting](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/03_Unix_Viewing_Counting.md)
4. [Sorting and Finding Duplicates](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/04_Unix_Sorting_Duplicates.md)
5. [Merging Files and Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/05_Unix_Merging.md)
6. [Comparing Files](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/06_Unix_Comparing.md)
7. [Pattern Searching](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/07_Unix_Patterns.md)
8. [Repeating Tasks with Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/08_Unix_Loops.md)

## Merging Files

We have used the `cat` utility throughout this workshop to print the contents of a file to the standard output. Another use of `cat` is to concatenate multiple files into one file. First, navigate to the `/Udata/PubMed` folder with `cd`:

```console

user@computer:~$ cd /home/user/Desktop/Udata/PubMed

```

Let's say we want to combine all of the PubMed Search files into one file. We can use `cat` and a wildcard `*` to match the files. Since we already know these files have many lines, we will use `>` to redirect the output to a new file:

```console

user@computer:~$ cat PubMed_Search*.txt > PubMed_Search_combined.txt

```

## Merging Data by Field Value

Another useful function to combine data is `join`, which joins lines of two files by a common index field. `cd` to the folder `/Udata/Joining` and `cat` the jmols01.txt and jmols02.txt files:

```console

user@computer:~$ cat jmols01.txt
ZHAOHDRTWMBHER-MRVPVSSYSA-N	CC=C[C@@H]1CC(=O)CCO1	149501208
ZHAOHDRTWMBHER-UHFFFAOYSA-N	CC=CC1CC(=O)CCO1	140006540
QGHJAGNQZQUZPO-UHFFFAOYSA-N	C1C2C=CC(O2)CC1=O.[Y]	135045719
DJXYBPVHUSVRLJ-KNVOCYPGSA-N	C1[C@@H]2C=C[C@@H](O2)CC1=O	5325223
DJXYBPVHUSVRLJ-UHFFFAOYSA-N	C1C2C=CC(O2)CC1=O	557672

user@computer:~$ cat jmols02.txt
ZHAOHDRTWMBHER-MRVPVSSYSA-N	C8H12O2	140.180	10
ZHAOHDRTWMBHER-UHFFFAOYSA-N	C8H12O2	140.180	10
QGHJAGNQZQUZPO-UHFFFAOYSA-N	C7H8O2Y	213.040	10
DJXYBPVHUSVRLJ-KNVOCYPGSA-N	C7H8O2	124.140	9
DJXYBPVHUSVRLJ-UHFFFAOYSA-N	C7H8O2	124.140	9

```

We can see that the jmols01.txt and jmols02.txt files have related data. If we want to use `join`, the first task we need to do is use `sort` and sort the files by the column that we want to use as the index field for `join`. In this case, we will select the first column as the index field, save the sorted (by field 1) output to new files, then use `join` to join the data:

```console

user@computer:~$ sort -k1,1 jmols01.txt > jmols01.sorted
user@computer:~$ sort -k1,1 jmols02.txt > jmols02.sorted
user@computer:~$ join jmols01.sorted jmols02.sorted
DJXYBPVHUSVRLJ-KNVOCYPGSA-N C1[C@@H]2C=C[C@@H](O2)CC1=O 5325223 C7H8O2 124.140 9
DJXYBPVHUSVRLJ-UHFFFAOYSA-N C1C2C=CC(O2)CC1=O 557672 C7H8O2 124.140 9
QGHJAGNQZQUZPO-UHFFFAOYSA-N C1C2C=CC(O2)CC1=O.[Y] 135045719 C7H8O2Y 213.040 10
ZHAOHDRTWMBHER-MRVPVSSYSA-N CC=C[C@@H]1CC(=O)CCO1 149501208 C8H12O2 140.180 10
ZHAOHDRTWMBHER-UHFFFAOYSA-N CC=CC1CC(=O)CCO1 140006540 C8H12O2 140.180 10

```
By default, `join` uses the first column field as the common join field. You can, however, use options to select specific column fields to indicate the common join field. Let's look at the file jmols_df.txt:

```console

user@computer:~$ cat jmols01_df.txt
CC=C[C@@H]1CC(=O)CCO1	149501208	ZHAOHDRTWMBHER-MRVPVSSYSA-N
CC=CC1CC(=O)CCO1	140006540	ZHAOHDRTWMBHER-UHFFFAOYSA-N
C1C2C=CC(O2)CC1=O.[Y]	135045719	QGHJAGNQZQUZPO-UHFFFAOYSA-N
C1[C@@H]2C=C[C@@H](O2)CC1=O	5325223	DJXYBPVHUSVRLJ-KNVOCYPGSA-N
C1C2C=CC(O2)CC1=O	557672	DJXYBPVHUSVRLJ-UHFFFAOYSA-N

```
Next, sort by column 3:

```console

user@computer:~$ sort -k3,3 jmols01_df.txt > jmols01_df.sorted
user@computer:~$ cat jmols01_df.sorted
C1[C@@H]2C=C[C@@H](O2)CC1=O	5325223	DJXYBPVHUSVRLJ-KNVOCYPGSA-N
C1C2C=CC(O2)CC1=O	557672	DJXYBPVHUSVRLJ-UHFFFAOYSA-N
C1C2C=CC(O2)CC1=O.[Y]	135045719	QGHJAGNQZQUZPO-UHFFFAOYSA-N
CC=C[C@@H]1CC(=O)CCO1	149501208	ZHAOHDRTWMBHER-MRVPVSSYSA-N
CC=CC1CC(=O)CCO1	140006540	ZHAOHDRTWMBHER-UHFFFAOYSA-N

```

We can join jmols01_df.sorted with jmols02.sorted by adding a field option `-1` and `-2` for files 1 and 2, respectively. First, identify which field you want to join:

```console

user@computer:~$ cat jmols01_df.sorted
C1[C@@H]2C=C[C@@H](O2)CC1=O	5325223	DJXYBPVHUSVRLJ-KNVOCYPGSA-N
C1C2C=CC(O2)CC1=O	557672	DJXYBPVHUSVRLJ-UHFFFAOYSA-N
C1C2C=CC(O2)CC1=O.[Y]	135045719	QGHJAGNQZQUZPO-UHFFFAOYSA-N
CC=C[C@@H]1CC(=O)CCO1	149501208	ZHAOHDRTWMBHER-MRVPVSSYSA-N
CC=CC1CC(=O)CCO1	140006540	ZHAOHDRTWMBHER-UHFFFAOYSA-N
user@computer:~$ cat jmols02.sorted
DJXYBPVHUSVRLJ-KNVOCYPGSA-N	C7H8O2	124.140	9
DJXYBPVHUSVRLJ-UHFFFAOYSA-N	C7H8O2	124.140	9
QGHJAGNQZQUZPO-UHFFFAOYSA-N	C7H8O2Y	213.040	10
ZHAOHDRTWMBHER-MRVPVSSYSA-N	C8H12O2	140.180	10
ZHAOHDRTWMBHER-UHFFFAOYSA-N	C8H12O2	140.180	10

```

If we want to select the InChIKeys as the common field:

```console

user@computer:~$ join -1 3 -2 1 jmols01_df.sorted jmols02.sorted
DJXYBPVHUSVRLJ-KNVOCYPGSA-N C1[C@@H]2C=C[C@@H](O2)CC1=O 5325223 C7H8O2 124.140 9
DJXYBPVHUSVRLJ-UHFFFAOYSA-N C1C2C=CC(O2)CC1=O 557672 C7H8O2 124.140 9
QGHJAGNQZQUZPO-UHFFFAOYSA-N C1C2C=CC(O2)CC1=O.[Y] 135045719 C7H8O2Y 213.040 10
ZHAOHDRTWMBHER-MRVPVSSYSA-N CC=C[C@@H]1CC(=O)CCO1 149501208 C8H12O2 140.180 10
ZHAOHDRTWMBHER-UHFFFAOYSA-N CC=CC1CC(=O)CCO1 140006540 C8H12O2 140.180 10

```

In the above `join` operation, the `-1 3` option represents jmols01_df.sorted (file 1), column field 3, and the `-2 1` option represents jmols02.sorted (file 2), column field 1. 

There are many other options for `join` ([see GNU Manual for join](https://www.gnu.org/software/coreutils/manual/coreutils.html#join-invocation)) such as specifying the output format in a field list in the form `-o m.n,m.n,...` where `m` is the file number and `n` is the field number. For example, if we wanted the output order to be columns 1, 2, and 3 from jmols01_df.sorted (file 1) and then columns 2 and 3 from jmols02.sorted, the option syntax is as follow: `1.1,1.2,1.3,2.2,2.3`


```console

user@computer:~$ join -1 3 -2 1 -o 1.1,1.2,1.3,2.2,2.3 jmols01_df.sorted jmols02.sorted
C1[C@@H]2C=C[C@@H](O2)CC1=O 5325223 DJXYBPVHUSVRLJ-KNVOCYPGSA-N C7H8O2 124.140
C1C2C=CC(O2)CC1=O 557672 DJXYBPVHUSVRLJ-UHFFFAOYSA-N C7H8O2 124.140
C1C2C=CC(O2)CC1=O.[Y] 135045719 QGHJAGNQZQUZPO-UHFFFAOYSA-N C7H8O2Y 213.040
CC=C[C@@H]1CC(=O)CCO1 149501208 ZHAOHDRTWMBHER-MRVPVSSYSA-N C8H12O2 140.180
CC=CC1CC(=O)CCO1 140006540 ZHAOHDRTWMBHER-UHFFFAOYSA-N C8H12O2 140.180

```
## References and Further Reading

* [GNU Coreutils - cat: Concatenate and write files](https://www.gnu.org/software/coreutils/manual/coreutils.html#cat-invocation)
* [GNU Coreutils - sort: Sort text files](https://www.gnu.org/software/coreutils/manual/coreutils.html#sort-invocation)
* [GNU Coreutils - join: Join lines on a common field](https://www.gnu.org/software/coreutils/manual/coreutils.html#join-invocation)
* [Bash Manual - Redirections](https://www.gnu.org/software/bash/manual/bash.html#Redirections)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

# paste and join

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

# paste

`paste` merges lines of files in the order that they are in. Navigate to the `/Udata2/Joining` folder with `cd`:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/Joining

```

Now, try `paste` with `jmols01.txt` and `jmols01_data.txt`:

```console

user@computer:~$ cat jmols01.txt
ZHAOHDRTWMBHER-MRVPVSSYSA-N	CC=C[C@@H]1CC(=O)CCO1	149501208
ZHAOHDRTWMBHER-UHFFFAOYSA-N	CC=CC1CC(=O)CCO1	140006540
QGHJAGNQZQUZPO-UHFFFAOYSA-N	C1C2C=CC(O2)CC1=O.[Y]	135045719
DJXYBPVHUSVRLJ-KNVOCYPGSA-N	C1[C@@H]2C=C[C@@H](O2)CC1=O	5325223
DJXYBPVHUSVRLJ-UHFFFAOYSA-N	C1C2C=CC(O2)CC1=O	557672
```

```console

user@computer:~$ cat jmols01_data.txt
140.18	2020
140.18	2019
213.04	2018
124.14	2006
124.14	2005
```

```console

user@computer:~$ paste jmols01.txt jmols01_data.txt
ZHAOHDRTWMBHER-MRVPVSSYSA-N	CC=C[C@@H]1CC(=O)CCO1	149501208	140.18	2020
ZHAOHDRTWMBHER-UHFFFAOYSA-N	CC=CC1CC(=O)CCO1	140006540	140.18	2019
QGHJAGNQZQUZPO-UHFFFAOYSA-N	C1C2C=CC(O2)CC1=O.[Y]	135045719	213.04	2018
DJXYBPVHUSVRLJ-KNVOCYPGSA-N	C1[C@@H]2C=C[C@@H](O2)CC1=O	5325223	124.14	2006
DJXYBPVHUSVRLJ-UHFFFAOYSA-N	C1C2C=CC(O2)CC1=O	557672	124.14	2005
```


# join

Another useful utility to combine data is `join`, which joins lines of two files by a common index field.

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

Above, we can see that the jmols01.txt and jmols02.txt files have related data. If we want to use `join`, the first task we need to do is use `sort` and sort the files by the column that we want to use as the index field for `join`. In this case, we will select the first column as the index field, save the sorted (by field 1) output to new files, then use `join` to join the data:

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

* [GNU Coreutils - cat](https://www.gnu.org/software/coreutils/manual/coreutils.html#cat-invocation)
* [GNU Coreutils - sort](https://www.gnu.org/software/coreutils/manual/coreutils.html#sort-invocation)
* [GNU Coreutils - paste](https://www.gnu.org/software/coreutils/manual/coreutils.html#paste-invocation)
* [GNU Coreutils - join](https://www.gnu.org/software/coreutils/manual/coreutils.html#join-invocation)
* [Bash Manual - Redirections](https://www.gnu.org/software/bash/manual/bash.html#Redirections)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

# cat, tac, head, and tail

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

## cat

One way to quickly view text files is to print the contents to standard output (your terminal window) using `cat`. Let's take a look at the subsetA_CID_51351709_similar.txt file located in the `/Udata2/View` folder. First, use `cd` to change your directory to the folder:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/View

```
We can then use the `cat` utility to print the contents of a file to standard output:

```console

user@computer:~$ cat subsetA_CID_5135709_similar.txt 
CC.CC1CCC2CC(=C(CC2C1)C=C)C=C	154673141	232.400
CC1CCCCC1C2=CC=CCC2	154546688	176.300
CC1CCCC2C1=CC=C3C2C=CC=C3	154307178	198.300
CCC1=CC=C2C(C1)C(CCC2(C)C)(C)C	154280750	218.380
CC1C(=C)CCC2C1=CC=CC2	154236167	160.250

```

A common use of `cat` is also to concatenate files. For example, let's say we wanted to combine the three subset*.txt files and redirect, `>`, the output to a new file named `combined_test.txt`:

```console

user@computer:~$ cat subset*.txt > combined_test.txt

```

## tac

We can display the contents of files in reverse using `tac`. Compare `tac` to our example above with `cat`:

```console

user@computer:~$ tac subsetA_CID_5135709_similar.txt
CC1C(=C)CCC2C1=CC=CC2	154236167	160.250
CCC1=CC=C2C(C1)C(CCC2(C)C)(C)C	154280750	218.380
CC1CCCC2C1=CC=C3C2C=CC=C3	154307178	198.300
CC1CCCCC1C2=CC=CCC2	154546688	176.300
CC.CC1CCC2CC(=C(CC2C1)C=C)C=C	154673141	232.400
```

## head

Instead of using `cat` or `tac` first, it is usually a good idea to look at a preview of the file, so we don't unnecessarily print 100s or 1000s of lines to the standard output. For example, the file `CID_51351709_similar.txt` has ~500 lines. We can use `head` to print the first 10 lines of the file:

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
CC1CCC(CC1)C2=CC(C(C=C2)C)C	153688226	204.350
```

Further, we can specify the number of lines printed to standard output with `head` by adding the `-n` option followed by a digit. For example, the first 4 lines:

```console

user@computer:~$ head -n4 CID_51351709_similar.txt
CC.CC1CCC2CC(=C(CC2C1)C=C)C=C	154673141	232.400
CC1CCCCC1C2=CC=CCC2	154546688	176.300
CC1CCCC2C1=CC=C3C2C=CC=C3	154307178	198.300
CCC1=CC=C2C(C1)C(CCC2(C)C)(C)C	154280750	218.380

```

## tail

The `tail` program is similar to `head`, but it prints the last lines of files. For example, print the last 5 lines of `CID_51351709_similar.txt`:

```console

user@computer:~$ tail -n5 CID_51351709_similar.txt 
CC1CCC(C2C1=CCC(=C2)C)C(C)C	519298	204.350
CCCC1C(C(CC2C1=CC=CC2)C)C	186376	204.350
CC1=C[C@H]2[C@H](CC1)C(=C)CC[C@@H]2C(C)C	92313	204.350
CC1=CC2C(CC1)C(=C)CCC2C(C)C	15094	204.350
CC1=CCCC2(C1CC(CC2)C(=C)C)C	10123	204.350

```

Note that the original order in the file is maintained with `tail`, so the last 5 lines are not reversed. If we want to reverse the output, one way to to do this is to pipe the `tail` results to `tac`:

```console

user@computer:~$ tail -n5 CID_51351709_similar.txt | tac
CC1=CCCC2(C1CC(CC2)C(=C)C)C	10123	204.350
CC1=CC2C(CC1)C(=C)CCC2C(C)C	15094	204.350
CC1=C[C@H]2[C@H](CC1)C(=C)CC[C@@H]2C(C)C	92313	204.350
CCCC1C(C(CC2C1=CC=CC2)C)C	186376	204.350
CC1CCC(C2C1=CCC(=C2)C)C(C)C	519298	204.350

```

## References and Further Reading

* [GNU Coreutils - cat](https://www.gnu.org/software/coreutils/manual/coreutils.html#cat-invocation)
* [GNU Coreutils - tac](https://www.gnu.org/software/coreutils/manual/coreutils.html#tac-invocation)
* [GNU Coreutils - head](https://www.gnu.org/software/coreutils/manual/coreutils.html#head-invocation)
* [GNU Coreutils - tail](https://www.gnu.org/software/coreutils/manual/coreutils.html#tail-invocation)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

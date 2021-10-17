# diff and comm

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

# comm

`comm` compares sorted files and outputs three columns by default. The first column is lines unique to file1, the second column is lines unique to file2, and the third column are common lines in both files. Navigate to the `/Udata2/Comparing` folder:


```console

user@computer:~$ cd /home/user/Desktop/Udata2/Comparing

```
Let's compare the sorted files:

```console

user@computer:~$ comm CIDs_SearchA.sorted CIDs_SearchB.sorted
11031767
11062432
11075478
11159638
11160028
		11171745
11171853
11229242
		11229455
		11243457
		118785
1390
		142665
144732868
144732935
144780848
		144780855
		144883221
		144911941
		144967834
144974135
145079716
145080515
	147947816
	147948350
...
...
...
```

A useful option flag is `-12`, which only outputs column 3 (common lines). We can then pipe this to `wc` to get the number of common lines between the files:


```console

user@computer:~$ comm -12 CIDs_SearchA.sorted CIDs_SearchB.sorted | wc -l
20
```

# diff

The `diff` utility compares files line by line. Comparing files with `diff` is a quick way to see differences between files. Navigate to the `/Udata2/Benchmark` folder:


```console

user@computer:~$ cd /home/user/Desktop/Udata2/Benchmark

```

In this folder, there are three selected files from the [NextMove Software smilesreading repository](https://github.com/nextmovesoftware/smilesreading). These files represent some benchmark data, and in order to analyze them, we need to compare any differences between the files. Let's start by comparing the WeiningerCEX_132_reading_smilesvalence.txt and avalon_1.2.0_reading_smilesvalence.txt files with `diff`. By default, `diff` prints the output vertically and shows the line numbers that differ from file 1 and file 2. I prefer to display the results side by side, so we will add the `-y` (two column) option here:

```console

user@computer:~$ diff -y WeiningerCEX_132_reading_smilesvalence.txt avalon_1.2.0_reading_smilesvalence.txt 
B0 3								B0 3
B1 2 3								B1 2 3
B2 1 3 3							B2 1 3 3
B3 0 3 3 3							B3 0 3 3 3
B4 0 3 3 3 3							B4 0 3 3 3 3
...
...
Cl0 1								Cl0 1
Cl1 0 3								Cl1 0 3
Cl2 0 3 3						      |	Cl2 1 3 3
Cl3 0 3 3 3							Cl3 0 3 3 3
Cl4 0 3 3 3 3						      |	Cl4 1 3 3 3 3
Cl5 0 3 3 3 3 3							Cl5 0 3 3 3 3 3
Br0 1								Br0 1
Br1 0 3								Br1 0 3
...
...
I2 0 3 3						      |	I2 1 3 3
I3 0 3 3 3							I3 0 3 3 3
I4 0 3 3 3 3						      |	I4 1 3 3 3 3
I5 0 3 3 3 3 3							I5 0 3 3 3 3 3

```

The `-y` option displays all lines of text and marks differences with a vertical bar. To display only the differences, we can add the `--suppress-common-lines` option:

```console

user@computer:~$ diff -y --suppress-common-lines WeiningerCEX_132_reading_smilesvalence.txt avalon_1.2.0_reading_smilesvalence.txt 
Cl2 0 3 3						      |	Cl2 1 3 3
Cl4 0 3 3 3 3						      |	Cl4 1 3 3 3 3
Br2 0 3 3						      |	Br2 1 3 3
Br4 0 3 3 3 3						      |	Br4 1 3 3 3 3
I2 0 3 3						      |	I2 1 3 3
I4 0 3 3 3 3						      |	I4 1 3 3 3 3

```

Let's try another comparison:

```console

user@computer:~$ diff -y --suppress-common-lines cdk_2.1_reading_smilesvalence.txt avalon_1.2.0_reading_smilesvalence.txt 
B0 3    						      |	B0 3
B1 2 3  						      |	B1 2 3
B2 1 3 3						      |	B2 1 3 3
B3 0 3 3 3      					      |	B3 0 3 3 3
B4 0 3 3 3 3    					      |	B4 0 3 3 3 3
C0 4    						      |	C0 4
C1 3 3  						      |	C1 3 3
...
...
```

Here you will notice that `diff` is marking the lines as different, but they look the same. So, we need to investigate the files and identify any potential hidden characters. A convenient method is to use `cat` with the `-t` option, which shows non-printing and tab characters in the standard output. Let's look more closely at the cdk_2.1_reading_smilesvalence.txt file:

```console

user@computer:~$ cat -t cdk_2.1_reading_smilesvalence.txt 
B0 3^M
B1 2 3^M
B2 1 3 3^M
B3 0 3 3 3^M
B4 0 3 3 3 3^M
C0 4^M
C1 3 3^M
C2 2 3 3^M
...
...
```

Here we can see that there are some `^M` characters, which are carriage returns. We can use the `diff` option `--strip-trailing-cr` to remove these for comparison:

```console

user@computer:~$ diff -y --suppress-common-lines --strip-trailing-cr cdk_2.1_reading_smilesvalence.txt avalon_1.2.0_reading_smilesvalence.txt 
Cl2 0 3 3						      |	Cl2 1 3 3
Cl4 0 3 3 3 3						      |	Cl4 1 3 3 3 3
Br2 0 3 3						      |	Br2 1 3 3
Br4 0 3 3 3 3						      |	Br4 1 3 3 3 3
I2 0 3 3						      |	I2 1 3 3
I4 0 3 3 3 3						      |	I4 1 3 3 3 3
```

Great! Now we can see the differences without the carriage return differences. There are many more `diff` options. You may need to experiment with the options depending upon the formatting of your input data. 

## References and Further Reading


* [GNU comm](https://www.gnu.org/software/coreutils/manual/coreutils.html#comm-invocation)
* [GNU diffutils](https://www.gnu.org/software/diffutils/manual/diffutils.html)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.


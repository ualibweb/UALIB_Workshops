# split and shuf

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


# split

`split` will output consecutive sections of files; that is, one use-case is to split a big file into numerous smaller files by the number of lines or size. Navigate to the `/Udata2/Sorting` folder with `cd`:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/Sorting

```

First, check the number of lines of the file `molecules3.smi`:

```console

user@computer:~$ wc -l molecules3.smi
1430 molecules3.smi
```

Let's say we needed to split this file into chunks of 250 lines each. The default number of lines for `split` is 1000, but we can change this with the `-l` option. In addition, we will use `mols_` as the file prefix and the `additional-suffix` option to add our preferred file extension:

```console

user@computer:~$ split -l250 molecules3.smi mols_ --additional-suffix='.smi'
user@computer:~$ wc -l mols*.smi
  250 mols_aa.smi
  250 mols_ab.smi
  250 mols_ac.smi
  250 mols_ad.smi
  250 mols_ae.smi
  180 mols_af.smi
 1430 total
```

# shuf

`shuf` outputs a random selection of lines. According to `info shuf`, The default behavior is that "Each output permutation is equally likely." This is quite useful for sampling datasets. For example, we could use `shuf` to select 20 random lines from `molecules3.smi`:

```console

user@computer:~$ shuf -n20 molecules3.smi
CCC1(C(CCC2C1=CCCC2)C(C)(C)C)C	PZPIXXRYSWHWEV-UHFFFAOYSA-N	143681056
CC1(CCC(C2=CCCCC21)(C)C)C	LOTKSLLORLTOQN-UHFFFAOYSA-N	145751120
CCC1CC[C@H](C2C1C=C(CC2)C)C	JGVOBAQNVSGFRL-NTXGFPLRSA-N	141800277
C[C@@H]1CCC2=CC(=C)CCC2C1	VYQXHZJGWUHKSE-RWANSRKNSA-N	153141248
CCC[C@H]1CCC(=CC1)C2[C@@H](CCC3=CC23)C	SPPRTJKFYRDPTA-QJRTVWDNSA-N	152806595
...
...

```

# csplit

`csplit` can split files on a specified pattern. Navigate to the `/Udata2/SDF` folder with `cd`:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/SDF

```

The `PubChem_substance_WikiData1-15.sdf` file is a sample of 15 chemical substance records from WikiData in the PubChem Substance database, exported in `.sdf` format. The `.sdf` file has a pattern. While the number of lines for each record varies, each molecule substance record ends with four dollar signs, `$$$$`. What if we wanted to split the `.sdf` file into individual substance files, creating 15 files? We can do this with `csplit` as follows:


```console

user@computer:~$ csplit --elide-empty-files --suffix-format='%03d.mol' PubChem_substance_WikiData1-15.sdf '/\$\{4\}/1' '{*}'
```

```console

user@computer:~$ ls
PubChem_substance_WikiData1-15.sdf  xx003.mol  xx007.mol  xx011.mol
xx000.mol                           xx004.mol  xx008.mol  xx012.mol
xx001.mol                           xx005.mol  xx009.mol  xx013.mol
xx002.mol                           xx006.mol  xx010.mol  xx014.mol
```

The above `csplit` command is more complicated than `split`. Let's look at each piece and the thought process:

1. First, the pattern I wanted to define for the file splitting was four repeated dollar signs, `$$$$`. The regular expression I came up with for this was:

`\${4}`, which is a dollar sign repeated 4 times (i.e., `{4}`). Note that I added an escape `\` to avoid special interpretation of `$`. I'm not an expert with regular expressions, but this seemed reasonable to try.

2. The regular expression above did not work, but I found out that in POSIX Basic Regular Syntax, the metacharacters need to be escaped like this:

`\$\{4\}`, see the [Wikipedia Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression) page and chapter 19 of [LinuxCommand.org](http://linuxcommand.org/) / [LinuxCommand (PDF version)](https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf).

3. Next, this pattern is inserted into forward slashes as per the `csplit` syntax:

`/\$\{4\}/`

4. After some testing, I found that I needed to add an offset of `1` to the pattern, to allow the `$$$$` line to be included at the end of the file, and not the beginning of the next file. So, the pattern argument became:

`/\$\{4\}/1`

5. Next, this pattern is followed by the `csplit` notation `'{*}'` to repeat the pattern for every match (see `$ man csplit`). So now we have our final pattern syntax:

`'/\$\{4\}/1' '{*}'`

6. The `--elide-empty-files` option was added because a 16th empty file is created without this, presumably from trying to split the file at the last occurrence of `$$$$`.

7. The `--suffix-format='%03d.mol'` specifies to label each output file with 3 integer digits and the `.mol` extension. The `%03d` is a [printf notation](https://www.gnu.org/software/libc/manual/html_node/Formatted-Output.html)

## References and Further Reading

* [GNU Coreutils - wc](https://www.gnu.org/software/coreutils/manual/coreutils.html#wc-invocation)
* [GNU Coreutils - split](https://www.gnu.org/software/coreutils/manual/coreutils.html#split-invocation)
* [GNU Coreutils - shuf](https://www.gnu.org/software/coreutils/manual/coreutils.html#shuf-invocation)
* [GNU Coreutils - csplit](https://www.gnu.org/software/coreutils/manual/coreutils.html#csplit-invocation)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.


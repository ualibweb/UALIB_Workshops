# sort, uniq, and cut

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


## sort

The `sort` utility sorts lines. One application of `sort` is to identify and/or remove duplicate lines. Navigate to the `/Udata2/Sorting` folder with `cd`:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/Sorting

```
Let's look at the molecules.smi file with `cat`:

```console

user@computer:~$ cat molecules.smi
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C	OZQAPQSEYFAMCY-SOUVJXGZSA-N	10726905
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
CC1CC2CCCC=C2C(C1(C)C)(C)C	WLZHEXZCQNVIOB-UHFFFAOYSA-N	129720989
CCC[C@@H]1CCC(C2=CCCC=C12)C	UUIJJZRFSATZAR-PIJUOVFKSA-N	141868307
CC1CCCCC1C2=CC=CCC2	ONWJTPPDINXBJV-UHFFFAOYSA-N	154546688
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125

```

We can use the `sort` utility, which by default sorts be the first column:

```console

user@computer:~$ sort molecules.smi
CC1CC2CCCC=C2C(C1(C)C)(C)C	WLZHEXZCQNVIOB-UHFFFAOYSA-N	129720989
CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C	OZQAPQSEYFAMCY-SOUVJXGZSA-N	10726905
CC1CCCCC1C2=CC=CCC2	ONWJTPPDINXBJV-UHFFFAOYSA-N	154546688
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
CCC[C@@H]1CCC(C2=CCCC=C12)C	UUIJJZRFSATZAR-PIJUOVFKSA-N	141868307
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125

```

If we want to sort by a different column, we can add the `-k` option and specify a start and end column number separated by a comma. For example, to sort by the second column:


```console

user@computer:~$ sort -k2,2 molecules.smi
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1CCCCC1C2=CC=CCC2	ONWJTPPDINXBJV-UHFFFAOYSA-N	154546688
CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C	OZQAPQSEYFAMCY-SOUVJXGZSA-N	10726905
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125
CCC[C@@H]1CCC(C2=CCCC=C12)C	UUIJJZRFSATZAR-PIJUOVFKSA-N	141868307
CC1CC2CCCC=C2C(C1(C)C)(C)C	WLZHEXZCQNVIOB-UHFFFAOYSA-N	129720989
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
```

If we want to eliminate duplicates, we can add the option `-u` for unique. For example, to sort on column 3 and output a list of unique lines:

```console

user@computer:~$ sort -u -k3,3 molecules.smi
CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C	OZQAPQSEYFAMCY-SOUVJXGZSA-N	10726905
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1CC2CCCC=C2C(C1(C)C)(C)C	WLZHEXZCQNVIOB-UHFFFAOYSA-N	129720989
CCC[C@@H]1CCC(C2=CCCC=C12)C	UUIJJZRFSATZAR-PIJUOVFKSA-N	141868307
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
CC1CCCCC1C2=CC=CCC2	ONWJTPPDINXBJV-UHFFFAOYSA-N	154546688
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125

```

## uniq

The previous example (`$ sort -u -k3,3 molecules.smi`) removed duplicates. To output a list of the duplicates instead, we can pipe `|` the sorted file to the `uniq` utility, which can report or omit duplicate lines. Use the `-d` option to only print the duplicate lines:

```console

user@computer:~$ sort -k3,3 molecules.smi | uniq -d
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125

```

The `uniq` utility requires sorting the files first (see `$ man uniq`), which is why we piped our sorted molecules.smi file into `uniq`. It is important to note that `uniq` is analyzing lines, not a particular column. So, for example, if we look at molecules2.smi, which is identical to molecules.smi, except for replacement of the InChIKey value with `TEST`  in the second column of line 9:

```console

user@computer:~$ cat molecules2.smi
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C	OZQAPQSEYFAMCY-SOUVJXGZSA-N	10726905
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
CC1CC2CCCC=C2C(C1(C)C)(C)C	WLZHEXZCQNVIOB-UHFFFAOYSA-N	129720989
CCC[C@@H]1CCC(C2=CCCC=C12)C	UUIJJZRFSATZAR-PIJUOVFKSA-N	141868307
CC1CCCCC1C2=CC=CCC2	ONWJTPPDINXBJV-UHFFFAOYSA-N	154546688
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC/C=C/1\CCC2CC(CCC2C1)C	TEST	153248005
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125

```

Let's sort this file by column 3:

```console

user@computer:~$ sort -k3,3 molecules2.smi
CC1=CCC[C@]2([C@H]1C[C@H](CC2)C(=C)C)C	OZQAPQSEYFAMCY-SOUVJXGZSA-N	10726905
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
CC1CC2CCCC=C2C(C1(C)C)(C)C	WLZHEXZCQNVIOB-UHFFFAOYSA-N	129720989
CCC[C@@H]1CCC(C2=CCCC=C12)C	UUIJJZRFSATZAR-PIJUOVFKSA-N	141868307
CC/C=C/1\CCC2CC(CCC2C1)C	TEST	153248005
CC/C=C/1\CCC2CC(CCC2C1)C	WSTKIWSHWCBHED-UUILKARUSA-N	153248005
CC1CCCCC1C2=CC=CCC2	ONWJTPPDINXBJV-UHFFFAOYSA-N	154546688
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125

```
Note that our line with TEST in it actually has a duplicate value in column 3, but if we pipe this sorted file directly to `uniq` with the `-d` option, we will not see this as a duplicate since the overall line is different:

```console

user@computer:~$ sort -k3,3 molecules2.smi | uniq -d
CC1C[C@H]2CC=CC[C@H]2CC1C	MERJPGYKGRUPDP-CAODYFQJSA-N	123488840
C[C@H]1CC[C@@H](C2=CC(=C)CCC12)C(C)C	RNDFUOKDULDZPR-WLDKUNSKSA-N	91747125

```

## cut

An alternative workflow to find duplicates in column 3 would be to first isolate column 3 with the `cut` utility and `-f` option for field:

```console

user@computer:~$ sort -k3,3 molecules2.smi | cut -f3 | uniq -d
123488840
153248005
91747125
```

Now we can see above that 153248005 is also a duplicate.

Another useful feature of `uniq` is the ability to count duplicates with the `-c` option. Let's try this with the molecules3.smi file on the second column. We will first use `cut -f2` to select the second column, then pipe the results to `sort`, followed by `uniq -c`:

```console

user@computer:~$ cut -f2 molecules3.smi | sort | uniq -c
1 AADGSRWLEUZENB-UHFFFAOYSA-N
1 ABVUHYAHYXFJSS-KQTLUZQSSA-N
1 ABVUHYAHYXFJSS-UHFFFAOYSA-N
1 ACZYKRLNKMPGCE-TZMCWYRMSA-N
1 ADSNFHKCMSDPOJ-UHFFFAOYSA-N
...
1 AQGAXCSMGZRGJZ-UHFFFAOYSA-N
2 AQIXNFSMFTXNRC-UHFFFAOYSA-N
```

This output is fine, but an even more useful output might be to display the results with most repeated first. We can add another pipe to redirect to `sort` with the `-n` for numeric sort and `-r` option for reverse output (greatest number first):

```console

user@computer:~$ cut -f2 molecules3.smi | sort | uniq -c | sort -n -r
      5 QTNYQRWMEMVYPD-UHFFFAOYSA-N
      5 IVOPGGGQQORTCJ-UHFFFAOYSA-N
      3 BMZFMBCBVGEJJU-UHFFFAOYSA-N
      2 ZZPSOALECBMAMW-UHFFFAOYSA-N
      2 ZZPSOALECBMAMW-GIJJTGMTSA-N
      2 ZPMMGGDVYXPGIO-UHFFFAOYSA-N
      2 ZPMMGGDVYXPGIO-JJARTYCRSA-N
      2 ZMORNSMYOUIDDO-UHFFFAOYSA-N
      2 ZDYSJYZWQCRTFL-ZQDZILKHSA-N
      2 ZDYSJYZWQCRTFL-LXTVHRRPSA-N
      2 ZDYSJYZWQCRTFL-DNDYEEKYSA-N
...
```

Finally, maybe we only want to see the top 5, so we can extend our pipeline with `head`:

```console

user@computer:~$ cut -f2 molecules3.smi | sort | uniq -c | sort -n -r | head -n5
      5 QTNYQRWMEMVYPD-UHFFFAOYSA-N
      5 IVOPGGGQQORTCJ-UHFFFAOYSA-N
      3 BMZFMBCBVGEJJU-UHFFFAOYSA-N
      2 ZZPSOALECBMAMW-UHFFFAOYSA-N
      2 ZZPSOALECBMAMW-GIJJTGMTSA-N

```

## References and Further Reading

* [GNU Coreutils - sort](https://www.gnu.org/software/coreutils/manual/coreutils.html#sort-invocation)
* [GNU Coreutils - uniq](https://www.gnu.org/software/coreutils/manual/coreutils.html#uniq-invocation)
* [GNU Coreutils - cut](https://www.gnu.org/software/coreutils/manual/coreutils.html#cut-invocation)

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.


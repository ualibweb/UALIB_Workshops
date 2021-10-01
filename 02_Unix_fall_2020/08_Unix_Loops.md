# Repeating Tasks with Loops

**Lesson Navigation**

1. [Introduction and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/01_Unix_Introduction.md)
2. [Navigating Files and Directories](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/02_Unix_Navigating.md)
3. [Viewing Files and Counting](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/03_Unix_Viewing_Counting.md)
4. [Sorting and Finding Duplicates](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/04_Unix_Sorting_Duplicates.md)
5. [Merging Files and Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/05_Unix_Merging.md)
6. [Comparing Files](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/06_Unix_Comparing.md)
7. [Pattern Searching](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/07_Unix_Patterns.md)
8. [Repeating Tasks with Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix_fall_2020/08_Unix_Loops.md)

## Repeating Tasks with a Loop

We can write loops in Bash to repeat tasks, similar to other programming languages. The general syntax of a for loop in Bash is as follows:

```console

for item in list_of_items
do
     something_using $item
done
```

The `$` symbol within the loop is interpreted as a variable. That is, `$item` gets substituted with the item name in our list_of_items. Let's return to the `/Udata/PubMed` folder and our use of `grep` with the PubMed_Search_combined.txt file. Let's say we wanted to create several files by using `grep` with independent patterns. A possible workflow is to create a list of our patterns and then use `grep` in a Bash for loop:

```console

user@computer:~$ for pattern in "biology" "chemistry" "engineering" "physics"
> do
>     grep -w -i "$pattern" PubMed_Search_combined.txt > PubMed_Search_filter_"$pattern".txt
> done

```

In the above script, we are telling Bash to use the `grep` utility with options `-w -i` and our pattern variable on file PubMed_Search_combined.txt, then redirect the output to a new file with the variable name at the end of the file name. So, on the first iteration, our pattern is "biology" and the file name is PubMed_Search_filter_biology.txt, on the second iteration, our pattern is "chemistry" and the file name is PubMed_Search_filter_chemistry.txt, and so on. 


## References and Further Reading

* [Software Carpentry Unix Loops Lesson](https://swcarpentry.github.io/shell-novice/05-loop/index.html)
* [Bash Manual Looping Constructs](https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs). 

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

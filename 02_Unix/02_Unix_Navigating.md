# Navigating Files and Directories

**Lesson Navigation**

1. [Introduction and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/01_Unix_Introduction.md)
2. [Navigating Files and Directories](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/02_Unix_Navigating.md)
3. [Viewing Files and Counting](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/03_Unix_Viewing_Counting.md)
4. [Sorting and Finding Duplicates](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/04_Unix_Sorting_Duplicates.md)
5. [Merging Files and Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/05_Unix_Merging.md)
6. [Comparing Files](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/06_Unix_Comparing.md)
7. [Pattern Searching](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/07_Unix_Patterns.md)
8. [Repeating Tasks with Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/02_Unix/08_Unix_Loops.md)

## Find Current Working Directory

We can display the name of the current working directory with the `pwd` utility:

```console

user@computer:~$ pwd
/home/user

```
## List Contents

To list the contents within a directory, use `ls`:

```console

user@computer:~$ ls
Downloads	Music	Desktop
Pictures	Templates	Documents

```
We can add the `-F` option to classify the contents, which can help identify a file versus a directory, for example.

```console

user@computer:~$ ls -F
Downloads/	Music/	Desktop/
Pictures/	Templates/	Documents/

```
In the above example, all of our contents now end with a `/`, which indicates they are directories. 

## Changing Directories

To change directories, we can use `cd` followed by the name of a directory or path to a directory:

```console

user@computer:~$ cd Desktop
user@computer:~$ pwd
/home/user/Desktop

```

We can then list the contents in our new working directory:

```console

user@computer:~$ ls -F
Udata/

```
And then `cd` into the `Udata` folder, and sub-directories as desired:

```console

user@computer:~$ cd Udata
user@computer:~$ ls -F
Benchmark/  Joining/  PubMed/  Sorting/  toolkit_process/  View/
user@computer:~$ cd Sorting
/home/user/Desktop/Udata/Sorting
user@computer:~$ ls -F
molecules2.smi  molecules3.smi  molecules.smi

```

Alternatively, we can always change directories by providing the full directory path:

```console

user@computer:~$ cd /home/user/Desktop/Udata/Sorting

```

Finally, a useful shortcut to return to the parent of the current directory is `..`:

```console

user@computer:~$ pwd
/home/user/Desktop/Udata/Sorting
user@computer:~$ cd ..
user@computer:~$ pwd
/home/user/Desktop/Udata/

```

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

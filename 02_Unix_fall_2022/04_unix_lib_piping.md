# Pipelines and Redirecting Data Outputs

---
**Lesson Navigation**

1. [Introduction](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_introduction.md)
2. [Navigation and Directories](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_files_directories.md)
3. [Common Unix Commands](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_common_commands.md)
4. [Pipelines and Redirecting Data Outputs](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_piping.md)
---

## Starting with Pipes in Unix

For the last part of our workshop, we will take a look a few examples of 
redirecting data outputs into multiple commands and into new files.

The Unix/Bash Shell is a powerful tool for working with data, and its capacity to
redirect output from one command into another using pipes or `|` are an important 
concept in the ["Unix Philosophy"](https://en.wikipedia.org/wiki/Unix_philosophy) 
and allow for easy combination of commands.

For example:
```console
user@computer:~$ something1 | something2 | something3
```
The above syntax creates a sequence of commands. The output from something1 is
used as the input into something2, and then the output from something2 is used 
as the input for something3. This is a powerful approach and allows us to combine
simple tasks into much more complex processes.

Let's try this with some of the data with which we've been working. Earlier, 
we used a detailed command to sort the data for Hurricane Iota by its minimum 
central pressure. Let's use the same command, and pipe the results into the `head`
command to limit our output to only the first 5 lines in the newly sorted data 
set (**Don't forget that you can use the `Up` arrow key to see and reuse previous
commands**):

```console
user@computer:~$ sort -t',' -k7 -n -r AL312020_iota.txt | head -n 5
20201116, 1200,  , HU, 13.5N,  81.5W, 135,  917,  200,  130,  100,  180,   80,   60,   50,   80,   40,   30,   25,   40,
20201117, 0000,  , HU, 13.6N,  83.0W, 130,  918,  200,  130,  100,  180,   80,   60,   50,   80,   40,   30,   25,   40,
20201116, 1800,  , HU, 13.5N,  82.3W, 130,  918,  200,  130,  100,  180,   80,   60,   50,   80,   40,   30,   25,   40,
20201117, 0340, L, HU, 13.6N,  83.5W, 125,  922,  200,  130,   90,  180,   80,   60,   50,   70,   40,   30,   20,   35,
20201116, 0600,  , HU, 13.4N,  80.7W, 120,  935,  180,  130,   90,  160,   80,   60,   40,   80,   35,   30,   25,   35,
```
We can also redirect output into a new file using `> filename` or `>> filename`.
Let's try this using `ls` and a few of wild card examples from earlier to create
a file with a list of all of the hurricanes for which we have data in the 2010s:

```console
user@computer:~$ ls AL??201* > storms_2010s.txt
user@computer:~$ cat storms_2010s.txt
AL052019_dorian.txt
AL112017_irma.txt
AL142018_michael.txt
AL152017_maria.txt
```
**Note: Be sure to check that you are not redirecting output to a filename that
already exists. Using the `>` will automatically overwrite whatever data is in 
that file. If you would like to redirect output to add data to a file that already 
exists, you can use the `>>` in place of `>`.**

---
**Attribution**
> Some content in this workshop has been adapted and derived from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Hurricane data was retrieved from the [National Hurricane Center's Data Archive](https://www.nhc.noaa.gov/data/), and is derived from the [Best Track Data HURDAT2 dataset](https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2020-052921.txt). Please see the [NOAA website Use of NOAA/NWS Data and Products and Disclaimers](https://www.weather.gov/disclaimer) for more information regarding the data.

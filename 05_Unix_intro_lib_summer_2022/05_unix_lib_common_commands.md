# Common Unix Commands

---
**Lesson Navigation**

1. [Introduction](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/f535af66199cf41499be66c191fa4e3cb207436d/05_Unix_intro_lib_summer_2022/05_unix_lib_introduction.md)
2. [Navigation and Directories](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/f535af66199cf41499be66c191fa4e3cb207436d/05_Unix_intro_lib_summer_2022/05_unix_lib_files_directories.md)
3. [Common Unix Commands](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/f535af66199cf41499be66c191fa4e3cb207436d/05_Unix_intro_lib_summer_2022/05_unix_lib_common_commands.md)
4. [Pipelines and Redirecting Data Outputs](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/f535af66199cf41499be66c191fa4e3cb207436d/05_Unix_intro_lib_summer_2022/05_unix_lib_piping.md)

---

In this section of the workshop, we will learn a few commands that are commonly 
used in the Unix/Bash Shell, especially for sorting and retrieving specific parts 
of datasets when beginning analysis. We will focus on the commands, and many more
in the subsequent workshop, Introduction to Unix Shell for Basic Data Transformation
and Analysis.

---
## Command Syntax

This is a quick reminder to consider the syntax for commands: command(ls, man, 
touch, etc) [space] -option (-F, -i, -a, etc.) [space] argument. Or, as in the 
example below:

```console
user@computer:~$ ls -F ~/Desktop/hurricane_data
```

---
## Unix Commands and Tools

Use The `cat` command, or concatenate, to utilize the data from a file in the 
command line. Where the `less` command that we learned earlier allows you to view
the data from a particular file, `cat` allows use to use the data. When using `cat`
alone, the data from the file or files requested will be printed in the command 
window.

For example:

```console
user@computer:~$ cat example1
2004 ivan
2003 isabel
2020 iota
2017 irma
```
This prints the data from the `example1` that we created earlier into the command
window. This particular file contains a small amount of data that we added earlier.
If you are using `cat` alone, be aware that it will print the entirety of a file.
The file `hurdat2-1851-2020-052921.txt`contains best track data for every tropical
system between 1851 and 2020, meaning that using `cat` on this file would take a
few moments, and print several pages of data into the command line.

The `sort` command does exactly as it says, and it provides a way to sort data in
a file. Similar to `cat`, this will send the data to the screen, in the command 
line. `sort` automatically sorts alphabetically, and treats numbers with this same
concept. To sort numerically, add the `-n` option.

```console
user@computer:~$ sort -k2 example1
2004 ivan
2003 isabel
2020 iota
2017 irma
```
We can also use the `-k` option to sort using the names in the second column we
created:

```console
user@computer:~$ sort -n example1
2020 iota
2017 irma
2003 isabel
2004 ivan
```

The files that we are working with have tabular data that use `,` as the delimiter.
To use `sort` with this type of data, we will have add an option `-t` and specify
the delimiter in single quotes `','`. See more about [using the `-t` option with this example from Stack Overflow](https://unix.stackexchange.com/questions/140388/sort-comma-separated-fields-on-each-line-by-numeric-value).
To sort using a specific column, we will need to add the `-k` option as well, 
with the column number immediately after the `-k`. We can also sort the data in
reverse using the `-r` option.

Let's try this in the example below. In looking at the data from Hurricane Iota
in `AL312020_iota.txt`, column 7 is the minimum central pressure in millibars for
each recorded instances in the best track dataset. To sort this file by the 
minimum central pressure, we can execute the following:

```console
user@computer:~$ sort -t',' -k7 -n -r AL312020_iota.txt
20201116, 1200,  , HU, 13.5N,  81.5W, 135,  917,  200,  130,  100,  180,   80,   60,   50,   80,   40,   30,   25,   40,
20201117, 0000,  , HU, 13.6N,  83.0W, 130,  918,  200,  130,  100,  180,   80,   60,   50,   80,   40,   30,   25,   40,
20201116, 1800,  , HU, 13.5N,  82.3W, 130,  918,  200,  130,  100,  180,   80,   60,   50,   80,   40,   30,   25,   40,
20201117, 0340, L, HU, 13.6N,  83.5W, 125,  922,  200,  130,   90,  180,   80,   60,   50,   70,   40,   30,   20,   35,
20201116, 0600,  , HU, 13.4N,  80.7W, 120,  935,  180,  130,   90,  160,   80,   60,   40,   80,   35,   30,   25,   35,
20201117, 0600,  , HU, 13.7N,  83.8W, 110,  935,  190,  130,   80,  180,   70,   60,   30,   60,   35,   25,   15,   25,
20201116, 0000,  , HU, 13.2N,  79.8W,  90,  961,  160,  120,   80,  140,   70,   60,   40,   70,   30,   25,   20,   25,
20201117, 1200,  , HU, 13.7N,  84.7W,  75,  965,  170,  110,   50,  160,   60,   40,    0,   50,   30,    0,    0,   20,
20201115, 1800,  , HU, 13.2N,  78.9W,  75,  974,  140,  100,   70,  120,   60,   50,   40,   60,   25,   20,    0,   20,
20201115, 1200,  , HU, 13.1N,  78.0W,  70,  982,  120,   90,   50,  100,   50,   40,   30,   50,   20,   20,    0,   20,
20201115, 0600,  , HU, 13.0N,  77.1W,  65,  988,  100,   80,   40,   90,   40,   40,   20,   30,   20,    0,    0,   20,
20201117, 1800,  , TS, 13.7N,  85.7W,  55,  988,  150,   70,    0,  140,   60,    0,    0,    0,    0,    0,    0,    0,
20201115, 0000,  , TS, 12.6N,  76.7W,  55,  992,   90,   80,   30,   70,   40,   40,    0,    0,    0,    0,    0,    0,
20201114, 1800,  , TS, 12.5N,  76.4W,  45,  997,   80,   80,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201118, 0000,  , TS, 13.8N,  86.7W,  40, 1000,  140,    0,    0,  130,    0,    0,    0,    0,    0,    0,    0,    0,
20201114, 1200,  , TS, 12.9N,  75.7W,  40, 1002,   80,   80,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201118, 0600,  , TS, 13.8N,  87.8W,  35, 1005,  140,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201114, 0600,  , TS, 13.3N,  75.0W,  35, 1004,   80,   80,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201114, 0000,  , TS, 13.6N,  74.5W,  35, 1005,   80,   80,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201113, 1800,  , TS, 14.0N,  74.1W,  35, 1005,   80,   80,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201113, 1200,  , TD, 14.4N,  73.7W,  30, 1006,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201118, 1200,  , TD, 13.7N,  89.0W,  25, 1006,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201113, 0600,  , LO, 14.7N,  73.3W,  25, 1007,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201113, 0000,  , LO, 15.0N,  72.7W,  25, 1008,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201112, 1800,  , LO, 15.3N,  71.9W,  25, 1009,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20201112, 1200,  , LO, 15.5N,  70.9W,  25, 1009,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
```
To pull data from the top portion of the file, we can use the `head` 
command, and can specify how many lines from the top we would like to pull
using the `-n` option.

Let's try an example in retrieving the first 5 lines of data on Hurricane Ivan
from file `AL092004_ivan.txt`:

```console
user@computer:~$ head -n 5 AL092004_ivan.txt
20040902, 1800,  , TD,  9.7N,  27.6W,  25, 1009,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 0000,  , TD,  9.7N,  28.7W,  30, 1007,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 0600,  , TS,  9.7N,  30.3W,  35, 1005,   50,    0,    0,   50,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 1200,  , TS,  9.5N,  32.1W,  40, 1003,   50,    0,    0,   50,    0,    0,    0,    0,    0,    0,    0,    0,
20040903, 1800,  , TS,  9.3N,  33.6W,  45, 1000,   60,  125,  125,   60,    0,    0,    0,    0,    0,    0,    0,    0,
```
We can also pull relative to the end of a dataset in a file using `tail`.
Let's try pulling the last 5 lines from `AL092004_ivan.txt`:

```console
user@computer:~$ tail -n 5 AL092004_ivan.txt
20040923, 1200,  , TS, 28.9N,  92.2W,  50,  998,   60,   60,   20,   40,   20,    0,    0,   20,    0,    0,    0,    0,
20040923, 1800,  , TS, 29.2N,  92.7W,  40, 1003,   50,   50,   20,   40,    0,    0,    0,    0,    0,    0,    0,    0,
20040924, 0000,  , TD, 29.6N,  93.2W,  30, 1003,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040924, 0200, L, TD, 29.8N,  93.6W,  30, 1004,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20040924, 0600,  , TD, 30.1N,  94.2W,  25, 1009,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
```
---

## Next Steps, Onto Final Lesson

For the final lesson in our workshop, let's take a look at [using pipes and other
tools to redirect outputs](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/f535af66199cf41499be66c191fa4e3cb207436d/05_Unix_intro_lib_summer_2022/05_unix_lib_piping.md) from commands into files and even other commands.

**Attribution**

> Some content in this workshop has been adapted and derived from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Hurricane data was retrieved from the [National Hurricane Center's Data Archive](https://www.nhc.noaa.gov/data/), and is derived from the [Best Track Data HURDAT2 dataset](https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2020-052921.txt). Please see the [NOAA website Use of NOAA/NWS Data and Products and Disclaimers](https://www.weather.gov/disclaimer) for more information regarding the data.

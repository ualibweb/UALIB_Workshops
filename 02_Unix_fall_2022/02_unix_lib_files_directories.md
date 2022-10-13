# Navigation and Directories

---
**Lesson Navigation**

1. [Introduction](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_introduction.md)
2. [Navigation and Directories](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_files_directories.md)
3. [Common Unix Commands](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_common_commands.md)
4. [Pipelines and Redirecting Data Outputs](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_piping.md)

---

As you prepare to analyze your data using the Bash Shell, it is important to 
understand how the shell organizes files and directories, how to move around 
within the shell, and how to interact with files and directories.

---
## Navigating the Unix File System

Let's start by getting an idea of the directory where you are currently working.
To do this, use the `pwd` command to assess the current directory out of which 
you are working.

```console
user@computer:~$ pwd
/home/user
```
By default, when opening the command line, your current working directory should
be the directory for the current user inside of your home folder.

Let's take a look at what other files or directories may be present in this the
current user directory using the `ls` command.

```console
user@computer:~$ ls
Desktop Documents Downloads Music Pictures Videos
```
Using the `ls` command lists all files and directories located within a folder. 
By default, these items are listed in alphabetical order. To get more information 
about those files and directories, you can use what is called a flag or option 
(for consistency, we will call these options throughout this workshop) like `-F` 
to determine which of these is a file, and which is a directory. 

With the `-F` option, directories have a `/` appended at the end of their name. 
For example:

```console
user@computer:~$ ls -F
Desktop/ Documents/ Downloads/ Music/ Pictures/ Videos/
```

There are a number of other options available for the `ls` command available by 
executing the help file with `ls --help`.

---
### Retrieveing Data Using the `wget` Command

If you are utilizing the library server Shell congifuration, your `home` directory 
will be pretty bare, likely only containing the `bin` directory.

From this point forward in the lesson, all examples will involve the directory 
and dataset associated with the `hurricane_data` directory available for download with [this repository](https://github.com/lsimpsonlibrary/UALIB_Workshops/archive/refs/heads/master.zip).

There are a variety of ways to access this data if you also have access to a 
Guided User Interface, or GUI, but for this workshop, we will access and download it through the command line.

In order to access the data, we will use the `wget` command, along with the 
corresponding URL for the data in the workshop GitHub repository. `wget` allows 
you to download files from the the web directly into the directory of your choice. 
If you do not specify a directory, the file will download into your current working directory.

For this, execute the following command in your terminal session:

```console
user@computer:~$ wget https://github.com/lsimpsonlibrary/UALIB_Workshops/archive/refs/heads/master.zip
```
Now, use `pwd` to see that your file was downloaded. Your directory should
look something like the following:

```console
user@computer:~$ pwd

bin master.zip
```

To extract the contents of `master.zip`, we will use the `unzip` command in SUSE
Linux using the following line of code:

```console
user@computer:~$ unzip master.zip
```

Using `pwd` again, you should see the following:

```console
user@computer:~$ pwd

bin master.zip UALIB_Workshops-master
```
Now that you have had a chance to take a look around in the directory where 
you are currently working, let's try moving to another directory using the `cd` 
command to change directories. For this command, we will need to supply an argument 
with the command using the directory to which we would like to move.

Up until this point, we have been operating from the `/home/user/` directory. 
Let's change the directory to `UALIB_Workshops-master`, which is one of the subdirectories 
available.

```console
user@computer:~$ cd UALIB_Workshops-master
```
Once the command is executed, the shell provides the prompt for the next command.
Now use `pwd` to assess that you are in the directory "UALIB_Workshops-master":

```console
user@computer:~$ pwd

/UALIB_Workshops-master

```
We will be working with files from a specific directory in `UALIB_Workshops-master`, so use the
`ls` command to see what file and directories are available.

```console
user@computer:~$ ls

01_MATLAB_fall_2020  02_Unix_fall_2020              LICENSE
01_MATLAB_fall_2021  03_Python_fall_2020            README.md
02_Unix1_fall_2021   04_Python_spring_2022
02_Unix2_fall_2021   05_Unix_intro_lib_summer_2022
```
Let's change the directory again using `cd` to `05_Unix_intro_lib_summer_2022`.

>*Shortcut: You can type the first few characters of the directory, and then press
the `tab` key to have the rest of the directory title propagate.*

From here, let's use `cd` to access to the directory `hurricane_data`

```console
user@computer:~$ cd hurricane_data
```
This is an example of moving down from one directory into its subdirectories. 
We can also move back up one level by using `cd ..`, or back to the home directory
by using `cd` with no argument.

To change to a specific directory outside of your current working directory, 
you must provide the absolute path instead of only the directory name, or the 
relative path. For example:

```console
user@computer:~$ cd /home/user/Desktop/hurricane_data
```
Or you can use the `~` in place of the home/user directory designation:

```console
user@computer:~$ cd ~/UALIB_Workshops-master/05_Unix_intro_lib_summer_2022/hurricane_data
```

To consider the use of absolute and relative paths, we will quote directly from 
[The Software Carpentries' lesson on "Navigating Files and Directories"](https://swcarpentry.github.io/shell-novice/02-filedir/index.html):

>So far, when specifying directory names, or even a directory path (as above), 
we have been using relative paths. When you use a relative path with a command 
like `ls` or `cd`, it tries to find that location from where we are, rather than 
from the root of the file system.

>However, it is possible to specify the absolute path to a directory by including
its entire path from the root directory, which is indicated by a leading slash. 
The leading `/` tells the computer to follow the path from the root of the file 
system, so it always refers to exactly one directory, no matter where we are when
we run the command.

**Note: you can also use absolute path name with `ls` to list contents of a 
directory different from your current working directory.**

---

## Files and Directories


Let's try a few tools in working directly with file and directories. First, 
navigate back to the `hurricane_data` directory using `cd`:

```console
user@computer:~$ cd ~/UALIB_Workshops-master/05_Unix_intro_lib_summer_2022/hurricane_data
```
We can take a quick look at what's in this directory using `ls`:

```console
user@computer:~$ ls

AL042007_dean.txt    AL122005_katrina.txt  AL182005_rita.txt
AL052019_dorian.txt  AL132003_isabel.txt   AL252005_wilma.txt
AL092004_ivan.txt    AL142018_michael.txt  AL312020_iota.txt
AL112017_irma.txt    AL152017_maria.txt    hurdat2-1851-2020-052921.txt
```
Let's make a new directory nested in the directory `hurricane_data`. To do this, 
we will use the command `mkdir`, and let's name the directory `outputs`:

```console
user@computer:~$ mkdir outputs
```
Now, use `ls -F` to see the directory with the other files:

```console
user@computer:~$ ls -F
AL042007_dean.txt     AL132003_isabel.txt   AL312020_iota.txt
AL052019_dorian.txt   AL142018_michael.txt  hurdat2-1851-2020-052921.txt
AL092004_ivan.txt     AL152017_maria.txt    outputs/
AL112017_irma.txt     AL182005_rita.txt
AL122005_katrina.txt  AL252005_wilma.txt
```
To create a new file, there are several commands that you can use. Using `touch`
followed by a space and a filename will create a blank file.

```console
user@computer:~$ touch example_file
user@computer:~$ ls
AL042007_dean.txt    AL122005_katrina.txt  AL182005_rita.txt   hurdat2-1851-2020-052921.txt
AL052019_dorian.txt  AL132003_isabel.txt   AL252005_wilma.txt  outputs
AL092004_ivan.txt    AL142018_michael.txt  AL312020_iota.txt
AL112017_irma.txt    AL152017_maria.txt    example_file
```
**Note: You do not have to specify a file type.**

To create a text file that can be immediately edited, you can use the [GNU text ednitor, Nano](https://www.nano-editor.org/docs.php). 'nano' is a program, and you can call it similar to calling a command.

```console
user@computer:~$ nano example2
```
Which will create the file `example2` and open the editor in the commandline 
window. Try adding the following text to your file `example2`, open in the `nano` 
editor:

```console
GNU nano 4.8                           example2

2004 ivan
2003 isabel
2020 iota
2017 irma 


              [ line 4/5 (80%), col 10/10 (100%), char 41/42 (97%) ]
^G Get Help   ^O Write Out  ^W Where Is   ^K Cut Text   ^J Justify    ^C Cur Pos
^X Exit       ^R Read File  ^\ Replace    ^U Paste Text ^T To Spell   ^_ Go To Line
```
To save the file, enter `CTRL O`, `Return`. To exit from the editor, use `CTRL X`.

To view the contents of a file, there are several different options as well.

The `less` command provides a quick view the contents of a file. Where `nano` 
is an actual program and text editor, and may take a few moments to read the data 
in the file and render it editable, `less` loads quickly and does not allow for
editing.

For example, let's take a look in the file `AL042007_dean.txt`:

```console
user@computer:~$ less AL042007_DEAN.txt
20070813, 0600,  , TD, 12.2N,  28.9W,  30, 1006,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20070813, 1200,  , TD, 12.1N,  30.7W,  30, 1005,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20070813, 1800,  , TD, 12.0N,  32.4W,  30, 1005,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20070814, 0000,  , TD, 11.9N,  34.5W,  30, 1005,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20070814, 0600,  , TD, 11.8N,  36.5W,  30, 1005,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20070814, 1200,  , TS, 11.8N,  38.3W,  35, 1004,   30,    0,    0,   30,    0,    0,    0,    0,    0,    0,    0,    0,
20070814, 1800,  , TS, 11.8N,  40.1W,  40, 1002,   45,   30,    0,   45,    0,    0,    0,    0,    0,    0,    0,    0,
20070815, 0000,  , TS, 11.9N,  41.7W,  50,  997,   45,   45,   30,   45,   25,    0,    0,    0,    0,    0,    0,    0,
20070815, 0600,  , TS, 12.0N,  43.4W,  50,  997,   45,   45,   30,   45,   20,    0,    0,    0,    0,    0,    0,    0,
20070815, 1200,  , TS, 12.3N,  45.1W,  50,  997,   45,   45,   30,   45,   20,    0,    0,   20,    0,    0,    0,    0,
20070815, 1800,  , TS, 12.8N,  47.0W,  55,  994,   60,   45,   30,   45,   20,    0,    0,   20,    0,    0,    0,    0,
20070816, 0000,  , TS, 13.0N,  49.2W,  60,  991,   60,   45,   30,   45,   20,    0,    0,   20,    0,    0,    0,    0,
20070816, 0600,  , HU, 13.2N,  51.3W,  70,  984,   60,   45,   30,   60,   30,   20,    0,   30,   20,    0,    0,   15,
20070816, 1200,  , HU, 13.5N,  53.3W,  80,  972,   90,   75,   40,   75,   40,   20,   10,   40,   20,   15,    5,   15,
20070816, 1800,  , HU, 13.8N,  55.5W,  80,  972,  120,   75,   40,  120,   50,   25,   10,   50,   20,   20,    5,   20,
20070817, 0000,  , HU, 14.0N,  57.7W,  80,  976,  120,   75,   40,  120,   50,   25,   10,   50,   20,   20,    5,   20,
20070817, 0600,  , HU, 14.2N,  59.8W,  80,  975,  120,   90,   40,  120,   50,   35,   10,   50,   20,   20,    5,   20,
20070817, 1200,  , HU, 14.4N,  61.7W,  90,  967,  120,  100,   50,  160,   80,   50,   20,   50,   20,   20,   10,   20,
20070817, 1800,  , HU, 14.8N,  63.5W, 110,  961,  160,  120,   70,  160,   80,   60,   30,   70,   25,   20,   20,   25,
20070818, 0000,  , HU, 14.9N,  65.1W, 125,  944,  180,  120,  100,  180,  100,   60,   50,  100,   50,   30,   30,   50,
20070818, 0600,  , HU, 15.0N,  66.6W, 145,  929,  180,  120,  100,  180,  100,   60,   50,  100,   50,   30,   30,   50,
20070818, 1200,  , HU, 15.4N,  68.0W, 145,  923,  200,  120,  100,  180,  100,   60,   50,  100,   50,   35,   30,   50,
20070818, 1800,  , HU, 15.9N,  69.5W, 130,  930,  200,  130,  100,  150,  100,   60,   50,  100,   50,   40,   30,   50,
20070819, 0000,  , HU, 16.1N,  71.0W, 120,  920,  180,  120,  100,  150,   90,   70,   70,   90,   50,   40,   40,   50,
20070819, 0600,  , HU, 16.4N,  72.6W, 120,  921,  180,  120,  100,  150,   90,   70,   70,   90,   50,   40,   40,   50,
20070819, 1200,  , HU, 16.8N,  74.3W, 125,  923,  180,  150,  100,  150,   90,   70,   70,   90,   50,   40,   40,   50,
20070819, 1800,  , HU, 17.1N,  76.0W, 125,  930,  180,  150,   75,  120,   80,   70,   50,   80,   50,   50,   30,   50,
20070820, 0000,  , HU, 17.5N,  77.8W, 125,  926,  180,  150,   75,  120,   80,   70,   50,   80,   50,   50,   30,   50,
20070820, 0600,  , HU, 17.6N,  79.8W, 130,  926,  180,  150,   75,  120,   80,   70,   50,   75,   50,   40,   30,   50,
20070820, 1200,  , HU, 17.8N,  81.5W, 130,  926,  150,  150,   85,  120,   90,   75,   50,   75,   50,   40,   30,   50,
20070820, 1800,  , HU, 18.0N,  83.3W, 135,  924,  150,  150,   85,  120,   90,   75,   50,   75,   50,   40,   30,   50,
20070821, 0000,  , HU, 18.2N,  85.1W, 145,  914,  150,  150,   90,  125,  100,   75,   50,  100,   50,   40,   30,   50,
20070821, 0600,  , HU, 18.6N,  86.9W, 150,  907,  180,  180,   90,  125,  100,   75,   50,  100,   50,   40,   30,   50,
20070821, 0830, L, HU, 18.7N,  87.7W, 150,  905, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,
20070821, 1200,  , HU, 18.9N,  88.7W, 110,  935,  210,  210,   75,   90,   60,   60,   40,   60,   40,   40,   20,   30,
20070821, 1800,  , HU, 19.2N,  90.5W,  75,  960,  175,  120,   60,  120,   60,   60,   40,   60,   30,   30,   20,   30,
20070822, 0000,  , HU, 19.7N,  92.2W,  65,  979,  175,  100,   75,  120,   75,   60,   60,   60,   30,   30,   20,   30,
20070822, 0600,  , HU, 20.1N,  94.0W,  70,  979,  175,  100,  100,  160,  100,   70,   80,   80,   60,    0,    0,   60,
```
To leave the `less` view of the file, press `q`. In a subsequent part of the 
workshop, we will review the `cat` command as a means of retrieving data from a file as well.

To copy a file or directory, use the `cp` command. Let's copy the file 
`AL042007_dean.txt` to the directory `outputs/`. To copy an item, you have to 
specify the item to copy, and the destination to which you want to copy the item.
For this example, to make a copy of `AL042007_dean.txt` in `outputs/`, the 
command will be as follows *don't forget the `tab` shortcut for file and directory
names:

```console
user@computer:~$ cp AL042007_dean.txt outputs
user@computer:~$ ls outputs/

AL042007_dean.txt
```


The `mv` command can be used to either rename a file or directory, or move a 
file or directory. 

For example, to rename a file, enter the command `mv`, followed by the name of
the file that you would like to change, and then the name to which you would 
like to change the file name:

```console
user@computer:~$ mv example2 example1
user@computer:~$ ls
AL042007_dean.txt    AL112017_irma.txt     AL142018_michael.txt  AL252005_wilma.txt  example_file
AL052019_dorian.txt  AL122005_katrina.txt  AL152017_maria.txt    AL312020_iota.txt   hurdat2-1851-2020-052921.txt
AL092004_ivan.txt    AL132003_isabel.txt   AL182005_rita.txt     example1            outputs
```
To move a file, use `mv` with the name of the file, followed by the directory 
to which you would like to move the file. For example:

```console
user@computer:~$ mv example1 outputs/
user@computer:~$ cd outputs
user@computer:~$ ls

example1
```
**Note: It is possible to overwrite files and directories with `cp` and `mv`. 
You can include an `-i` option with `mv` or `cp` to receive a prompt if your 
command will overwrite a file or directory. There is not option to undo actions
in the shell.**

---
### Wildcards

The shell allows for the use of wild cards alongside commands, allow for queries
to return more specific pieces information about the data with which you are 
working. The wildcards include `*` and `?`. The `*` allows for stemming, 
returning results that include characters specified before the `*`, and 
any characters that follow.

```console
user@computer:~$ cd ~/UALIB_Workshops-master/05_Unix_intro_lib_summer_2022/hurricane_data
user@computer:~$ ls *.txt
AL042007_dean.txt    AL092004_ivan.txt  AL122005_katrina.txt  AL142018_michael.txt  AL182005_rita.txt   AL312020_iota.txt
AL052019_dorian.txt  AL112017_irma.txt  AL132003_isabel.txt   AL152017_maria.txt    AL252005_wilma.txt  hurdat2-1851-2020-052921.txt
```
This request returns all files that have the `.txt` extension. However, we can 
be even more specific with our queries for the files in this directory. Each of 
the files follows a convention provided by the National Hurricane Center in their 
HURDAT2 dataset. The first two letters `AL`, indicate that the storm occured 
in the Atlantic basin. The second two digits indicate the storm number for that year. 
The next four digits are the year, with the text after the underscore being the 
name of the storm. 

Let's use the `?` in conjunction with the `*` to see how many storms we have 
data for from the 2010s:

```console
user@computer:~$ ls AL??201*
AL052019_dorian.txt  AL112017_irma.txt  AL142018_michael.txt  AL152017_maria.txt
```
What if we wanted to see how many of the storms for which we have data were 
named with a specific letter?

```console
user@computer:~$ ls AL??20??_i*
AL092004_ivan.txt  AL112017_irma.txt  AL132003_isabel.txt  AL312020_iota.txt
```
---
## Next Steps

Now, let's go to the [next lesson to take a look at some common Unix commands](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_common_commands.md).

---
**Attribution**
> Some content in this workshop has been adapted and derived from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Hurricane data was retrieved from the [National Hurricane Center's Data Archive](https://www.nhc.noaa.gov/data/), and is derived from the [Best Track Data HURDAT2 dataset](https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2020-052921.txt). Please see the [NOAA website Use of NOAA/NWS Data and Products and Disclaimers](https://www.weather.gov/disclaimer) for more information regarding the data.

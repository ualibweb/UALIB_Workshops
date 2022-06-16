# Introduction

---
**Lesson Navigation**

1. [Introduction](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_introduction.md)
2. [Navigation and Directories](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_files_directories.md)
3. [Common Unix Commands](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_common_commands.md)
4. [Pipelines and Redirecting Data Outputs](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_piping.md)
---

## What is a Unix Shell?

It is worth starting with some terminology. You have probably heard many different
terms for interacting with a computer via text input such as a shell, terminal, 
console, and command line. In practice, users are often using these terms 
interchangeably, but you should be aware that there are differences (see this 
[Unix Stack Exchange Thread](https://unix.stackexchange.com/questions/4126/what-is-the-exact-difference-between-a-terminal-a-shell-a-tty-and-a-con)).
And to quote from the community accepted answer:

> In unix terminology, the short answer is that
>    * terminal = tty = text input/output environment
>    * console = physical terminal
>    * shell = command line interpreter

Further, most users today are actually using a Unix-like operating system such as 
[GNU/Linux](https://www.gnu.org/gnu/linux-and-gnu.en.html). And most GNU/Linux distributions
use the Bash Shell with GNU Utilities (i.e., software utilities).

Let's quote a bit from the [Bash Manual](https://www.gnu.org/software/bash/manual/bash.html#Introduction):

> Bash is the shell, or command language interpreter, for the GNU operating system. 
The name is an acronym for the ‘Bourne-Again SHell’, a pun on Stephen Bourne, the author 
of the direct ancestor of the current Unix shell sh, which appeared in the 
Seventh Edition Bell Labs Research version of Unix. 

> At its base, a shell is simply a macro processor that executes commands...
> A Unix shell is both a command interpreter and a programming language. As a 
command interpreter, the shell provides the user interface to the rich set of 
GNU utilities. The programming language features allow these utilities to be combined.

With this workshop, we will shape the introduction of the Bash Shell with an eye
toward its use for analyzing data. This workshop is intended to be an introduction
for novice users, and will assume little to no prior knowledge in utlizing the shell.
Specifically, this workshops has been adapted for a training session with librarians at
[UA Libraries](http://lib.ua.edu/). This particular workshop is offered in two 
parts, with the first serving as an introduction to the Bash Shell, and the 
second serving as an application of these tools using [EDirect](https://dataguide.nlm.nih.gov/edirect/documentation.html)
for data extraction and analysis.

For this workshop, we will use datasets gathered from 
[The National Hurricane Center's Data Archive](https://www.nhc.noaa.gov/data/)
to demonstrate tools and commands in the Bash Shell. However, following the 
workshop, it is recommended to consider datasets that may be relevant to you in 
practicing use of these commands and tools.

### The Unix Philosophy

As we begin our work in the Bash Shell, it's important to consider a few parts of
what's known as The Unix Philosophy.

One of the many contributors to what we know as Unix, Doug McIlroy, is quoted by Peter Salus in his book, [*A Quarter-Centry of Unix*](http://www.worldcat.org/oclc/60165734), as saying:
>This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.

The Unix or Bash Shell is comprised of a set of simple, yet powerful tools. Let's get started putting them to work!

---

## Access to a Shell

For this workshop, it is best if you are using a Bash Shell with GNU Utilities in a GNU/Linux distribution. We will be using a terminal accessed through SSH client PuTTy, and using an enterprise version of [SUSE Linux](https://www.suse.com/) available through a virtual server. Secure access is provided through UA OIT, and in order to access this server while on UA's campus, you will need register for one of our workshops.

If you want to try out these exercises later using your own machine, you may consider installing [Ubuntu Linux](https://ubuntu.com/) in a virtual machine on Mac OS or Windows using software such as the open-source [Virtual Box](https://www.virtualbox.org/). Microsoft now offers the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about), which provides access to a Bash shell without the need to create a virtual machine.

Alternative options are available in Mac OS Terminal (you can [change the default shell from zsh to Bash](https://support.apple.com/guide/terminal/change-the-default-shell-trml113/mac)), and Windows through emulators like [Cygwin](https://en.wikipedia.org/wiki/Cygwin),  [GitBash](https://git-scm.com/downloads), however commands and utilities might be different with these alternative options.

---

## Setup Files

If you are going to follow along with us, you will need a copy of the tabular data files we will use throughout the workshop. The easiest way to get these files is to download this UALIB_Workshops repository as a ZIP file, unarchive the file, then copy the `hurricane_data` folder in `UALIB_Workshops/02_Unix_fall_2021/` to your Desktop. We will use this dataset to test out several commands later in the workshop.

As a part of the workshop, we will access and download this data directly through the commandline useing the `wget` command.  If you would like to access the data this way, instructions will be available in the next lesson.

---

### Dataset Information

The files in this folder include datasets for each of the most intense hurricanes between 2000 and 2020, and a larger dataset that includes data for all tropical systems in the Atlantic Basin between 1851 and 2020. These files were derived from the ["Best Track Data (HURDAT2)"](https://www.nhc.noaa.gov/data/#hurdat) dataset, a product of the [National Hurricane Center](https://www.nhc.noaa.gov/data/). 

For more information on how to read and utilize this data set, check out ["The revised Atlantic hurricane database (HURDAT2) November 2019"](https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-nov2019.pdf) from NHC's Chris Landsea and Jack Beven.

---
## Let's Get Started!

If you are accessing this lesson asychronously, launch a session in your preferred iteration of the Bash Shell.

---

**Launch your Bash Shell (in our case Gnome terminal):**

```console
user@computer:~$ 
```
We type commands and text after the `$` symbol. Commands follow a specific syntax in Bash that will include the command, a space, any options associated with the command, and the argument or item that the command is to act upon. Once you have entered the full text of your command or query, press enter to execute it. For our UA Libraries team, instead of the `$`, you will see `>`.

Let's try our first command, for luck. Type the following command into your terminal session, and press `enter`/`return`:

```console
user@computer:~$ echo "Hello, World!"

Hello, World!
```

You've now used your first command! The `echo` command can be used to print text on screen.

---

## Accessing Documentation

The first step to learning any new computing skill is to know how to get help and access the documentation. The documentation will allow you to discover utilities and show you how to construct the appropriate syntax for usage.

As an example, let's search for the manual pages using the `man` command to find information about the utility, `cat`.

```console 
user@computer:~$ man cat
```
This action will take you to the manual page for the utility `cat`. 

There are two main ways to access the documentation. The first is to view the manual pages with the command we learned, `man`. If you know the name of the utility or command such as, you can access the manual page directly.

If you do not know what utility you are looking for, you can search the manual pages and output a list of matches. 

For example, if we want to search the manual pages for the word "compare":

```console
user@computer:~$ man -k `compare`
```
The `-k` option searched the short descriptions in the manual pages for the keyword. In our example above, the keyword was "compare". 


You can see all `man` options by accessing the manual page for `man`:

```console
user@computer:~$ man man
```
The second method to access documentation is to view the help file for a specific utility, which is usually done by adding `--help` after the utility name:

```console
user@computer:~$ cat --help
```
It is also important to note that commands, options, and file/directory names are case sensitive in the shell.

---

## Getting Started

Before we take a look at navigation, and files and directories within the shell. There are a few quick tools and commands that it is great to know in getting started. With these tools, consider that utilizing a command line interface is all about creating efficient workflows, and for the context of this workshop, efficient workflows for managing and analyzing data.

One tool that can be of significant value is using the `up` and `down` arrow keys.  This allows the user to sort through up to 1000 previously entered commands or queries to either reuse, or make quick edits before executing again.  This especially helpful for longer or complicated queries!

You can also clear all commands and outputs from your screen using the `clear` command. This does not delete data, or undo any commands.

```console
user@computer:~$ clear
```

**Other utilizies that may be useful include the following:**

You can call for the date using the `date` utility:

```console
user@computer:~$ date
Wed 01 Sep 2021 03:08:30 PM CDT
```
The `cal` utility will provide a calendar for the current month:

```console
user@computer:~$ cal

 October 2021
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
```
To close the shell session, type `exit` and then press return or enter.

```console
user@computer:~$ exit
```
---

## Next Steps

Now that we've had a chance to try out a few of the utilities in the Bash Shell, let's take a look at organization and how to navigate and interact with [files and directories](https://github.com/lsimpsonlibrary/UALIB_Workshops/blob/12a60225d25eda0b12f88ffd4b926d1a8b4a8218/05_Unix_intro_lib_summer_2022/05_unix_lib_files_directories.md) in our next lesson.

---

**Attribution**

> Some content in this workshop has been adapted and derived from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Hurricane data was retrieved from the [National Hurricane Center's Data Archive](https://www.nhc.noaa.gov/data/), and is derived from the [Best Track Data HURDAT2 dataset](https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2020-052921.txt). Please see the [NOAA website Use of NOAA/NWS Data and Products and Disclaimers](https://www.weather.gov/disclaimer) for more information regarding the data.

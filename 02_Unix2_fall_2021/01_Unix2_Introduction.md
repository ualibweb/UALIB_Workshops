# Introduction

**Lesson Navigation**

   1. Introduction
   2. cat, tac, head, and tail
   3. wc and nl
   4. sort and uniq
   5. split and shuf
   6. cut, paste, and join
   7. tr and sed
   8. grep
   9. comm and diff

## What is a Unix Shell?

It is worth starting with some terminology. You have probably heard many different terms for interacting with a computer via text input such as a shell, terminal, console, and command line. In practice, users are often using these terms interchangeably, but you should be aware that there are differences (see this [Unix Stack Exchange Thread](https://unix.stackexchange.com/questions/4126/what-is-the-exact-difference-between-a-terminal-a-shell-a-tty-and-a-con)). And to quote from the community accepted answer:

> In unix terminology, the short answer is that
>    * terminal = tty = text input/output environment
>    * console = physical terminal
>    * shell = command line interpreter

Further, most users today are actually using a Unix-like operating system such as [GNU/Linux](https://www.gnu.org/gnu/linux-and-gnu.en.html). And most GNU/Linux distributions use the Bash Shell with GNU Utilities (i.e., software utilities).

Let's quote a bit from the [Bash Manual](https://www.gnu.org/software/bash/manual/bash.html#Introduction):

> Bash is the shell, or command language interpreter, for the GNU operating system. The name is an acronym for the ‘Bourne-Again SHell’, a pun on Stephen Bourne, the author of the direct ancestor of the current Unix shell sh, which appeared in the Seventh Edition Bell Labs Research version of Unix. 

> At its base, a shell is simply a macro processor that executes commands...
> A Unix shell is both a command interpreter and a programming language. As a command interpreter, the shell provides the user interface to the rich set of GNU utilities. The programming language features allow these utilities to be combined.

## Support and Resources

1. [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
2. [GNU Core Utilities Manual](https://www.gnu.org/software/coreutils/manual/)
3. [Software Carpentry The Unix Shell](http://swcarpentry.github.io/shell-novice/)
4. [Unix and Linux Stack Exchange](https://unix.stackexchange.com/)
5. [LinuxCommand.org](http://linuxcommand.org/) / [LinuxCommand (PDF version)](https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf/download)

## Access to a Shell

For this workshop, it is best if you are using a Bash Shell with GNU Utilities in a GNU/Linux distribution. We will be using the Gnome Terminal in Ubuntu for access to Bash Shell. If you want to follow along with us, you may consider installing [Ubuntu Linux](https://ubuntu.com/) in a virtual machine on Mac OS or Windows using software such as the open-source [Virtual Box](https://www.virtualbox.org/). 

Alternative options are available in Mac OS Terminal, and Windows through emulators like [Cygwin](https://en.wikipedia.org/wiki/Cygwin) or the [Windows Subsystem for Linux](https://ubuntu.com/wsl), however commands and utilities might be different with these alternative options. We are working on making access to the Bash Shell more accessible in future workshops.

## Setup Files

If you are going to follow along with us, you will need a copy of the tabular data files we will use throughout the workshop. The easiest way to get these files is to download this UALIB_Workshops repository as a ZIP file, unarchive the file, then copy the `Udata2` folder in `UALIB_Workshops/02_Unix2_fall_2021/` to your Desktop. Note that you may need to change your directory to the data folder (and/or subfolders) as we work through the workshop, for example:

```console

user@computer:~$ cd /home/user/Desktop/Udata2/
user@computer:~$ cd /home/user/Desktop/Udata2/folder1

```

## Accessing Documentation

The first step to learning any new computing skill is to know how to get help and access the documentation. The documentation will allow you to discover utilities and show you how to construct the appropriate syntax for usage.

Launch your Bash Shell (in our case Gnome terminal):

```console

user@computer:~$ 

```

We type commands and text after the `$` symbol. There are four main ways to access the documentation. The first is to view the manual pages with `man`. If you know the name of the utility such as `cat`, you can access the manual page directly:

```console

user@computer:~$ man cat

```
If you do not know what utility you are looking for, you can search the manual pages and output a list of matches. For example, if we want to search the manual pages for the word "compare":

```console

user@computer:~$ man -k 'compare'

```
The `-k` option searched the short descriptions in the manual pages for the keyword. In our example above, the keyword was "compare". You can see all `man` options by accessing the manual page for `man`:

```console

user@computer:~$ man man

```
The second method to access documentation is to view the help file for a specific utility, which is usually done by adding `--help` after the utility name:

```console

user@computer:~$ cat --help

```

The third way to access documentation is with `info`. The [GNU Info](https://www.gnu.org/software/texinfo/manual/info-stnd/info-stnd.html) reader is another way to access documentation and can sometimes provide more information (such as examples) compared to `man` or `--help`. For example, compare the following two documentation outputs for `join`:

```console

user@computer:~$ man join

user@computer:~$ info join

```
The last way to find documentation is to read it online. Here is a link to the GNU manuals:

https://www.gnu.org/doc/doc.html

## Pipes

[Pipes](https://en.wikipedia.org/wiki/Pipeline_(Unix)), `|`, are an important concept in the ["Unix Philosophy"](https://en.wikipedia.org/wiki/Unix_philosophy) and allow for easy combination of commands:

```console
user@computer:~$ something1 | something2 | something3

```
The above syntax creates a sequence of commands. The output from `something1` is used as the input into `something2`, and then the output from `something2` is used as the input for `something3`. This is a powerful approach and allows us to combine simple tasks into much more complex processes. 


## Scope of this Workshop

We are going to focus on introducing a variety of GNU utilities useful for working with tabular data. Our focus today will be on a basic use of the listed utilities in the lesson navigation. For more details, advanced options, and use-cases, we encourage you to read the GNU documentation pages.

---

**Attribution**

> Some content in this workshop have been adapted and derive from the Software Carpentry [The Unix Shell lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/shell-novice/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/shell-novice/LICENSE.html)). We reused a few parts of their lesson including some descriptions and command examples, but included our own specific datasets and use-case workflows. We have maintained the MIT license for program and code examples. Molecular and bibliographic dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.


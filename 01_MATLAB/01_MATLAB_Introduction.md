# What is MATLAB?

**Attribution**

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html)). In general, we reused parts of their lesson including the basic structure, some descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples. We have maintained the MIT license for program and code examples. Molecular dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

## What is MATLAB?

[MathWorks MATLAB](https://www.mathworks.com/products/matlab.html) is a complete interactive desktop environment and programming language. MATLAB is used by Mathematicians, Scientists, Engineers and others for numeric computation, data analysis, data visualization, and creation of applications. There are a variety of MATLAB [add-on toolboxes](https://www.mathworks.com/products.html) for solving specific problems, for example, in computational biology or image processing.


## Support and Resources

MATLAB has excellent documentation, support, and user created forums and learning materials. Here are a few recommended resources:

* [MathWorks MATLAB Documentation](https://www.mathworks.com/help/matlab/)
* [MathWorks MATLAB Tutorials](https://www.mathworks.com/help/matlab/getting-started-with-matlab.html)
* [MATLAB Central User Community](https://www.mathworks.com/matlabcentral/)
* [Stackoverflow MATLAB Questions](https://stackoverflow.com/questions/tagged/matlab)
* [Software Carpentry Programming with MATLAB](http://swcarpentry.github.io/matlab-novice-inflammation/)

We also have many MATLAB eBooks available from The University of Alabama Libraries. Try a [Scout](https://www.lib.ua.edu/scout/) search for `Matlab` in the record title and limit to eBooks:

`TI (Matlab) AND PT eBook AND FT Y`

## Access and Installation

The University of Alabama maintains a site license to MATLAB and Simulink, as well as many of the add-on toolboxes. See the [UA Office of Information Technology](https://oit.ua.edu/software/matlab/) website for access and installation instructions. MATLAB is available for Windows, Mac, and Linux.

## Starting MATLAB

Windows and Mac users can open MATLAB similarly to other installed programs. Linux users will need to open a terminal window and type `matlab` to launch MATLAB.

```console

user@computer:~$ matlab

```
## MATLAB GUI

MATLAB has a tabbed toolbar interface and four main windows:

* **Current Folder:** For file directory viewing and navigation
* **Command Window:** For entering and executing MATLAB commands. Users input commands at the MATLAB prompt, `>>`, and then execute with the `Enter` keyboard button.
* **Editor:** Allows input of multiple lines of code and sequential execution, which is useful for running scripts.
* **Workspace:** For viewing stored variables.

## Accessing Documentation for MATLAB functions

MATLAB has many built in features and functions, so it is important to know how to access documentation and help from within MATLAB. You can access the documentation reference pages directly from the MATLAB toolbar or from the Command Window using `doc`:

```Matlab

>> doc

```
The doc function will open the MATLAB documentation in a new window browser. You can search the documentation with the `docsearch` function from the Command Window, for example, if we wanted to find all documentation pages mentioning `histogram`:

```Matlab

>> docsearch histogram

```

MATLAB also contains help entries for functions and these can be viewed with `help`. For example, if we wanted to view help for the `mean` function:

```Matlab

>> help mean
 mean   Average or mean value.
    S = mean(X) is the mean value of the elements in X if X is a vector. 
    For matrices, S is a row vector containing the mean value of each 
    column. 
...
...
...
```

Finally, we can search the help entries with `lookfor`. Below, we find all functions containing the word `plot`:

```Matlab

>> lookfor plot
cellplot                       - Display graphical depiction of cell array.
etreeplot                      - Plot elimination tree.
gplot                          - Plot graph, as in "graph theory".
treeplot                       - Plot picture of tree.
plot                           - Alpha shape plot
plot                           - Plot a polyshape object
odeplot                        - Time series ODE output function.
...
...
...
```

Should you use Documentation or Help? Use both!

## Setup

We will be using a text file dataset, CID51840_similar.txt, for a few of the examples during the workshop. The easiest way to get this file setup is probably to download this GitHub Repository ([UALIB_Workshops](https://github.com/vfscalfani/UALIB_Workshops/archive/master.zip)) as a zip file, then unarchive the zip file. Finally, copy the MATLAB Mdata folder (UALIB_Workshops/01_MATLAB/Mdata) to a convenient location such as your desktop. After copying thee Mdata folder to your desktop, open MATLAB, and change the working directory in the Command Window to the Mdata folder path:

```Matlab

>> cd('/home/myusername/Desktop/Mdata')

```

There are many different ways to import data into MATLAB. We will use the `readtable` function. The `readtable` function creates a table from delimited text files and other formats like .xls and .ods.

```Matlab

>> myCIDdata = readtable('CID51840_similar.txt','Format','%s %s %s %f %d %d %d')

myCIDdata =

  574×7 table

                               IsomericSmiles                                     CID         MolecularFormula     MolecularWeight    RotatableBondCount    HeavyAtomCount    AtomChiralCount
    _____________________________________________________________________    _____________    _________________    _______________    __________________    ______________    _______________

    {'CCN(CC(=O)C)C(C1=CC=CC=C1)C(=O)OC(C)(C)C'                         }    {'146168522'}    {'C17H25NO3'    }         291.4                  8                  21                 1       
    {'CCN(CC(=O)OCC)C(C1=CC=CC=C1)C(=O)OC'                              }    {'146168519'}    {'C15H21NO4'    }        279.33                  9                  20                 1       
    {'C1=CC=C(C=C1)CN(CC2=CC=CC=C2)C(C3=CC=C(C=C3)F)C(=O)O'             }    {'146161459'}    {'C22H20FNO2'   }         349.4                  7                  26                 1       
    {'CC.CCCN1CCN(CC1)C(C2=CC=CC=C2CC)C(=O)O'                           }    {'145524776'}    {'C19H32N2O2'   }         320.5                  6                  23                 1       
    {'CC.CC.CCC.CC(=C)N1CCN(CC1)C(C2=CC=CC=C2)C(=O)O'                   }    {'145520251'}    {'C22H40N2O2'   }         364.6                  4                  26                 1       
    {'CC.CC(C)N(C)C(CC1=CC=CC=C1)C(=O)O'                                }    {'145086414'}    {'C15H25NO2'    }        251.36                  5                  18                 1       
    {'CN(C)C(C1=CC=CC=C1C(F)(F)F)C(=O)O.Cl'                             }    {'144259917'}    {'C11H13ClF3NO2'}        283.67                  3                  18                 1       
...
...
...
```

The above command imports the data within the `CID51840_similar.txt` file using the built in MATLAB `readtable` function and then saves the data as a variable called `myCIDdata`. The format option was added in order to specify the data type format for each of the seven columns. `%s` is a character vector, `%f` is a floating point number, and `%d` is an integer. The data is a collection of molecules that are similar to PubChem Compound Identifier (CID) 51840. The molecules are represented in a linear notation called [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) and some associated data is included about the molecules such as their molecular weight and heavy atom counts. It is not necessary that you fully understand what this data represents, but rather understand that it is tabular data with a mixture of character and numeric data.





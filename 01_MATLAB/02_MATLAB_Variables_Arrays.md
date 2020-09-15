# Variables and Arrays

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html). In general, we reused parts of their lesson including the basic structure, descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples.

## Assigning Variables

In the Introduction, we briefly mentioned variables. Variables store data in memory and are assigned with an equal sign, `=`. For example, the following statement creates a variable, 10, which is a 1x1 array, named A:

```Matlab

>> A = 10

A =

    10

```

Note that variable names must start with a letter, not contain any spaces, and are case sensitive. We can create larger arrays in MATLAB using brackets and semicolons to designate the start of a new row:

```Matlab

>> B = [20 30 40]

B =

    20    30    40

>> C = [20 30 40; 50 60 70]

C =

    20    30    40
    50    60    70

```

Similarly, text data can be saved as variables:

```Matlab

>> state = 'Alabama'

state =

    'Alabama'

>> states = ["Alabama"; "Mississippi"; "Florida"]

states = 

  3×1 string array

    "Alabama"
    "Mississippi"
    "Florida"
```

And we can even mix text and numbers together in a special data class (more on this below) called cell arrays, which are created with curly brackets:

```Matlab

>> state_data = {"Alabama", 10; "Mississippi", 20; "Florida", 30}

state_data =

  3×2 cell array

    {["Alabama"    ]}    {[10]}
    {["Mississippi"]}    {[20]}
    {["Florida"    ]}    {[30]}

```

## MATLAB Classes

Variables in MATLAB can be saved as many different types of [classes](https://www.mathworks.com/help/matlab/matlab_prog/fundamental-matlab-classes.html). A convenient function for inspecting variables is `whos`:

```Matlab

>> whos
  Name              Size             Bytes  Class     Attributes

  A                 1x1                  8  double              
  B                 1x3                 24  double              
  C                 2x3                 48  double              
  myCIDdata       574x7             253528  table               
  state             1x7                 14  char                
  state_data        3x2               1106  cell                
  states            3x1                266  string 

```

So far we have saved our variables as a few different MATLAB classes including the double (default for numeric data), table, character, cell, and string class. There are also data classes such as logical and structure arrays. Each class has its specific use-case and purpose. A reasonable place to start with MATLAB is to use the double class for numeric data, character or string class for text data, and then cells or tables for storing different types of data in the same class (e.g., mixing text and numbers). Of course, you may have to experiment with the best data class for each application, as there is often not a right or wrong choice.

MATLAB contains many functions for converting data into different classes. For example, if we wanted to convert our myCIDdata table into a cell array:

```Matlab

>> myCIDdata_C = table2cell(myCIDdata)

myCIDdata_C =

  574×7 cell array

```

It is often useful to be able to delete variables. Variables can be deleted with the function `clear`, but be careful because executing `clear` will delete all variables. To delete only one variable, you need to add the variable name, for example, to delete the state variable:

```Matlab

>> clear state

```

## Indexing

..





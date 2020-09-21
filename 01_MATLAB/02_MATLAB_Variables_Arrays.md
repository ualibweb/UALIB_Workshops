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

>> C = [20 30 40; 50 60 70; 80 90 100]

C =

    20    30    40
    50    60    70
    80    90   100

```

Similarly, text data can be saved as variables:

```Matlab

>> state = 'Alabama'

state =

    'Alabama'

>> states = ["Alabama" "Mississippi" "Georgia"; "Virginia" "North Carolina" "South Carolina" ]

states = 

  2×3 string array

    "Alabama"     "Mississippi"       "Georgia"       
    "Virginia"    "North Carolina"    "South Carolina"

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
  C                 3x3                 72  double              
  myCIDdata       574x7             253528  table               
  state             1x7                 14  char                
  state_data        3x2               1106  cell                
  states            2x3                458  string

```

So far we have saved our variables as a few different MATLAB classes including the double (default for numeric data), table, character, cell, and string class. There are also data classes such as logical and structure arrays. Each class has its specific use-case and purpose. A reasonable place to start with MATLAB is to use the double class for numeric data, character or string class for text data, and then cells or tables for storing different types of data in the same class (e.g., mixing text and numbers). Of course, you may have to experiment with the best data class for each application, as there is often not a right or wrong choice.

MATLAB contains many functions for converting data into different classes. For example, if we wanted to convert our myCIDdata table into a cell array:

```Matlab

>> myCIDdata_C = table2cell(myCIDdata)

myCIDdata_C =

  574×7 cell array

```

It is often useful to be able to delete variables. Variables can be deleted with the function `clear`, but be careful because executing `clear` will delete all variables. To delete only one variable, you need to add the variable name. For example, to delete the state variable:

```Matlab

>> clear state

```

## Indexing

Indexing into arrays allows us to select a subset of values. Working with a subset of values is often necessary during data preparation and analysis. Selecting single values can be performed by specifying the row and column in the form `array(row,col)`. So, for example, if we want the value of array C in row 3, column 2:

```Matlab

>> C

C =

    20    30    40
    50    60    70
    80    90   100

>> C(3,2)

ans =

    90

```

To specify an entire row or column, we can use `:`. For example, index out row 2, all columns:

```Matlab

>> C(2,:)

ans =

    50    60    70

```

Ranges can also be specified using `:`, for example if we want to index out only rows 2 and 3 within columns 1 and 2:

```Matlab

>> C(2:3,1:2)

ans =

    50    60
    80    90
```

Note that if indexing to an end row or column, we can use `end` instead of specifying the number of the last row/col:

```Matlab

>> C(2:end,1:2)

ans =

    50    60
    80    90

```

Indexing into character text data can be achieved by specifying a range of characters, starting at index position 1. For example,  if we wanted to index out all characters staring at index position 4 to the end:

```Matlab

>> state(4:end)

ans =

    'bama'

```

There are a couple different ways to access data in [cell arrays](https://www.mathworks.com/help/matlab/matlab_prog/access-data-in-a-cell-array.html) (e.g., state_data) and string arrays (e.g., states). If you want to create a subsection of the array and maintain the original data class, use smooth parentheses:

```Matlab

>> state_data

state_data =

  3×2 cell array

    {["Alabama"    ]}    {[10]}
    {["Mississippi"]}    {[20]}
    {["Florida"    ]}    {[30]}

>> state_data(3,1)

ans =

  1×1 cell array

    {["Florida"]}


>> states

states = 

  2×3 string array

    "Alabama"     "Mississippi"       "Georgia"       
    "Virginia"    "North Carolina"    "South Carolina"

>> states(1,:)

ans = 

  1×3 string array

    "Alabama"    "Mississippi"    "Georgia"

```

To access the contents of the cells, use curly braces instead:

```Matlab

>> state_data{3,1}

ans = 

    "Florida"

>> states{1,:}

ans =

    'Alabama'


ans =

    'Mississippi'


ans =

    'Georgia'

```

There are a variety of methods to [access data in tables](https://www.mathworks.com/help/matlab/matlab_prog/access-data-in-a-table.html). Similarly to cell array indexing, if we want to maintain the original table data class and create a subsection, use smooth parentheses:

```Matlab

>> myCIDdata

myCIDdata =

  574×7 table

                               IsomericSmiles                                     CID         MolecularFormula     MolecularWeight    RotatableBondCount    HeavyAtomCount    AtomChiralCount
    _____________________________________________________________________    _____________    _________________    _______________    __________________    ______________    _______________

    {'CCN(CC(=O)C)C(C1=CC=CC=C1)C(=O)OC(C)(C)C'                         }    {'146168522'}    {'C17H25NO3'    }         291.4                  8                  21                 1       
    {'CCN(CC(=O)OCC)C(C1=CC=CC=C1)C(=O)OC'                              }    {'146168519'}    {'C15H21NO4'    }        279.33                  9                  20                 1       
    {'C1=CC=C(C=C1)CN(CC2=CC=CC=C2)C(C3=CC=C(C=C3)F)C(=O)O'             }    {'146161459'}    {'C22H20FNO2'   }         349.4                  7                  26                 1       
    {'CC.CCCN1CCN(CC1)C(C2=CC=CC=C2CC)C(=O)O'                           }    {'145524776'}    {'C19H32N2O2'   }         320.5                  6                  23                 1       
    {'CC.CC.CCC.CC(=C)N1CCN(CC1)C(C2=CC=CC=C2)C(=O)O'                   }    {'145520251'}    {'C22H40N2O2'   }         364.6                  4                  26                 1            
...
...


>> myCIDdata(:,2:4)

ans =

  574×3 table

         CID         MolecularFormula     MolecularWeight
    _____________    _________________    _______________

    {'146168522'}    {'C17H25NO3'    }         291.4     
    {'146168519'}    {'C15H21NO4'    }        279.33     
    {'146161459'}    {'C22H20FNO2'   }         349.4     
    {'145524776'}    {'C19H32N2O2'   }         320.5     
    {'145520251'}    {'C22H40N2O2'   }         364.6     
...
...

``` 

If instead, we want to index out specific contents of the table cells, use curly parentheses:

```Matlab

>> myCIDdata{:,4}

ans =

  291.4000
  279.3300
  349.4000
  320.5000
  364.6000
...
...

```

Finally, tables also allow dot indexing, where we can specify a particular named column to index out:

```Matlab
>> myCIDdata.HeavyAtomCount

ans =

  574×1 int32 column vector

   21
   20
   26
   23
   26
...
...

>> myCIDdata.HeavyAtomCount(1:10)

ans =

  10×1 int32 column vector

   21
   20
   26
   23
   26
   18
   18
   17
   18
   20

```


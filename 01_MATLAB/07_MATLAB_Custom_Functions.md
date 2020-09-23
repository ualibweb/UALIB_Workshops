# Custom Functions

**Attribution**

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html)). In general, we reused parts of their lesson including the basic structure, some descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples. We have maintained the MIT license for program and code examples. Molecular dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

## Creating Your Own Functions

Creating your own custom functions can be useful for repeating multiple lines of code with a single command. Custom functions are saved as `.m` files with the function name and can be accessed from the current working directory. In MATLAB, custom functions have the following general form:

```Matlab

function [out1, out2] = function_name(in1, in2)
    %function_name   function description

    % commands
    out1 = calculate something 1
    out2 = calculate something 2
end

```

Here is a simple example function to convert inches to centimeters:

```Matlab

function [out_cm] = inches_to_cm(inches_in)
%inches_to_cm convert inches to centimeters
out_cm = inches_in * 2.54;
end

```
And to use our new function:

```Matlab

>> inches_to_cm(23)

ans =

   58.4200

```

Let's return to our script we wrote while learning about conditional statements that checked for presence of a + OR - character in a SMILES string:

```Matlab

>> smi = myCIDdata{:,1}

smi =

  574×1 cell array

    {'CCN(CC(=O)C)C(C1=CC=CC=C1)C(=O)OC(C)(C)C'                         }
    {'CCN(CC(=O)OCC)C(C1=CC=CC=C1)C(=O)OC'                              }
    {'C1=CC=C(C=C1)CN(CC2=CC=CC=C2)C(C3=CC=C(C=C3)F)C(=O)O'             }
    {'CC.CCCN1CCN(CC1)C(C2=CC=CC=C2CC)C(=O)O'                           }
...
...
    {'CCCCCCCCCC(=O)NC(C1=CC=CC=C1)C(=O)O'                              }
    {'CC1CC1N(C)C(C2=CC=CC=C2)C(=O)O.Cl'                                }
    {'CN(C)C(C1=CC=CC=C1)C(=O)[O-].[Na+]'                               }
    {'C1=CC=C(C=C1)C(C(=O)O)N(C=O)C=O'                                  }
    {'[2H]CN(C[2H])C(C1=CC=CC=C1)C(=O)O'                                }
    {'CC(C)C(C(C)C)N(C)C(C1=CC=CC=C1)C(=O)O.Cl'                         }
    {'[2H]CN(C(C1=CC=CC=C1)C(=O)O)C(=O)OC(C)(C)C'                       }
    {'C1=CC=C(C=C1)C(C(=O)O)N(CCN(CC(=O)O)CC(=O)O)C(C(=O)O)(O)O'        }
...
...

```


```Matlab

>> smi = myCIDdata{:,1};
result1 = cell(length(smi),1); % this preallocates our variable for speed
for j = 1:length(smi)
    if count(smi{j},'+') > 0 || count(smi{j},'-') > 0
       result1{j,1} = true; % this saves the results in row j, column 1
    else
       result1{j,1} = false;  
    end
end

>> result1

result1 =

  574×1 cell array

    {[0]}
    {[0]}
    {[0]}
    {[0]}
...
...   
    {[0]}
    {[0]}
    {[1]}
    {[0]}
    {[0]}
    {[0]}
    {[0]}
    {[0]}
    {[0]}
    {[0]}
    {[0]}    
...
...
```

We can rewrite this task as a function:

```Matlab

function [out] = contains_charge(smi_in)
%contains_charge this function checks for presences of + or - characters
%   A conditional if statement is used and returns true or false

num_positive = count(smi_in,'+');
num_negative = count(smi_in,'-');

  if num_positive > 0 || num_negative > 0
    out = true;
  else  
    out = false;
  end

end
```

And now to use the function, we save the function as contains_charge.m and use it similarly to other functions in MATLAB:

```Matlab

>> contains_charge('CCC(CCN(C)C(C1=CC=CC=C1)C(=O)O)O')

ans =

  logical

   0

>> contains_charge('CCCCCOC(=O)[C@H](C1=CC=CC=C1)[N+](C)(C(C)(C)C)C(C)(C)C')

ans =

  logical

   1

```

If we want to apply the function to an entire cell array (e.g., our column of SMILES strings), we can use the MATLAB `cellfun` function to apply the function to each cell:


```Matlab

>> smi = myCIDdata{:,1};
result2 = cellfun(@contains_charge,smi)

result2 =

  574×1 logical array

   0
   0
   0
   0
   0
...
... 
   0
   0
   1
   0
   0
   0
   0
   0
   0
   0

...
...
```

As a check, let's compare the results from result1 and result2. If we check for equality with `isequal`, the returned logical array will return 1 for true or 0 for false:


```Matlab

>> comparison = isequal(cell2mat(result1), result2)

comparison =

  logical

   1
```

Yes, looks like our two methods produced the same results. Note that the `cell2mat` function was used to convert the cell array to the logical data within the cells.




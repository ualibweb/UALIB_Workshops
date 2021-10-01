# Conditional Statements

**Lesson Navigation**

   1. [Introduction, Overview of the MATLAB GUI, and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/01_MATLAB_Introduction.md)
   2. [Variables and Arrays](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/02_MATLAB_Variables_Arrays.md)
   3. [Plotting Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/03_MATLAB_Plotting.md)
   4. [Scripts](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/04_MATLAB_Scripts.md)
   5. [Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/05_MATLAB_Loops.md)
   6. [Conditional Statements](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/06_MATLAB_Conditional_Statements.md)
   7. [Custom Functions](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/07_MATLAB_Custom_Functions.md)

## Decisions

One way to make choices in how code executes is to use the MATLAB [if,elseif,else](https://www.mathworks.com/help/matlab/ref/if.html) keywords. The general MATLAB syntax for these conditional statements is as follows:

```Matlab

if expression
   do something 1
elseif expression
   do something 2
else
   do something 3
end

```
Expressions generally use [relational operators](https://www.mathworks.com/help/matlab/relational-operators.html) and [logical operators](https://www.mathworks.com/help/matlab/ref/logicaloperatorsshortcircuit.html) to test a condition. Some examples of relational operators include `==` for equality and `>` for greater than. Logical operators allow you to test two conditions, including `||` for OR, and `&&` for AND.

In a conditional `if` statement, the only required keywords to use are `if` and `end`. You do not need to use the `elseif` nor `else` if your code choices do not require multiple decisions. Here is an example:

```Matlab

>> n = 'Alabama';
if length(n) > 5
    disp('n has more than 5 characters')
end 
n has more than 5 characters

```

In the above code, we use the `if` keyword, `length` function, and relational operator `>` to determine if variable `n` has more than 5 characters. If it does, we display `n has more than 5 characters`. If we provide an `n` with a length fewer than 5, the expression is false, and the code will not display anything:

```Matlab

>> n = 'Utah';
if length(n) > 5
    disp('n has more than 5 characters')
end

```

We can add `else` to our code to execute a statement when the first expression is false:

```Matlab

>> n = 'Alabama';
if length(n) > 5
    disp('n has more than 5 characters')
else
    disp('n has less than 5 characters')
end
n has more than 5 characters

>> n = 'Utah';
if length(n) > 5
    disp('n has more than 5 characters')
else
    disp('n has less than 5 characters')
end
n has less than 5 characters
```

We can then add an `elseif` keyword, for example, if we wanted to test the condition that `n` has exactly 5 characters:

```Matlab

>> n = 'Alabama';
if length(n) > 5
    disp('n has more than 5 characters')
elseif length(n) == 5
    disp('n has 5 characters')
else
    disp('n has less than 5 characters')
end
n has more than 5 characters

>> n = 'Utah';
if length(n) > 5
    disp('n has more than 5 characters')
elseif length(n) == 5
    disp('n has 5 characters')
else
    disp('n has less than 5 characters')
end
n has less than 5 characters

>> n = 'Maine';
if length(n) > 5
    disp('n has more than 5 characters')
elseif length(n) == 5
    disp('n has 5 characters')
else
    disp('n has less than 5 characters')
end
n has 5 characters

```

We can use multiple `elseif` keywords to add a test for an empty string:

```n = '';
if length(n) > 5
    disp('n has more than 5 characters')
elseif length(n) == 5
    disp('n has 5 characters')
elseif length(n) == 0
    disp('n has no characters')
else
    disp('n has less than 5 characters')
end
n has no characters
```

With conditional statements, once a condition is true, the code for that condition is executed and no further conditions are tested. So, be sure to experiment often and try a variety of test cases when coding. As an example, let's say we wrote the following code expecting to test for more than 5 characters and the character a:

```
>> n = 'Alabama';
if length(n) > 5
    disp('n has more than 5 characters')
elseif count(n,'a') > 0
    disp('n contains the character a')
else
    disp('n has less than 5 characters and does not contain a')
end
n has more than 5 characters

```

Since the first statement `length(n) > 5` was true, the code executed and stopped, even though the next statement `count(n,'a') > 0` is also true. One way we can test for two conditions at the same time would be to rewrite the code using a logical operator:

```Matlab

>> n = 'Alabama';
if length(n) > 5 && count(n,'a') > 0
    disp('n has more than 5 characters and contains the character a')
else
    disp('false')
end
n has more than 5 characters and contains the character a

>> n = 'Utah';
if length(n) > 5 && count(n,'a') > 0
    disp('n has more than 5 characters and contains the character a')
else
    disp('false')
end
false
```

We can also combine conditional statements with loops:

```Matlab

>> n = {'Alabama','Georgia','Maine','Utah'};
for j = 1:length(n)
    if length(n{j}) > 5
        disp('n has more than 5 characters')
    elseif length(n{j}) == 5
        disp('n has 5 characters')
    else
        disp('n has less than 5 characters')
    end
end
n has more than 5 characters
n has more than 5 characters
n has 5 characters
n has less than 5 characters
```

Let's return to our `myCIDdata` variable and create a new variable by indexing out the first column (the SMILES):

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

We can apply what we learned about conditional statements to find some patterns in the SMILES strings. For example, if we wanted to find out if each SMILES string contains either a '+' OR '-' character:

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

In the above code, we use a `for` loop to iterate over each cell value in `smi` and then test the condition that the string contains at least one `+` symbol or `-` symbol. If the pattern is found a new logical value `true` (1) is added to the [preallocated](https://www.mathworks.com/help/matlab/matlab_prog/preallocate-memory-for-a-cell-array.html) cell array, result1. If the pattern is not found (`else`) the value is `false` (0). Note that we chose to save the variables here instead of displaying 500+ results. The line `result1{j,1} tells MATLAB to save the result in the jth row (i.e., same row the SMILES being tested is on), and first column.

---

**Attribution**

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html)). In general, we reused parts of their lesson including the basic structure, some descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples. We have maintained the MIT license for program and code examples. Molecular dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.





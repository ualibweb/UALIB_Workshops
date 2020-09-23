# Conditional Statements

**Attribution**

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html)). In general, we reused parts of their lesson including the basic structure, some descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples. We have maintained the MIT license for program and code examples. Molecular dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

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

Let's return to our `myCIDdata` variable and create a new variable by indexing out the first 20 rows of the first column (Isomeric SMILES):

```Matlab

>> smi = myCIDdata{1:20,1}

smi =

  20×1 cell array

    {'CCN(CC(=O)C)C(C1=CC=CC=C1)C(=O)OC(C)(C)C'            }
    {'CCN(CC(=O)OCC)C(C1=CC=CC=C1)C(=O)OC'                 }
    {'C1=CC=C(C=C1)CN(CC2=CC=CC=C2)C(C3=CC=C(C=C3)F)C(=O)O'}
    {'CC.CCCN1CCN(CC1)C(C2=CC=CC=C2CC)C(=O)O'              }
    {'CC.CC.CCC.CC(=C)N1CCN(CC1)C(C2=CC=CC=C2)C(=O)O'      }
    {'CC.CC(C)N(C)C(CC1=CC=CC=C1)C(=O)O'                   }
    {'CN(C)C(C1=CC=CC=C1C(F)(F)F)C(=O)O.Cl'                }
    {'CC1CCC(=C)N1C(C2=CC=CC=C2)C(=O)O'                    }
    {'CCC(CCN(C)C(C1=CC=CC=C1)C(=O)O)O'                    }
    {'CC=C.CC1=C(C(=CC=C1)C(C(=O)O)N(C)C)C.C#C'            }
    {'CCCC1=C(C(=CC=C1)[C@H](C(=O)O)N2CCCCC2)F'            }
    {'CCN(C)CCN(C)C(C1=CC=CC=C1)C(=O)O'                    }
    {'CC(C)C1CC1C(C(=O)O)N(C)CC2=CC=CC=C2'                 }
    {'CCCC1=CC(=CC=C1)[C@H](C(=O)O)N2CCCCC2'               }
    {'CC(CC=C)(NC(C1=CC=CC=C1)C(=O)O)O'                    }
    {'CC(C)N(CCCCCCCCC(=O)O)CC1=CC=CC=C1'                  }
    {'CC1(CCN(CC1)[C@@H](C2=CC=CC=C2)C(=O)O)O'             }
    {'CCN[C@@H](C1=CC=CC=C1)C(=O)O.Cl'                     }
    {'CCCCCCC(C1=CC=CC=C1)(C(=O)O)N(C)C'                   }
    {'[2H]CC(C)(C)OC(=O)N(CC(=O)O)C(C1=CC=CC=C1)C(=O)O'    }


```

We can apply what we learned about conditional statements to find some patterns in the SMILES strings. For example, if we wanted to display information about SMILES that contain the characters '+' OR '-':


...
...









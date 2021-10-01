# Plotting Data

**Lesson Navigation**

   1. [Introduction, Overview of the MATLAB GUI, and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB_fall_2020/01_MATLAB_Introduction.md)
   2. [Variables and Arrays](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB_fall_2020/02_MATLAB_Variables_Arrays.md)
   3. [Plotting Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB_fall_2020/03_MATLAB_Plotting.md)
   4. [Scripts](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB_fall_2020/04_MATLAB_Scripts.md)
   5. [Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB_fall_2020/05_MATLAB_Loops.md)
   6. [Conditional Statements](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB_fall_2020/06_MATLAB_Conditional_Statements.md)
   7. [Custom Functions](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB_fall_2020/07_MATLAB_Custom_Functions.md)

## Review on Loading Data

We will be plotting data from the CID51840_similar.txt. If you have not already done so, import this data into MATLAB as follows:

```Matlab

>> cd('/home/myusername/Desktop/Mdata')

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

First, we will need to index out some data for plotting, namely the MolecularWeight and HeavyAtomCount columns:

```Matlab

>> mw = myCIDdata{:,4};
>> hac = myCIDdata{:,6};

```

Note that above, we used the `;` symbol to suppress the output in the command window. Next, let's plot the MolecularWeight variable (mw) as a histogram using the MATLAB `histogram` function.


```Matlab

>> h = histogram(mw)

h = 

  Histogram with properties:

             Data: [574×1 double]
           Values: [16 50 68 132 90 104 46 21 15 17 5 3 3 1 1 1 0 1]
          NumBins: 18
         BinEdges: [160 180 200 220 240 260 280 300 320 340 360 380 400 420 440 460 480 500 520]
         BinWidth: 20
        BinLimits: [160 520]
    Normalization: 'count'
        FaceColor: 'auto'
        EdgeColor: [0 0 0]

  Show all properties

```
![M_image01](/01_MATLAB/img/M_image01.jpg)


Our histogram has a variety of properties that we can adjust (above), so for example, if we wanted to change the color of the bars, we can use dot indexing into our histogram properties and set a new value:


```Matlab

>> h.FaceColor = 'red';

```

![M_image02](/01_MATLAB/img/M_image02.jpg)

As an alternative, we can also set properties in the initial histogram plotting step:

```Matlab

>> h = histogram(mw,'FaceColor','red')

```

It is always a good idea to add axes labels and a title:

```Matlab

>> xlabel('Molecular Weight')
>> ylabel('Frequency')
>> title('CID 51840 Similar Compounds')

```

![M_image03](/01_MATLAB/img/M_image03.jpg)


We can create an inset scatter plot of Molecular Weight vs. Heavy Atom Count as follows:

```Matlab

>> axes('Position',[.55 .55 .3 .3]);
>> scatter(hac,mw,'o','filled','black');
>> box on;
>> xticks(10:5:40);
>> xlabel('Heavy Atom Count');
>> ylabel('Molecular Weight');

```

![M_image04](/01_MATLAB/img/M_image04.jpg)


In the above code, we first use `axes` to create a set of new axes at position 0.55, 0.55 and a scale of 0.3 relative to the original figure. I used trial and error here on the values until it looked good to me. Next, `scatter` is used to plot Molecular Weight vs. Heavy Atom Count with filled black circles. `box on` adds a box around the entire inset plot. `xticks` adjusts the number of intervals. Lastly, we use `xlabel` and `ylabel` to add axes labels.

---

**Attribution**

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html)). In general, we reused parts of their lesson including the basic structure, some descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples. We have maintained the MIT license for program and code examples. Molecular dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.



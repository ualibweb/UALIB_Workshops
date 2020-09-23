# Loops

**Lesson Navigation**

   1. [Introduction, Overview of the MATLAB GUI, and Setup](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/01_MATLAB_Introduction.md)
   2. [Variables and Arrays](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/02_MATLAB_Variables_Arrays.md)
   3. [Plotting Data](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/03_MATLAB_Plotting.md)
   4. [Scripts](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/04_MATLAB_Scripts.md)
   5. [Loops](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/05_MATLAB_Loops.md)
   6. [Conditional Statements](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/06_MATLAB_Conditional_Statements.md)
   7. [Custom Functions](https://github.com/vfscalfani/UALIB_Workshops/blob/master/01_MATLAB/07_MATLAB_Custom_Functions.md)

## Repeating Tasks with a For Loop

It is often useful to repeat tasks. For example, let's create a variable named foods:

```Matlab

>> foods = ["eggs","toast","yogurt","blueberries"];

```

Perhaps we want to display the values in foods one by one after the phrase "I ate" and add a period at the end of the sentence. We can do this by indexing into the foods string array, concatenating this value with 'I ate' and '.', and then displaying the new text using the MATLAB `disp` function:

```Matlab
>> disp(['I ate ' foods{1} '.'])
I ate eggs.
>> disp(['I ate ' foods{2} '.'])
I ate toast.
>> disp(['I ate ' foods{3} '.'])
I ate yogurt.
>> disp(['I ate ' foods{4} '.'])
I ate blueberries.

```

After a couple of repeated command inputs, we can quickly see that this method is repetitive and inefficient. What if we had hundreds of food variables to display? We can accomplish the same task much faster using a loop. A general [for loop](https://www.mathworks.com/help/matlab/ref/for.html) in MATLAB is constructed as follows:

```Matlab

for variable = collection
   do something
end

```

Transferring this format to our task above produces:

```Matlab

>> foods = ["eggs","toast","yogurt","blueberries"];

for j = 1:4
   disp(['I ate ' foods{j} '.'])   
end
I ate eggs.
I ate toast.
I ate yogurt.
I ate blueberries.

```
In the above code, `j` is a variable, in this case, `j` starts at 1 in the first iteration and indexes out the value 'eggs', on the second iteration `j` become 2 and indexes out the value 'toast'.

Whenever possible, it is a good idea to make your code more general. For example, if we change the number of values in the foods variable, we would need to manually edit our loop with the correct index values. We can instead use the length function to make our code more robust and general:

```Matlab

>> length(foods)

ans =

     4

>> foods = ["eggs","toast","yogurt","blueberries"];

for j = 1:length(foods)
   disp(['I ate ' foods{j} '.'])   
end
I ate eggs.
I ate toast.
I ate yogurt.
I ate blueberries.

```

Let's return to the CID51840_similar.txt dataset and our script hist_plotCompounds.m. 

```Matlab

% hist_plotCompounds
% creates a histogram plot of compound molecular weights and places a 
% scatter plot inset of molecular weight vs. heavy atom count

% load data
cd('/home/myusername/Desktop/Mdata')
myCIDdata = readtable('CID51840_similar.txt','Format','%s %s %s %f %d %d %d');
mw = myCIDdata{:,4};
hac = myCIDdata{:,6};

% plot histogram of molecular weight
h = histogram(mw);
h.FaceColor = 'red';
xlabel('Molecular Weight')
ylabel('Frequency')
title('CID 51840 Similar Compounds')

% create an inset scatter plot of molecular weight vs. heavy atom count
axes('Position',[.55 .55 .3 .3]);
scatter(hac,mw,'o','filled','black');
box on;
xticks(10:5:40);
xlabel('Heavy Atom Count');
ylabel('Molecular Weight');

```

As a reminder, the hist_plotCompounds.m script loads the CID51840_similar.txt dataset and creates a histogram plot of the molecular weight values with a scatter plot inset figure of molecular weight vs. heavy atom count.

What if we wanted to create the same histogram, but with different inset scatter plots, namely molecular weight vs. rotatable bond count (column 5) and molecular weight vs. atom chiral count (column 7)? We could repeat the commands for each plot by changing the variables and labels, but we would end up producing a lot of repetitive code and are likely to make a mistake. Instead, we can modify our script with a for-loop to create the 3 plots.

In the below modified code, we first create a cell array of data for the scatter plot inset called `inset_data`, which contains the values of rotatable bond counts (rbc), heavy atom counts (hac), and atom chiral counts (acc). We also create a cell array for the x-axis labels, `inset_xlabels`. Similarly to the text display example above, we use a `j` variable to specify the index value. Then, in the for loop, we specify the variable to use within the scatter plot as `inset_data{j}` and the xlabel as `inset_xlabels{j}`. As a result, on the first iteration, `j` is equal to 1 and `inset_data{1}` becomes the rbc column values, and `inset_xlabels{1}` is the 'Rotatable Bond Count' label. On the next iteration, `j` is equal to 2 and uses the hac values and 'Heavy Atom Count' label. This process is repeated for all values of `j`, in our case, `j` equals 1 though `length(inset_data)` (i.e., 3).

```Matlab

% hist_plotCompounds
% creates histogram plots of compound molecular weights and places a 
% scatter plot inset of molecular weight vs. selected data

% load data
cd('/home/myusername/Desktop/Mdata')
myCIDdata = readtable('CID51840_similar.txt','Format','%s %s %s %f %d %d %d');
mw = myCIDdata{:,4};
rbc = myCIDdata{:,5};
hac = myCIDdata{:,6};
acc = myCIDdata{:,7};

% setup figure inset data and x labels in cell arrays
inset_data = {rbc,hac,acc};
inset_xlabels = {'Rotatable Bond Count', 'Heavy Atom Count', 'Atom Chiral Count'};


for j = 1:length(inset_data)
    figure(j) % creates a new figure on each iteration
    % plot histogram of molecular weight
    h = histogram(mw);
    h.FaceColor = 'cyan';
    xlabel('Molecular Weight')
    ylabel('Frequency')
    title('CID 51840 Similar Compounds')

    % create an inset scatter plot
    axes('Position',[.55 .55 .3 .3]);
    scatter(inset_data{j}, mw,'o','filled','black');
    box on;
    xlabel(inset_xlabels{j});
    ylabel('Molecular Weight');
end

```
Running the revised hist_plotCompounds.m script produces the following plots:

![M_image05](/01_MATLAB/img/M_image05.jpg)

![M_image06](/01_MATLAB/img/M_image06.jpg)

![M_image07](/01_MATLAB/img/M_image07.jpg)


## Repeating Tasks with a While Loop

MATLAB [While loops](https://www.mathworks.com/help/matlab/ref/while.html) execute code in a loop if the expression is true. The general form of a MATLAB while loop is as follows:

```Matlab

while expression
   do something
end

```

The while loop evaluates the expression and continues only if the expression is true. 

> Note it is pretty easy to accidentally get stuck in an infinite loop when experimenting with while loops. You can stop execution by pressing Ctrl+C in the MATLAB command window.

If we take our example of displaying "I ate"...foods from earlier, we can write a while loop and get the same result as the previous for loop:

```Matlab

>> foods = ["eggs","toast","yogurt","blueberries"];
j = 1;
while j <= length(foods)
  disp(['I ate ' foods{j} '.']);
  j = j + 1;
end
I ate eggs.
I ate toast.
I ate yogurt.
I ate blueberries.

```

In the above code, our expression uses a [relational operator](https://www.mathworks.com/help/matlab/relational-operators.html), `<=` (less than or equal to) in order to create an expression that says only evaluate the commands if `j` is less than or equal to the length of the foods variable (length is 4). Typically, while loops are used for cases when you don't necessarily know the number of iterations to be performed. 

For example, in our `myCIDdata` variable, there is a molecular formula column. Let's say we wanted to display values of the molecular formula column starting at index position 1 and repeating until we matched a phosphorous atom, P. We can modify the above code by adding a [logical operator](https://www.mathworks.com/help/matlab/ref/logicaloperatorsshortcircuit.html) (AND, `&&`) and use the MATLAB function `contains` to check for presence of the character 'P'. The below code, then, displays molecular formulas if `j` is less than or equal to the length of the MF variable (which is 574) AND the molecular formula string does not contain the character 'P'. Once the condition is false (e.g., a P character is found) the loop stops.

```Matlab

>> MF = myCIDdata{:,3};
j = 1;
while j <= length(MF) && not(contains(MF{j},'P'))
  disp(MF{j});
  j = j + 1;
end
C17H25NO3
C15H21NO4
C22H20FNO2
C19H32N2O2
C22H40N2O2
C15H25NO2
C11H13ClF3NO2
C14H17NO2
C14H21NO3
C17H25NO2
C16H22FNO2
C14H22N2O2
C16H23NO2
C16H23NO2
C13H17NO3
C19H31NO2
C14H19NO3
C10H14ClNO2
C16H25NO2
C15H19NO6
C17H27NO2
C16H27NO2
C27H47NO2
C13H21NO2
C15H21NO2
C14H23NO3
C12H17NO3
C12H18N2O2
C12H18N2O2
C18H19NO2
C14H21NO3
C17H30N4O2
C20H29NO4
C18H27NO3
C13H18ClNO2
C10H12NNaO2
C10H9NO4
C10H13NO2
C16H26ClNO2
C14H19NO4
C16H20N2O10
C16H26ClNO2
C11H15NO2
C10H9NO6

```
Note that the next molecular formula in the dataset is 'C13H20NO2P'.

We will discuss expressions and operators more in the next topic on Conditional Statements.

---

**Attribution**

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license for Instructional Materials](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html) and [MIT License for programs and code examples](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html)). In general, we reused parts of their lesson including the basic structure, some descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples. We have maintained the MIT license for program and code examples. Molecular dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.



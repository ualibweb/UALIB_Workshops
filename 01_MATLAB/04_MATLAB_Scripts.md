# Scripts

> Content in this workshop have been adapted and derive from the Software Carpentry [Programming with MATLAB lesson](https://software-carpentry.org/lessons/) ([CC BY 4.0 license](http://swcarpentry.github.io/matlab-novice-inflammation/LICENSE.html). In general, we reused parts of their lesson including the basic structure, descriptions, and logical ordering, but included our own specific variables, scripts, loops, and custom function examples. Molecular dataset examples were retrieved from NCBI via their EDirect utility and is credited to NCBI and NLM. Please see the [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) for more information regarding the data.

## Executing Code in a Sequence

In the previous section on Plotting, we saw that it often requires several lines of code in a typical data/analysis workflow. This can be time consuming to retype every time or when making adjustments to your code. We can use MATLAB scripts to save commands in a file that executes each line of code sequentially and allows for easier editing. We start by creating a new script file with a descriptive name and `.m` extension. Note that this will save the script in your current working directory:

```Matlab

>> edit hist_plotCompounds.m

```

Now we can add comments with `%` and commands as desired in the Editor:

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

To run the script, type the name of the script in the MATLAB Command Window:

```Matlab

>> hist_plotCompounds

```

![M_image04](/01_MATLAB/img/M_image04.jpg)

To get help with the script, use the `help` function:

```Matlab

>> help hist_plotCompounds
  hist_plotCompounds
  creates a histogram plot of compound molecular weights and places a 
  scatter plot inset of molecular weight vs. heavy atom count

```



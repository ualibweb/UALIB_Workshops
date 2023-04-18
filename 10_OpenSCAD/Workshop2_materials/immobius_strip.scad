
// Written by Krishav Kassaju
// MIT License, see: https://github.com/ualibweb/UALIB_Workshops/blob/master/LICENSE

function f1(a,d)= (50+(d*(cos(a/2))))*cos(a);// function of x
function f2(b,e) = (50+(e*cos(b/2)))*sin(b); //function of y
function f3(c,f) = f*sin(c/2); //function of z

function combine(x,y) = [f1(x,y),f2(x,y),f3(x,y)];// calls all function, and returns the values of x y and z

for (i = [0:.25:360]){
    for (j = [-4:0.25:4]){
        translate(combine(i,j))
        sphere(.25);
    }
};
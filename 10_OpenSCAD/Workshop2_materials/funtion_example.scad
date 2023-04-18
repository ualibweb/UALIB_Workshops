
// Written by Krishav Kassaju
// MIT License, see: https://github.com/ualibweb/UALIB_Workshops/blob/master/LICENSE

function f1(a)= 20*sin(2*a)*cos(a);//function for y
function f2(b) = 20*cos(2*b)+20;//function of x

function combine(x) = [tan(x),f1(x),f2(x)];//returns a 3 point which relate to function of x y and z

for (i = [-89:.1:89]){//variying the value of x in known bound(can't have tan (90) as it is infinity)
    translate(combine(i))//calling the function for varying point to ploy in
    sphere(2);//
};
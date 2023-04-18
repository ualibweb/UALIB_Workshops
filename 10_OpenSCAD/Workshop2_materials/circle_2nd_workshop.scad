// Written by Krishav Kassaju
// MIT License, see: https://github.com/ualibweb/UALIB_Workshops/blob/master/LICENSE

for (i = [-4:.05:4]){
    for (j=[-4:.05:4]){
        r = sqrt((i*i)+(j*j));
        if ((round(r)==3)){
            translate([i,j,0])
            cube(.05);
        };
    };
};
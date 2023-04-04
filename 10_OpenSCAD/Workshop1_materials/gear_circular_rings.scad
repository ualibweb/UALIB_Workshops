

// Written by Krishav Kassaju
// MIT License, see: https://github.com/ualibweb/UALIB_Workshops/blob/master/LICENSE


//eample
/*
module 3d_circle(radius, extrusion, n){
    linear_extrude(extrusion)//extrudes the circle below
    circle(r = radius, $fn = n);//2D circle of r radius and number of elements
};
*/

module gear(r,n){//takes radius and no of teeth
    scr=r;
    bcr=((scr*2)*n*2)/(2*PI);//calculates the radius of the gear(bigger circle) from given information
    linear_extrude(2){//extrusion of the 2D shape that we create or thickness of the gear
        step = 360/n;
        difference(){
            circle(r = bcr,$fn=1000);//circle for gear
            circle(r = 3,$fn = 1000);//removes a circle for the center hole
            r=bcr;
            for (i=[0:step:360]) {//a for loop which gives us angles at which circles are cut
                angle = i;
                rotate([0,0,angle])//rotating the small circle around the big
                {translate([0,bcr,0])//translating this smaller circle to the outer radius
                    circle(r=scr,$fn=1000);}//create n amount of circles
                
                   
            };
        };
        //add circle on the other end
        //same steps as removing but this will be adding
        r=(bcr);
        for (i=[(step/2):step:360+(step/2)]) {//this is done because we need the angle for bigger circle a little more
            angle = i;
            rotate([0,0,angle])
                {translate([0,(bcr),0])
                    circle(r=scr,$fn=1000);}
    };
};
};
//Calling the module
gear(1, 20);
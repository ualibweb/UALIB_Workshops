
// Written by Krishav Kassaju
// MIT License, see: https://github.com/ualibweb/UALIB_Workshops/blob/master/LICENSE

rotate_extrude(angle=360,convexity=10,$fn=1000){//rotates and extrudes our 2D shape
rotate([0,0,90]){//this fixes our model for rotate_extrude
difference(){
        square([2,10]);//We start here with a square
    translate([1/2,8,0])//translate the smaller 
    square([1,2.1]);//Cut for groove inside for the rope
    
    //now creating the smooth curve(or fillet)
    //Remove for the fillet top left
    translate([.301,9.801,0])
    difference(){
        square([.2,.2]);//a square
        circle(.2,$fn=1000);//cute a circle in square
    };
     //fillet top right
     mirror([1,0,0])//mirror it on x plane
     translate([-1.699,9.8001,0])
     difference(){
        square([.2,.2]);
        circle(.2,$fn=1000);
        };
    };
//fillet left inside
translate([.5,8,0])
        difference(){
            square([.2,.2]);
            translate([.2,.2,0])
            circle(.2,$fn=1000);
            };
//fillet right inside
translate([2,0,0])//fixing placement
mirror([1,0,0]){
    translate([.5,8,0])
        difference(){
            square([.2,.2]);
            translate([.2,.2,0])
            circle(.2,$fn=1000);
            };
        };
    };
};

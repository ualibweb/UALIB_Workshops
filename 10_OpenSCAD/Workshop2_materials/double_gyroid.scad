
// Written by Krishav Kassaju
// MIT License, see: https://github.com/ualibweb/UALIB_Workshops/blob/master/LICENSE


res = 0.025;

scale([100,100,100]){// to make it easier to look at
for (x =[0:res:2]){//varying value of x
    for (y=[0:res:2]){//varying value of y
        for (z=[0:res:2]){//varying value of z
            t = (sin(2*180*x)*cos(2*180*y))+(sin(2*180*y)*cos(2*180*z))+(sin(2*180*z)*cos(2*180*x));//calculationg the value of t
            if ((t>1.1)){//setting parameter on which our funtion is true
                translate([x,y,z])
                cube(res,center=true)
                ;}
            if ((t<-1.1)){
                translate([x,y,z])
                cube(res,center=true);
            }
        }
    }
}
};
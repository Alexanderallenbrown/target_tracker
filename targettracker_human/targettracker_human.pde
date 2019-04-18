

MS2007 targ = new MS2007(5.4,5.4,3,-95,2.7,5.4,2,-25,2*3.1415/4.5,0,0,0);
float pathrot = 0;
float dt;
int tnow, oldt;
int targetscale = 25;
int tradius = 25;
float targactx,targacty;


void setup(){
  size(500,500);
  
}

void draw(){
  background(0);
  tnow = (millis());
  dt = (tnow-oldt)/1000.0;
  oldt = tnow;
  
  //update the target
  targ.update(dt);
  targactx = targ.x*targetscale+width/2;
  targacty = targ.y*targetscale+height/2;
  
  //draw the target
  fill(255);
  ellipse(targactx,targacty,tradius,tradius);
  
  
}

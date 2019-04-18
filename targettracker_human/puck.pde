class Puck{
  boolean oldPrs,Uprs,held,oldheld;
  float x,y,radius,ox,oy;
  Puck(float ix,float iy,float iradius){
   radius = iradius;
   x = ix;
   y = iy;
   ox = ix;
   oy = iy;
   Uprs = false;
   held = false;
   oldPrs = false;
   oldheld = false;
  }
  void update(){
   //determine whether there has been a unique press.
   Uprs =  mousePressed&&!oldPrs;
   oldPrs = mousePressed;
   //determine whether the press occurred while the mouse was over the puck
   held = (Uprs&&(sqrt(pow(mouseX-x,2)+pow(mouseY-y,2))<radius))||(mousePressed&&oldheld);
   oldheld=held;
   if(held){
     x=mouseX;
     y=mouseY;
   }
   
  }
  void reset(){
    held = false;
    x = ox;
    y = oy;
  }
  
}
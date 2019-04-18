class MS2007{
  // defaults 5.4,5.4,3,-95,2.7,5.4,2,-25,2*3.1415/4.5,0,0,0
  float A1x,A2x,hx,phx,A1y,A2y,hy,phy,w,ox,oy,rot;
  float x,y,t;
  MS2007(float iA1x, float iA2x, float ihx, float iphx, float iA1y, float iA2y, float ihy, float iphy, float iw, float iox, float ioy, float irot){
    A1x = iA1x;
    A2x = iA2x;
    hx = ihx;
    phx = iphx;
    A1y = iA1y;
    A2y = iA2y;
    hy = ihy;
    phy = iphy;
    w = iw;
    ox = iox;
    oy = ioy;
    rot = irot;
}
void update(float dt){
  t+=dt;
  x=A1x*cos(hx*w*t)+A2x*cos(hx* w* t- phx)+ ox;
  y= A1y*cos( hy* w* t)+ A2y*cos( hy* w* t- phy)+ oy;
}

void reset(){
  t = 0;
  x=A1x*cos(hx*w*t)+A2x*cos(hx* w* t- phx)+ ox;
  y= A1y*cos( hy* w* t)+ A2y*cos( hy* w* t- phy)+ oy;

}
}

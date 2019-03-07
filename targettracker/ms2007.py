class MS2007(object):
    def __init__(self,A1x=5.4,A2x=5.4,hx=3,phx=-95,A1y=2.7,A2y=5.4,hy=2,phy=-25,w=2*3.1415/4.5,ox=0,oy=0):
        self.A1x,self.A2x,self.hx,self.phx,self.A1y,self.A2y,self.hy,self.phy,self.w,self.ox,self.oy=A1x,A2x,hx,phx,A1y,A2y,hy,phy,w,ox,oy
        self.x = 0
        self.y = 0
        self.t = 0
        self.update(0.0);
    def update(self,dt):
        self.t+=dt
        self.x=self.A1x*cos(self.hx*self.w*self.t)+self.A2x*cos(self.hx*self.w*self.t-self.phx)+self.ox
        self.y=self.A1y*cos(self.hy*self.w*self.t)+self.A2y*cos(self.hy*self.w*self.t-self.phy)+self.oy

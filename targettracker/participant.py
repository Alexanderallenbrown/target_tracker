def mewise(l1,l2):
    assert len(l1)==len(l2)
    out = []
    for k in range(0,len(l1)):
        out.append(l1[k]*l2[k])
    return out
def aewise(l1,l2):
    assert len(l1)==len(l2)
    out = []
    for k in range(0,len(l1)):
        out.append(l1[k]+l2[k])
    return out
def mconst(const,l):
    out = []
    for k in range(0,len(l)):
        out.append(l[k]*const)
    return out

def dotprod(v1,v2):
    return v1[0]*v2[0]+v1[1]+v2[1]

def vmag(v):
    return (v[0]**2+v[1]**2)**0.5

class Participant(object):
    def __init__(self,x0=0.,y0=0.,w=10.,predT=0.2,predmethod='CV',capthresh=0.01,reactiontime=0.2,ttcthresh=0.5,capturethresh=1.0):
        self.x,self.y=x0,y0
        self.xdot,self.ydot = 0.,0.
        self.reactiontime=reactiontime
        self.lastdecisiontime=0.
        self.w,self.predT,self.capthresh=w,predT,capthresh
        self.captured=False
        self.ttcthresh = ttcthresh
        self.capturethresh = capturethresh
        
        self.tx,self.ty=0.,0.
        self.txd,self.tyd=0.,0.
        self.otx,self.oty=0.,0.
        self.predX,self.predY=0.,0.
        self.mypredX,self.mypredY = 0.,0.#these are for the "hand."
        
        #how long has it been since we made a prediction
        self.lastpredtime = 0
        #what is the simulation time?
        self.t = 0
        
        self.ddot = 0
        self.d = 0
        self.oldd = 0
        
        self.go = False
        self.ttc = -1000
    
    def measureTarget(self,target,dt):
        """ measures the target properties needed for prediction"""
        self.tx,self.ty=target.x,target.y
        self.txd=(self.tx-self.otx)/dt
        self.tyd=(self.ty-self.oty)/dt
        self.otx,self.oty=self.tx,self.ty
        #now determine the distance and derivative of distance between hand and target
        self.d = ((self.x-self.tx)**2+(self.y-self.ty)**2)**0.5
        self.ddot = (self.d-self.oldd)/dt
        self.oldd = self.d
        
    
    def predictTarget(self):
        """predicts future location of the target based on some model of target motion... start with constant velocity"""
        self.predX = self.tx+self.txd*self.predT
        self.predY = self.ty+self.tyd*self.predT
        self.lastpredtime = self.t
    
    
    def calcTTC(self):
        if (abs(self.ddot)>0.001):
            self.ttc = -(self.d/self.ddot)
        else:
            self.ttc = -10000
    
    def state_eq(self,stx,predX,predY):
        """ state space equations for the 'arm.' right now, directions are two identical but independent second-order systems (crit damping).
        The state vector is [x,xdot,y,ydot]^T """
        xdot = stx[1]
        xddot = -2*self.w*stx[1]+self.w**2*(predX-stx[0])
        ydot = stx[3]
        yddot = -2*self.w*stx[3]+self.w**2*(predY-stx[2])
        return [xdot,xddot,ydot,yddot]
    
    def rk_update(self,dt):
        #this should have taken case of all contingencies and got us the correct inputs for the car.
        stx = [self.x,self.xdot,self.y,self.ydot]
        k1x = self.state_eq(stx,self.predX,self.predY) # Calvulate k1
        xhat1 = aewise(stx,mconst(dt/2,k1x)) # Find x_hat1
        k2x = self.state_eq(xhat1,self.predX,self.predY) # Calcaulte k2 using x_hat1
        xhat2 = aewise(stx,mconst(dt/2,k2x)) # Find x_hat2
        k3x = self.state_eq(xhat2,self.predX,self.predY) # Calcaulte k3 using x_hat2
        xhat3 = aewise(stx,mconst(dt,k3x)) # Find x_hat3
        k4x = self.state_eq(xhat3,self.predX,self.predY) # Calcaulte k4 using x_hat3
        # Calculate xdot
        xdot = mconst(1/6.,aewise(k1x,aewise(mconst(2,k2x),aewise(mconst(2,k3x),k4x))))     #(k1x+2*k2x+2*k3x+k4x)/6 # Find xdot by averaging k1 and k2
        x = aewise(stx,mconst(dt,xdot))
        #print(x)
        self.x,self.xdot,self.y,self.ydot=x
    
    def update(self,target,dt):
        
        self.measureTarget(target,dt)
        #if enough time has passed, make another prediction
        
        # if(self.ttc<self.ttcthresh):
        #     print("gon' get him: "+str(self.ttc))
        if(not self.go):
            self.predictTarget()
        if(self.go):
            self.t+=dt
            self.calcTTC()
            if(((self.t-self.lastpredtime)>=self.reactiontime) and ((self.ttc>self.ttcthresh) or (self.ttc<0))):
                #print("predicting new target pos at time lag of: "+str(self.t-self.lastpredtime))
                self.predictTarget()
            self.rk_update(dt)
        if(self.d<self.capturethresh):
            self.captured = True

        
    
    

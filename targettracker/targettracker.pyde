from ms2007 import MS2007
from participant import Participant
from slider import Slider

targetscale = 25
ox = 300
oy = 300
tradius = 25
oldt = millis()-15
tnow = millis()
offsettime = 0

partdelay = 1000


def setup():
    size(800,800)
    global mstarget,part,predslider,omslider,lagslider,itimeslider,partdelay
    mstarget = MS2007()
    part = Participant()
    predslider = Slider(50,50,100,0,0.5,0.25,'Prediction Horizon')
    omslider = Slider(250,50,100,1.0*2*3.14,4*2*3.14,2*2*3.14,'Controller Stiffness')
    lagslider = Slider(450,50,100,0,0.5,0.1,'prediction delay')
    partdelay=1000
    
def draw():
    global oldt,tnow,targetscale,omslider,lagslider,offsettime,part,mstarget
    #timing
    tnow = millis()-offsettime
    dt = (tnow-oldt)/1000.0
    oldt = tnow
    #actually update dynamics
    part.predT = predslider.slpos
    part.w = omslider.slpos
    part.reactiontime = lagslider.slpos
    
    #if we haven't caught the target yet, update it.
    if(part.captured==False):
        mstarget.update(dt)
        if(tnow>partdelay):
            part.go=True
            part.update(mstarget,dt)
    else:
        mstarget = MS2007()
        part = Participant()
        offsettime = tnow
        oldt = tnow-dt*1000#to avoid first timestep being zero in next iteration
        part.captured=False
        
    print(tnow)
    
    #drawing functions
    background(0)
    noStroke()
    fill(255)
    translate(width/2,height/2)
    ellipse(mstarget.x*targetscale,mstarget.y*targetscale,tradius,tradius)
    noFill()
    stroke(color(0,255,0))
    ellipse(part.x*targetscale,part.y*targetscale,tradius/2,tradius/2)
    stroke(color(255,0,0))
    ellipse(part.predX*targetscale,part.predY*targetscale,tradius/3,tradius/3)
    
    translate(-width/2,-height/2)
    #update GUI
    predslider.drawSlider()
    omslider.drawSlider()
    lagslider.drawSlider()
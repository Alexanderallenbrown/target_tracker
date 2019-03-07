from ms2007 import MS2007
from participant import Participant
from slider import Slider
from radiobutton import RadioButton

targetscale = 25
ox = 300
oy = 300
tradius = 25
oldt = millis()-15
tnow = millis()
offsettime = 0

simt = 0

partdelay = 1000
partoffset = 13.

def setup():
    size(800,800)
    global simt,mstarget,part,predslider,omslider,lagslider,itimeslider,partdelay,partoffset,gobutton
    mstarget = MS2007()
    gobutton = RadioButton(100,100,25,"Play/Pause")
    part = Participant(x0=-partoffset,y0=partoffset)
    predslider = Slider(50,50,100,0,0.5,0.25,'Prediction Horizon')
    omslider = Slider(250,50,100,1.0*2*3.14,4*2*3.14,2*2*3.14,'Controller Stiffness')
    lagslider = Slider(450,50,100,0,0.5,0.1,'prediction delay')
    itimeslider = Slider(650,50,100,0,4500,1000,'Initiation Time (ms)')
    partdelay=1000

    
def draw():
    global simt,gobutton,partoffset,oldt,tnow,targetscale,omslider,lagslider,offsettime,part,mstarget,itimeslider
    #timing
    tnow = (millis())
    dt = (tnow-oldt)/1000.0
    oldt = tnow
    if(gobutton.state):
        simt+=dt*1000
    #actually update dynamics
    part.predT = predslider.slpos
    part.w = omslider.slpos
    part.reactiontime = lagslider.slpos
    partdelay = itimeslider.slpos
    
    if gobutton.state:
        # print tnow, offsettime
        #if we haven't caught the target yet, update it.
        if(part.captured==False):
            mstarget.update(dt)
            if(simt>partdelay):
                part.go=True
            else:
                pass
                # print("waiting")
        else:
            # print "resetting"
            mstarget = MS2007()
            part = Participant(x0=-partoffset,y0=partoffset)
            offsettime = oldt
            simt=0
            gobutton.state= not gobutton.state
    
            
        part.update(mstarget,dt)
        #print(tnow)
    
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
    if part.go:
        ellipse(part.predX*targetscale,part.predY*targetscale,tradius/3,tradius/3)
    
    translate(-width/2,-height/2)
    #update GUI
    gobutton.updateRadio()
    predslider.drawSlider()
    omslider.drawSlider()
    lagslider.drawSlider()
    itimeslider.drawSlider()

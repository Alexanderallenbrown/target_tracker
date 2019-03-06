from ms2007 import MS2007

targetscale = 25
ox = 300
oy = 300
tradius = 10
oldt = millis()-15
tnow = millis()

def setup():
    size(600,600)
    global mstarget
    mstarget = MS2007()
    
def draw():
    global oldt,tnow,targetscale
    tnow = millis()
    dt = (tnow-oldt)/1000.0
    oldt = tnow
    mstarget.update(dt)
    background(0)
    fill(255)
    translate(width/2,height/2)
    ellipse(mstarget.x*targetscale,mstarget.y*targetscale,tradius,tradius)
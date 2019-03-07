class RadioButton:
    def __init__(self,ix, iy, id, ilabel):
        self.x = ix;
        self.y = iy;
        self.d = id;
        self.state = False;
        self.touched = False;
        self.wastouched = False;
        self.newtouch = False;
        self.label = ilabel;
        
    def updateRadio(self):
        #detect whether the radio button is pressed 
        if (mousePressed == True):
            if ((((mouseX - self.x)**2 + (mouseY - self.y)**2)**.5) <= self.d / 2.0):
                self.touched = True;
        else:
            self.touched = False;
    
        if (self.touched == True and self.wastouched == False):
            self.state = not self.state;
        
        #update value of touched
        self.wastouched = self.touched;
    
        #draw the button
        self.drawRadio();


    def drawRadio(self):
        if (self.state == False):
            fill(0);
        else:
            fill(255);
        
        stroke(255);
        #draw the radio button
        ellipse(self.x, self.y, self.d, self.d);
        fill(255);
        stroke(255);
        textSize(12);
        text(self.label, self.x + self.d, self.y);

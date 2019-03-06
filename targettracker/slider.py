class Slider:
    def __init__(self,ixorg, iyorg, ilen, imin, imax, islpos, ilabel):
        self.xorg = ixorg;
        self.yorg = iyorg;
        self.len = ilen;
        self.slpos = islpos;
        self.min = imin;
        self.max = imax;
        self.label = ilabel;
        self.sliderstroke = color(255, 255, 255);
        self.sliderfill = color(255, 255, 255);
        self.was_pressed = False;
        self.held = False;

    def drawSlider(self):
        self.updateSlider();
        stroke(self.sliderstroke);
        fill(self.sliderfill);
        line(self.xorg, self.yorg, self.xorg + self.len, self.yorg);
        rectMode(CENTER);
        self.box_x = (self.slpos - self.min) * self.len / (self.max - self.min);
        rect(self.xorg + self.box_x, self.yorg, self.len * .2, self.len * .1);
        textSize(12);
        text(self.label + ": " + nf(self.slpos, 1, 2), self.xorg, self.yorg - self.len * .1);

    def updateSlider(self):
        self.box_x = (self.slpos - self.min) * self.len / (self.max - self.min);
        if ((mousePressed and not(self.was_pressed) and not(self.held))):
            if (abs(self.xorg + self.box_x - mouseX) < (0.2 * self.len) and abs(self.yorg - mouseY) < (0.2 * self.len)):
                self.held = True;
        elif (mousePressed and self.held):
            self.held=True
        else:
            self.held = False;
        #print(self.held)
        self.was_pressed = mousePressed;
        if (self.held == True):
            self.box_x = mouseX - self.xorg;
            if (mouseX > self.xorg + self.len):
                self.box_x = self.len;
            if (mouseX < self.xorg):
                self.box_x = 0;
            self.slpos = self.min + (self.max - self.min) * float(self.box_x )/ self.len
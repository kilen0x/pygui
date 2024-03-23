
import pygame as pg


class Selector:
    def __init__(self, x, y, width, height, font, color, text = "", view = None, textColor = (255,255,255)):
        o = len(text) // 15 + 1
        if o != 0:
            height *= o
        self.rect = pg.Rect(x,y,width,height)
        self.view = view
        self.color = color
        self.truecolor = color
        self.font = font
        self.textcolor = textColor
        
        ## text ##
        self.textpos = (self.rect.x+10, self.rect.y +5)
        p = 0
        orig = [""]
        f = 0
        for i in text:
            if p % 16 == 0 and p != 0:
                orig.append("")
                f += 1
                orig[f] += i
            else:
                orig[f] += i
            p += 1
        self.text = orig

class Gui:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, displayName = "main gui", font = None):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(displayName)

        pg.init()
        pg.font.init()

        self.sW = SCREEN_WIDTH
        self.sH = SCREEN_HEIGHT
        self.selectorY = 0
        self.onSelectors = False
        self.fS = 30
        self.selectors = []
        self.selectorspages = []

        ## DISPLAY DESIGN ##

        self.font = pg.font.Font(font, self.fS)
        self.frame_1 = pg.Rect(0, 0, SCREEN_WIDTH//5.13, SCREEN_HEIGHT)
        self.frame_2 = pg.Rect(300, 0, SCREEN_WIDTH-SCREEN_WIDTH//5.13, SCREEN_HEIGHT)

        self.splitline = pg.Rect(SCREEN_WIDTH//5.40, 0, SCREEN_WIDTH//102, SCREEN_HEIGHT)

        ## COLORS ##

        self.frame_1_color = (36,36,36)
        self.frame_2_color = (71,71,71)
        self.splitline_color = (20,20,20)
        self.selector_color = (80,80,80)

    def update(self):
        print(self.selectorY)
        mouse = pg.mouse
        for selector in self.selectors:
            if selector.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]):
                selector.color = (20,20,20)

            else:
                selector.color = selector.truecolor
        
        if self.frame_1.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]):
            self.onSelectors = True
        else:
            self.onSelectors = False

    def draw(self):

        self.screen.fill(self.frame_2_color)
        
        pg.draw.rect(self.screen, self.frame_1_color, self.frame_1)
        pg.draw.rect(self.screen, self.frame_2_color, self.frame_2)
        pg.draw.rect(self.screen, self.splitline_color, self.splitline)

        for selector in self.selectors:
            pg.draw.rect(self.screen, selector.color, selector.rect, border_radius=20)
            pg.draw.rect(self.screen, (0,0,0), selector.rect, width = 2, border_radius=20)
            y = 0
            for i in selector.text:
                text = selector.font.render(i, True, selector.textcolor)
                p = [selector.textpos[0], selector.textpos[1]]
                p[1] += y
                self.screen.blit(text, p)
                y += 30 # gap


        pg.display.flip()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEWHEEL:
                if self.onSelectors:

                    evy = event.y 

                    if evy == 1: self.selectorY -= 1
                    elif evy == -1: self.selectorY += 1
                    
                    if event.y == 1 and self.selectorY < 0:
                        self.selectorY += 1
                        return
            
                    if event.y == -1 and self.selectorY == len(self.selectors):
                        self.selectorY -= 1
                        return
        

                    for selector in self.selectors:
                        if evy == 1:
                            selector.rect.y += 150
                            a = [selector.textpos[0], selector.textpos[1] + 150]
                            selector.textpos = a
                        else:
                            selector.rect.y -= 150
                            a = [selector.textpos[0], selector.textpos[1] - 150]
                            selector.textpos = a
    def main_loop(self):
        while True:
            self.update()
            self.draw()
            self.event()


    def add_selector(self, selectorText):
        y = 30 + len(self.selectors) * 150
        print(y)
        selector = Selector(30, y, 200, 30, self.font, self.selector_color, selectorText, str(len(self.selectors)))

        self.selectors.append(selector)



import pygame as pg
import os


class ViewModeExcept(Exception):
    def __init__(self):
        pass

class IconExcept(Exception):
    def __init__(self):
        pass

class Selector:
<<<<<<< HEAD
    def __init__(self,screenW, x, y, width, height, font, color, text = "", view = None, textColor = (255,255,255)):
        f = screenW // 102
        o = len(text) // f + 1
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
        p = 1
        orig = [""]
        r = 0
        for i in text:
            if p % f == 0:
                orig.append("")
                r += 1
                orig[r] += i
            else:
                orig[r] += i
            p += 1
            self.text = orig

class Button:
    def __init__(self,screenW, x, y, width, height, font, color, fun, text = "", view = None, textColor = (255,255,255)):
        t = screenW // 17.3
        o = len(text) // t + 1
        if o != 0:
            height *= o
        self.rect = pg.Rect(x,y,width,height)
        self.view = view
        self.color = color
        self.truecolor = color
        self.font = font
        self.textcolor = textColor
        self.function = fun
        
        ## text ##
        self.textpos = (self.rect.x+10, self.rect.y +5)
        p = 1
        orig = [""]
        f = 0
        for i in text:
            if p % t == 0:
                orig.append("")
                f += 1
                orig[f] += i
            else:
                orig[f] += i
            p += 1
        self.text = orig

class Label:
    def __init__(self,screenW, x, y, width, height, font, color, text = "", view = None, textColor = (255,255,255)):
        t = screenW // 17.3
        o = len(text) // t + 1
=======
    def __init__(self, x, y, width, height, font, color, text = "", view = None, textColor = (255,255,255)):
        o = len(text) // 15
>>>>>>> 6ee97553f001fa34f6295b82911ec5433c9cb6e9
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
        p = 1
        orig = [""]
        f = 0
        for i in text:
            if p % t == 0:
                orig.append("")
                f += 1
                orig[f] += i
            else:
                orig[f] += i
            p += 1
        self.text = orig

class Gui:
    def __init__(self, SCREEN_WIDTH:int, SCREEN_HEIGHT:int, displayName:str = "main gui", font:str = None, theme:str = 'dark', iconPath:str = None): 
        
        ## kittens is so adorable :3 ##
            
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(displayName)

        if not iconPath is None:
            if os.path.exists(iconPath):
                img = pg.image.load(iconPath).convert_alpha()
                pg.display.set_icon(img)
            else:
                raise IconExcept(f"The {iconPath} icon file is not found")


        pg.init()
        pg.font.init()

        self.viewmode = ""

        self.sW = SCREEN_WIDTH
        self.sH = SCREEN_HEIGHT
        self.selectorY = 0
        self.objY = 0
        self.onSelectors = False
        self.onView = False
        self.fS = 30
        self.selectors = []
        self.selectorspages = []
        self.buttons = []
        self.labels = []
        self.viewmodeobjects = []
        self.pressed = False
        self.theme = theme

        ## DISPLAY DESIGN ##

        self.font = pg.font.Font(font, self.fS)
        self.frame_1 = pg.Rect(0, 0, SCREEN_WIDTH//5.13, SCREEN_HEIGHT)
        self.frame_2 = pg.Rect(300, 0, SCREEN_WIDTH-SCREEN_WIDTH//5.13, SCREEN_HEIGHT)

        self.splitline = pg.Rect(SCREEN_WIDTH//5.40, 0, SCREEN_WIDTH//102, SCREEN_HEIGHT)

        ## COLORS ##

        if theme not in ["dark", "light"]:
            theme = "dark"

        self.text_color = (255,255,255)

        if self.theme == "dark":
            self.frame_1_color = (36,36,36)
            self.frame_2_color = (71,71,71)
            self.splitline_color = (20,20,20)
            self.selector_color = (80,80,80)
            self.button_color = (60,60,60)
            self.label_color = (75,75,75)
            self.outline_color = (0,0,0)
            
        elif self.theme == "light":
            self.frame_1_color = (219,219,219)
            self.frame_2_color = (184,184,184)
            self.splitline_color = (235,235,235)
            self.selector_color = (175,175,175)
            self.button_color = (195,195,195)
            self.label_color = (180,180,180)
            self.outline_color = (255,255,255)

    def update(self):
        mouse = pg.mouse
        for selector in self.selectors:
            if selector.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]):
                selector.color = (20,20,20)
                if mouse.get_pressed()[0]:
                    self.viewmode = selector.view

            else:
                selector.color = selector.truecolor
        
        if self.frame_1.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]):
            self.onSelectors = True
        else:
            self.onSelectors = False

        if self.frame_2.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]) and self.viewmode != "":
            self.onView = True
        else:
            self.onView = False
        
        for button in self.buttons:
            if self.viewmode == button.view:
                if button.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]):
                    button.color = (20,20,20)

                    if mouse.get_pressed()[0] and self.pressed == False:
                        button.function()
                        self.pressed = True
                    elif mouse.get_pressed()[0] == False:
                        self.pressed = False
                else:
                    button.color = button.truecolor

        self.buttonselected = None


    def draw(self):

        self.screen.fill(self.frame_2_color)
        
        pg.draw.rect(self.screen, self.frame_1_color, self.frame_1)
        pg.draw.rect(self.screen, self.frame_2_color, self.frame_2)
        pg.draw.rect(self.screen, self.splitline_color, self.splitline)

        for selector in self.selectors:
            pg.draw.rect(self.screen, selector.color, selector.rect, border_radius=20)
            pg.draw.rect(self.screen, self.outline_color, selector.rect, width = 2, border_radius=20)
            y = 0
            for i in selector.text:
                text = selector.font.render(i, True, selector.textcolor)
                p = [selector.textpos[0], selector.textpos[1]]
                p[1] += y
                self.screen.blit(text, p)
                y += 30 # gap
        
        for button in self.buttons:
            if self.viewmode == button.view:
                pg.draw.rect(self.screen, button.color, button.rect, border_radius=20)
                pg.draw.rect(self.screen, self.outline_color, button.rect, width = 2, border_radius=20)
                y = 0
                for i in button.text:
                    text = selector.font.render(i, True, button.textcolor)
                    p = [button.textpos[0], button.textpos[1]]
                    p[1] += y
                    self.screen.blit(text, p)
                    y += 30 # gap

        for label in self.labels:
            if self.viewmode == label.view:
                pg.draw.rect(self.screen, label.color, label.rect, border_radius=20)
                pg.draw.rect(self.screen, self.outline_color, label.rect, width = 2, border_radius=20)
                y = 0
                for i in label.text:
                    text = label.font.render(i, True, button.textcolor)
                    p = [label.textpos[0], label.textpos[1]]
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
                if self.onView:

                    evy = event.y 

                    if evy == 1: self.objY -= 1
                    elif evy == -1: self.objY += 1
                    
                    if event.y == 1 and self.objY < 0:
                        self.objY += 1
                        return
                    
                    vmobj = []
                    for o in self.viewmodeobjects:
                        if o.view == self.viewmode:
                            vmobj.append(o)
            
                    if event.y == -1 and self.objY == len(vmobj)//2:
                        self.objY -= 1
                        return
        

                    for obj in self.viewmodeobjects:
                        step = 30 + obj.rect.height
                        if evy == 1:
                            obj.rect.y += step
                            a = [obj.textpos[0], obj.textpos[1] + step]
                            obj.textpos = a
                        else:
                            obj.rect.y -= step
                            a = [obj.textpos[0], obj.textpos[1] - step]
                            obj.textpos = a
            
    
    def main_loop(self): 
        while True:
            self.update()
            self.draw()
            self.event()


    def add_selector(self, selectorText:str, viewMode:str):
        if viewMode in ["", " "]:
            raise ViewModeExcept("Invalid viewMode argument")

        y = 30 + len(self.selectors) * 20
        
        for selector in self.selectors:
            if selector.view == viewMode:
                raise ViewModeExcept("Excepted the same viewMode")
            
            y += selector.rect.height

        selector = Selector(self.sW, self.sW//51.3, y, self.sW//7.7, 30, self.font, self.selector_color, selectorText, viewMode, self.text_color)

        if len(self.selectors) == 0:
            self.viewmode = viewMode

        self.selectors.append(selector)

    def add_button(self, buttonText:str, viewMode:str, function):
        if viewMode in ["", " "]:
            raise ViewModeExcept("Invalid viewMode argument")
        y = 30 + len(self.viewmodeobjects) * 20

        for ob in self.viewmodeobjects:
            y += ob.rect.height

        button = Button(self.sW, self.sW//4.6, y, self.sW//1.4, 30, self.font, self.button_color, function, buttonText, viewMode, self.text_color)
        self.buttons.append(button)
        self.viewmodeobjects.append(button)

    def add_label(self, labelText:str, viewMode:str):
        if viewMode in ["", " "]:
            raise ViewModeExcept("Invalid viewMode argument")
        y = 30 + len(self.viewmodeobjects) * 20

        for ob in self.viewmodeobjects:
            y += ob.rect.height

        label = Label(self.sW, self.sW//4.6, y, self.sW//1.4, 30, self.font, self.label_color, labelText, viewMode, self.text_color)
        self.labels.append(label)
        self.viewmodeobjects.append(label)

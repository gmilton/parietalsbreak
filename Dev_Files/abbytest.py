#!/usr/bin/env python

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
import os, sys
import pygame
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

## a simple class that uses the generator
# and can tell if it is done
pygame.mixer.init(44100, -16,2,2048)
pygame.init()
 
font = pygame.font.Font("Aaargh.ttf", 15)

# raise the USEREVENT every 1000ms
pygame.time.set_timer(pygame.USEREVENT, 200)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Parietals Break")

# Background Music
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Scrolling text functions 
def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        # don't pause for spaces
        if letter != ' ':
            yield tmp

class DynamicText(object):
    def __init__(self, font, text, pos, autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.pos = pos
        self.autoreset = autoreset
        self.update()

    # Reset text to loop
    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, (0, 128, 0))
            except StopIteration:
                self.done = True
                if self.autoreset: self.reset()

    # Displays text 
    def draw(self, screen):
        screen.blit(self.rendered, self.pos)

# Actual function that does the actual thing
def textBox(text):
        message = DynamicText(font, text, (200, 200), autoreset=False)
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: break
 #                       if event.type == pygame.USEREVENT: message.update()
                else:
                        message.draw(screen)
                        pygame.display.flip()
                        clock.tick(3)
                        continue
                break

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background = pygame.image.load("pictures/front_layer_title.png")
background = pygame.transform.scale(background, (700, 500))

clouds = pygame.image.load("pictures/clouds.png")

title = pygame.image.load("pictures/title_text.png")

play = pygame.image.load("pictures/play.png")

def backgroundimg(bg, x,y):
	screen.blit(bg, (x,y))

def cloudsimg(x,y):
	screen.blit(clouds, (x,y))

def titleimg(x,y):
	screen.blit(title, (x,y))

def playimg(x,y):

	screen.blit(play, (x,y))

x = 0
y = 0

cx = -100
cy = 0

cx2 = -800
cy2 = 0

def drawPrompt(prompt):
	numchars = len(prompt)
	counter = 0 	
	ycoord = 330
	lineLength = 70
	while counter < numchars-lineLength:
		linechars = 0
		for word in prompt[counter:numchars].split():
			linechars = linechars+len(word)+1
			if linechars > lineLength:
				break
		if counter < numchars:
			line = prompt[counter:counter+linechars].strip()
			one = font.render(line, False, (0, 0, 0))
			screen.blit(one, (50, ycoord))
			ycoord = ycoord + 25
		counter = counter + linechars
	line = prompt[counter:numchars].strip()
	one = font.render(line, False, (0, 0, 0))
	screen.blit(one, (50, ycoord))
	

# If only one person, type 'none.png' into person2.
def drawScene(person1, person2, background):
	backgroundimg(pygame.image.load(background), x, y);	
	backgroundimg(pygame.image.load(person1), x, y);
	backgroundimg(pygame.image.load(person2), x+400, y);
	backgroundimg(pygame.image.load("pictures/textBox.png"), x, y);	

# If there are less than 4 choices type " ".
def drawChoices(name, choice1, choice2, choice3, choice4):
	choiceFont = pygame.font.Font(None, 30)
	
	name = font.render(name, False, (255, 255, 255))
	one = choiceFont.render(choice1, False, (0, 0, 0))
	two = choiceFont.render(choice2, False, (0, 0, 0))
	three = choiceFont.render(choice3, False, (0, 0, 0))
	four = choiceFont.render(choice4, False, (0, 0, 0))
	screen.blit(name, (50, 300))
	screen.blit(one, (100, 410))
	screen.blit(two, (350, 410))
	screen.blit(three, (100, 440))
	screen.blit(four, (350, 440))

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    #MENU
    homescreen = True
    while homescreen:
        for event in pygame.event.get():
        #print type(event)
            if event.type == pygame.QUIT:
                done = True
                homescreen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                if m > 335 and m < 390 and n > 155 and n < 185:
                   screen.fill(WHITE)
                   homescreen = False
            else:
                screen.fill((252, 220, 197))
		cx = cx + 10
		cx2 = cx2 + 10
		if cx > 700:
		    cx = -700
		    print cx
		if cx2 > 700:
                    cx2 = -700
		cloudsimg(cx,cy)
		cloudsimg(cx2,cy2)
                backgroundimg(background,x,y)
		titleimg(x,y)
		playimg(x,y)
                pygame.display.update()
                pygame.display.flip()
 
    # --- Game logic should go here
    scene0 = True
    while scene0 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene0 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene0 = False
            else:
		drawPrompt("What is your name?")
		pygame.display.update()
                pygame.display.flip()
        	scene1 = True
    
    scene1 = True
    while scene1 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene1 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene1 = False
            else:
		drawScene("pictures/Silvia - thinking.png", "pictures/none.png", "pictures/dorm_bg.png")	
		drawPrompt("So you wake up one fine Friday morning in yoir dorm room in PE to your alarm. You have an 8:20 class, but aren't sure if you want to go. Do you go?")
		drawChoices("Silvia", " ", " ", "Of Course!", "Nah ma, stay in bed.")
		pygame.display.update()
                pygame.display.flip()
        	scene2 = True
    
    while scene2 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene2 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene2 = False
            else:
		drawScene("pictures/Silvia - sigh.png", "pictures/none.png", "pictures/dorm_bg.png")
		drawPrompt("That's a good idea. You've already paid an arm and a leg for it, anyways. You might as well go.")
		drawChoices("Silvia", " ", " ", "Continue", " ")
		pygame.display.update()
                pygame.display.flip()
		scene3 = True 

    while scene3 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene3 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene3 = False
            else:
		drawScene("pictures/Silvia - neutral.png", "pictures/Abby - Sad.png", "pictures/hallway_bg.png")
		drawPrompt("It's 8:10 AM.  Parietals are still in effect but you notice your RA trying to sneak out a member of the opposite sex. She asks you if you're willing to keep it between the both of you.")
		drawChoices("Silvia", "..For Price", "Scream and Faint", "Look the other way", "Speedial #2 for the Rector")
		pygame.display.update()
                pygame.display.flip()
    		scene4 = True

    while scene4 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene4 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene4 = False
            else:
		drawScene("pictures/Silvia - neutral.png", "pictures/Abby - Smiling.png", "pictures/hallway_bg.png")
		drawPrompt("They thank you for turning a blind eye and head out unnoticed. You walk to your first class.")
		drawChoices("Silvia", " ", " ",  "This might help you later...", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene5 = True

    while scene5 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene5 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene5 = False
            else:
		drawScene("pictures/Silvia - smiling.png", "pictures/none.png", "pictures/cafeteria_bg.png")
		drawPrompt("After your last class of the day your friends invite you to a late lunch. Do you want to go?")
		drawChoices("Silvia", "Yes, I have a craving for cheese right now.", " ",  "No, I have a date wth Jay Brockman", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene6 = True

    while scene6 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene6 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene6 = False
            else:
		drawScene("pictures/Silvia - neutral.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
		drawPrompt("You and your friends head to NDH, the superior dining hall, and grab a seat. What kind of food are you hungry for?")
		drawChoices("Silvia", "Yes.", "Tacos", "Pizza", "Literally just a single slice of cheese")
		pygame.display.update()
                pygame.display.flip()
    		scene7 = True

    while scene7 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene7 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene7 = False
            else:
		drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
		drawPrompt("You pick a single slice of cheese because that's just the kind of monster that you are. You try to decorate it with tiny bits of lettuce to make the dish look more appealing. You failed. You proceed to eat it with a knife and fork. You take an extra piece of cheese to go.")
		drawChoices("Silvia", " ", " ", "Continue", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene8 = True

    while scene8 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene8 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene8 = False
            else:
		drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
		drawPrompt("One of your friends is disappointed with the food selection and wants to go to the grocery store. She asks if you want to join.")
		drawChoices("Silvia", " ", " ", "Yes, I need more cheese.", "No, I don't even like you.")
		pygame.display.update()
                pygame.display.flip()
    		scene9 = True

    while scene9 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene9 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene9 = False
            else:
		drawScene("pictures/Silvia - Smiling.png", "pictures/cheese.png", "pictures/cafeteria_bg.png")
		drawPrompt("What a good friend! She's so appreciative that she buys you some cheese! You now head back to the dorm to get some work done.")
		drawChoices("Silvia", " ", " ", "Continue", " ");
		pygame.display.update()
                pygame.display.flip()
    		sceneCheese = True

    CheeseC = 0
    while sceneCheese and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sceneCheese = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                sceneCheese = False
            else:
		CheeseC += 5
		rotatedcheese = rot_center(pygame.image.load('pictures/cheese.png'), CheeseC)
		drawScene("pictures/none.png", "pictures/none.png", "pictures/rays.png")
		drawPrompt("You've acquired CHEESE!")
		drawChoices("Silvia", " ", " ", "Continue", " ");
		screen.blit(rotatedcheese, (200,0))
		pygame.display.update()
                pygame.display.flip()
		screen.fill(WHITE)
    		scene10 = True


    while scene10 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene10 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene10 = False
            else:
		drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
		drawPrompt("On the way back, you run into someone from your section.")
		drawChoices("Silvia", "Wave at them", "Scream and faint", "Insult them", "Profess your love to them");
		pygame.display.update()
                pygame.display.flip()
    		scene11 = True

    while scene11 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene11 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene11 = False
            else:
		drawScene("pictures/Silvia - Smiling.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("That was nice of you it seems to have brightened their day. You know those random acts of kindness can really benefit you in the long run...")
		drawChoices("Silvia", " ", " ", "Continue", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene12 = True

    while scene12 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene12 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene12 = False
            else:
		drawScene("pictures/Silvia - Smiling.png", "pictures/Grace - Smiling.png", "pictures/cafeteria_bg.png")
		drawPrompt("When you get back to your dorm you realize it's been literally 6 years since you last exercised. Do you want to go for a quick run?")
		drawChoices("Silvia", "Hell yeah! Do you even lift bro?", " ", "Nah, I'm healthy enough.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene13 = True

    while scene13 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene13 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene13 = False
            else:
		drawScene("pictures/Silvia - Smiling.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Good idea, it's always good to stay healthy! On yourway back to your room, you run into your friend and they invite you back to their room. Do you want to go with them?")
		drawChoices("Silvia", "Yeah! Dude, they have Doritos!", " ", "Sorry, cant. My life is dope and I do dope stuff", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene14 = True

    while scene14 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene14 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene14 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Your friend understands they can never reach your level of dopeness and sends you on your way with a sense of awe at all the dope stuff you're gonna do. You walk away thinking about how Verilog is a hardware description language.")
		drawChoices("Silvia"," ", " ", "Continue", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene15 = True

    while scene15 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene15 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene15 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Now that you're back in your room, your roomate asks if you wan to take a stroll around the dorm or just stay in your room and play Lego Star Wars on her emulator and order Knotty Knoodles.")
		drawChoices("Silvia"," ", "Walk around", "Stay because Knoodles, duh!", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene16 = True

    while scene16 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene16 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene16 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Now that you're back in your room, your roomate asks if you wan to take a stroll around the dorm or just stay in your room and play Lego Star Wars on her emulator and order Knotty Knoodles.")
		drawChoices("Silvia"," ", "Walk around", "Stay because Knoodles, duh!", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene17 = True

    while scene17 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene17 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene17 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("As you walk around, you notice that one of the side doors is blocked for construction because of the Great PE Flood of 2016. The guy who build this dorm deserves an award, really. If you need to exit, you CANNOT exit throught the WEST-FACING door.")
		drawChoices("Silvia"," ", " ", " Continue", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene18 = True

    while scene18 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene18 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene18 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("As you walk, you notice some empty rooms. Do you want to peek inside?")
		drawChoices("Silvia"," ", "Yeah, totally not creepy.", "Nah, I'm good.", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene19 = True

    while scene19 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene19 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene19 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("You see your neighbor has left some food out on their desk with a sign encouraging people to take some, so you do. They left cheese! Your single slice of cheese now has a friend. You head back to your room.")
		drawChoices("Silvia"," ", " ", "Continue", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene20 = True

    while scene20 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene20 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene20 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("You decide to stop being a creep and you don't go into the room. You go back to your room to play Pikmin and watch Nacho Libre with your roommate.")
		drawChoices("Silvia"," ", " ", "Continue", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene21 = True

    while scene21 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene21 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene21 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("You literally suck at Pikmin and accidentally drown half of your Pikmin friends. It's  getting pretty late and your roommate asks the all-important question...")
		drawChoices("Silvia"," ", " ", "I'm listening...", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene22 = True


    while scene22 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene22 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene22 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Do you want to go out this lovely Friday night (to have wholesome fun drinking non-alcoholic juice-based beverages that were definitely not made in a trash can and probably play some charades?)")
		drawChoices("Silvia","Hell yea, I love \"charades\"!", " ", "Nah, let's get a milkshake from Smashburger.", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene23 = True

    while scene23 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene23 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene23 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Due to some wild and unforseen consequences that involve a party cab, barbecue sauce, a stolen American flag, and the Polish festival of Dingus Day, you find yourself after 2am with a member of the opposite gender!")
		drawChoices("Silvia", " ", " ", "Oh, no", " ")
		pygame.display.update()
                pygame.display.flip()
    		scene24 = True

    while scene24 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene24 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene24 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Because we're obviously not adults capable of making decisions, the RA's are patrolling, looking for any stray males in the building but your guest wants to get to bed.") 
		drawChoices("Silvia", " ", " ", "Continue.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene25 = True

    while scene25 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene25 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene25 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("Looks like you're gonna have to facilitate a PARIETALS BREAK!")
		drawChoices("Silvia", " ", " ", "Bring it.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene26 = True

    while scene26 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene26 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene26 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("You should have foreseen this, but in your excitement you forgot the inevitable result of obtaining a milkshake. Your milkshake brought all the boys to your yard! And by yard I mean extremely small dorm room!")
		drawChoices("Silvia", " ", " ", "Well, at least it's better than yours.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene27 = True

    while scene27 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene27 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene27 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("You manage to herd them out, but as the clock strikes 2am, you realize that there is one remaining member of the opposite gender!")
		drawChoices("Silvia", " ", " ", "Well, now what.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene28 = True

    while scene28 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene28 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene28 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("All right, it's time to get this boy to freedom. You've got to make a run for the staircases. You room is right in the middle. Do you want to go for the main or the side staircase?")
		drawChoices("Silvia", "Main Staircase", " ", "Side Staircase", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene29 = True

    while scene29 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene29 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene29 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("You hear someone in the e-lounge. Do you want to stay on this path or turn around and go to the other staircase?")
		drawChoices("Silvia", "Turn back, turn back, turn back!", " ", "This boy ain't gonna free himself. Keep going.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene30 = True

    while scene30 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene30 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene30 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("You hear the jingle of keys from the RA walking up the stairs. Do you want to stay on this path or go to the other staircase?")
		drawChoices("Silvia", "Turn back, turn back, turn back!", " ", "This boy ain't gonna free himself. Keep going.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene31 = True

    while scene31 and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                scene31 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (m,n) = pygame.mouse.get_pos()
                print pygame.mouse.get_pos()
                screen.fill(WHITE)
                scene31 = False
            else:
		drawScene("pictures/Silvia - GTFO.png", "pictures/none.png", "pictures/forest_bg.png")
		drawPrompt("There's someone in the e-lounge.")
		drawChoices("Silvia", "Might be a regular person. Just wait them out.", " ", "I don't even like this guy! I need him out. Go to the stairs.", " ");
		pygame.display.update()
                pygame.display.flip()
    		scene31 = True
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here
    # --- Go ahead and update the screen with what we've drawn.
 
    # --- Limit to 60 frames per second
    clock.tick(600)
 
# Close the window and quit.
pygame.quit()

import pygame

pygame.init() #initialize the pygame libs

""" screen """
screen = pygame.display.set_mode((800, 600)) #this creats the game window with the width and hieght

""" title and icon """
pygame.display.set_caption("Space Invaders") #sets the game name
icon = pygame.image.load('rocket.png') #sets the word icon as the path of the image
pygame.display.set_icon(icon) #sets the icon var as the icon for the game window

""" player """
playerIMG = pygame.image.load('player1.png') #create a var to be the image we want
playerX = 370 #sets the x-axis cords
playerY = 480 #sets the y-axis cords
player_change = 0

def player(x,y): #create a function to be the player
    screen.blit(playerIMG, (x, y)) #screen.blit draws the image on the screen, at the passed x,y cords. drawimage [screen.blit((image var), (x cords, y cords))]


""" infinte loop for run time """
#the following creates a game loop for the quit function so we are able to close it, otherwise the loop will always be set to true and the game will never close
running = True
while running:
    screen.fill((0, 0, 0))  # sets the color for the backgorund we add it to the while loop as we want the color to be consistent across all the screens until exit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #creates an even for the presseing of a key
            print("Key stroke pressed")
            if event.key == pygame.K_LEFT: #checks what key is pressed, if its the left arrow print the following, and move x-cords by -0.3 (moves to the left)
                player_change = -0.3
                print("left key pressed")
            if event.key == pygame.K_RIGHT:#checks what key is pressed, if its the right arrow print the following, and move x-cords by 0.3 (moves to the right)
                player_change = 0.3
                print("right key pressed")

        if event.type == pygame.KEYUP: #creates an event so that when the key pressed is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #if left or right key get relased 
                player_change = 0.0
                print("key released")

    playerX += player_change
    player(playerX, playerY) #call the player function, make sure it is under our screen.fill otherwise it will be behind it



    pygame.display.update() #this line is pretty much necessary as it ensures the game display is updating with moves and so on
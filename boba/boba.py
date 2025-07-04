import pygame
import sys

# Initialize Pygame
pygame.init()


################################### music section #######################################
pygame.mixer.init()
current_music = "sounds/boba_date.mp3"
previous_music = None  # To remember what to resume

pygame.mixer.music.load("sounds/boba_date.mp3")  # Replace with your file path
click_sound = pygame.mixer.Sound("sounds/mouse-click-sound.mp3")  # Replace with your file path
tada_sound = pygame.mixer.Sound("sounds/tada.mp3")  # Load once at the top
tada_played = False


pygame.mixer.music.play(-1)
music_on = True

def play_music(file, loop=True):
    global current_music
    if music_on:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1 if loop else 0)
        current_music = file

def toggle_music():
    global music_on
    music_on = not music_on
    if not music_on:
        pygame.mixer.music.stop()
    else:
        play_music(current_music)


################################## Screen dimensions ##################################
WIDTH, HEIGHT = 500, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boba Tea Builder")

###################################### colors ######################################
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (70, 130, 180)
DARK_PINK = (231, 84, 128)
WHITE = (244, 240, 224)  # White text
LIGHT_PINK = (230, 143, 172)
LIGHT_GREEN = (136, 167, 142)
DARK_GREEN = (87, 116, 94)

########################## button dimensions ###############################
button_width = 250
button_height = 75
button_x = (WIDTH - button_width) // 2
button_y = HEIGHT - button_height - 50  # 20 pixels from the bottom

back_button_width = 100
back_button_height = 40
back_button_x = 20
back_button_y = 20  # 20 pixels from the top left corner

# Next button dimensions (bottom right corner)
next_button_width = 100
next_button_height = 40
next_button_x = WIDTH - next_button_width - 20
next_button_y = HEIGHT - next_button_height - 20

base_button_width = 140  # Increase the width of the buttons
base_button_height = 50
base_gap = 20  # Increase the gap between buttons
vert = 20

# First row (3 buttons)
option_button1 = pygame.Rect(vert, HEIGHT - 2 * (base_button_height + base_gap) - 60, base_button_width, base_button_height)
option_button2 = pygame.Rect(vert + base_button_width + base_gap, HEIGHT - 2 * (base_button_height + base_gap) - 60, base_button_width, base_button_height)
option_button3 = pygame.Rect(vert + 2 * (base_button_width + base_gap), HEIGHT - 2 * (base_button_height + base_gap) - 60, base_button_width, base_button_height)

# Second row (3 buttons)
option_button4 = pygame.Rect(vert, HEIGHT - (base_button_height + base_gap) - 60, base_button_width, base_button_height)
option_button5 = pygame.Rect(vert + base_button_width + base_gap, HEIGHT - (base_button_height + base_gap) - 60, base_button_width, base_button_height)
option_button6 = pygame.Rect(vert + 2 * (base_button_width + base_gap), HEIGHT - (base_button_height + base_gap) - 60, base_button_width, base_button_height)

# Volume button dimensions
volume_button_rect = pygame.Rect(WIDTH - 70, 20, 50, 50)  # top-right corner

################################# fonts #############################################

arial = pygame.font.SysFont("Arial", 34)

def get_starbim(size):
    return pygame.font.Font("fonts/Starbim.ttf", size)  # or None if using default font

def get_kiwi(size):
    return pygame.font.Font("fonts/Kiwi Fruit.otf", size)  # or None if using default font

def get_bubble(size):
    return pygame.font.Font("fonts/Chewy Bubble.otf", size)  # or None if using default font

def get_valty(size):
    return pygame.font.Font("fonts/valty.otf", size)  # or None if using default font

################################ text rendering #####################################

# Render each line separately
title_line1 = get_bubble(100).render("BOBA", True, LIGHT_PINK)
title_line2 = get_bubble(100).render("MAKER", True, LIGHT_PINK)

# Position them stacked vertically
title_line1_rect = title_line1.get_rect(center=(WIDTH // 2, 60))
title_line2_rect = title_line2.get_rect(center=(WIDTH // 2, 130))

page2_line1_title = get_starbim(40).render("CHOOSE YOUR", True, LIGHT_PINK)
page2_line2_title = get_starbim(40).render("FLAVOUR!", True, LIGHT_PINK)

page2_line1_title_rect = page2_line1_title.get_rect(center=(WIDTH // 2, 100))
page2_line2_title_rect = page2_line2_title.get_rect(center=(WIDTH // 2, 150))

page3_line1_title = get_starbim(40).render("CHOOSE YOUR", True, LIGHT_PINK)
page3_line2_title = get_starbim(40).render("ICE LEVEL!", True, LIGHT_PINK)

page3_line1_title_rect = page3_line1_title.get_rect(center=(WIDTH // 2, 100))
page3_line2_title_rect = page3_line2_title.get_rect(center=(WIDTH // 2, 150))

page4_line1_title = get_starbim(40).render("CHOOSE YOUR", True, LIGHT_PINK)
page4_line2_title = get_starbim(40).render("SUGAR LEVEL!", True, LIGHT_PINK)

page4_line1_title_rect = page4_line1_title.get_rect(center=(WIDTH // 2, 100))
page4_line2_title_rect = page4_line2_title.get_rect(center=(WIDTH // 2, 150))

page5_line1_title = get_starbim(40).render("CHOOSE YOUR", True, LIGHT_PINK)
page5_line2_title = get_starbim(40).render("BOBA!", True, LIGHT_PINK)

page5_line1_title_rect = page5_line1_title.get_rect(center=(WIDTH // 2, 100))
page5_line2_title_rect = page5_line2_title.get_rect(center=(WIDTH // 2, 150))

page6_line1_title = get_starbim(40).render("CHOOSE YOUR", True, LIGHT_PINK)
page6_line2_title = get_starbim(40).render("TOPPING!", True, LIGHT_PINK)

page6_line1_title_rect = page6_line1_title.get_rect(center=(WIDTH // 2, 90))
page6_line2_title_rect = page6_line2_title.get_rect(center=(WIDTH // 2, 150))


# Render the text
page7_line1_title = get_bubble(60).render("ENJOY!!!", True, DARK_PINK)
page7_line2_title = get_bubble(60).render("THE BOBA!!!", True, DARK_PINK)

# Position the text
page7_line1_title_rect = page7_line1_title.get_rect(center=(WIDTH // 2, 620))
page7_line2_title_rect = page7_line2_title.get_rect(center=(WIDTH // 2, 680))

# Create white rectangles behind the text with narrower width
page7_line1_bg_rect = pygame.Rect(page7_line1_title_rect.left - 5, page7_line1_title_rect.top - 5, page7_line1_title_rect.width - 5, page7_line1_title_rect.height + 5)
page7_line2_bg_rect = pygame.Rect(page7_line2_title_rect.left - 5, page7_line2_title_rect.top - 5, page7_line2_title_rect.width - 5, page7_line2_title_rect.height + 5)


# Load background image (JPEG)
background_image = pygame.image.load('misc/boba_hpage.jpg')  # Replace with the path to your JPEG file
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale to fit screen

background = pygame.image.load('misc/background.png')  # Replace with the path to your PNG file
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Scale to fit screen

frosting_background = pygame.image.load('misc/frostingbg.png')  # Replace with the path to your PNG file
frosting_background = pygame.transform.scale(frosting_background, (WIDTH, HEIGHT))  # Scale to fit screen

############################################ loading cup and mixing ##################################

cup_outline = pygame.image.load('misc/cup.png')
cup_outline = pygame.transform.scale(cup_outline, (WIDTH, HEIGHT))  # Scale to fit screen

mixing_img = pygame.image.load('misc/mixing.png')
mixing_img = pygame.transform.scale(mixing_img, (WIDTH, HEIGHT))  # Scale to fit screen

############################################ loading flavours ##################################

classic_img = pygame.image.load('flavours/classic.png')
classic_img = pygame.transform.scale(classic_img, (WIDTH, HEIGHT))  # Scale to fit screen

matcha_img = pygame.image.load('flavours/matcha.png')
matcha_img = pygame.transform.scale(matcha_img, (WIDTH, HEIGHT))  # Scale to fit screen

berry_img = pygame.image.load('flavours/berry.png')
berry_img = pygame.transform.scale(berry_img, (WIDTH, HEIGHT))  # Scale to fit screen

mango_img = pygame.image.load('flavours/mango.png')
mango_img = pygame.transform.scale(mango_img, (WIDTH, HEIGHT))  # Scale to fit screen

oreo_img = pygame.image.load('flavours/oreo.png')
oreo_img = pygame.transform.scale(oreo_img, (WIDTH, HEIGHT))  # Scale to fit screen

taro_img = pygame.image.load('flavours/taro.png')
taro_img = pygame.transform.scale(taro_img, (WIDTH, HEIGHT))  # Scale to fit screen

############################################ loading sugars #######################################

sugar_0 = None

sugar_25 = pygame.image.load('sugars/25.png')
sugar_25 = pygame.transform.scale(sugar_25, (WIDTH, HEIGHT))  # Scale to fit screen

sugar_50 = pygame.image.load('sugars/50.png')
sugar_50 = pygame.transform.scale(sugar_50, (WIDTH, HEIGHT))  # Scale to fit screen

sugar_75 = pygame.image.load('sugars/75.png')
sugar_75 = pygame.transform.scale(sugar_75, (WIDTH, HEIGHT))  # Scale to fit screen

sugar_100 = pygame.image.load('sugars/100.png')
sugar_100 = pygame.transform.scale(sugar_100, (WIDTH, HEIGHT))  # Scale to fit screen

sugar_125 = pygame.image.load('sugars/125.png')
sugar_125 = pygame.transform.scale(sugar_125, (WIDTH, HEIGHT))  # Scale to fit screen

############################################ loading sugars #######################################

ice_0 = None

ice_25 = pygame.image.load('ices/25.png')
ice_25 = pygame.transform.scale(ice_25, (WIDTH, HEIGHT))  # Scale to fit screen

ice_50 = pygame.image.load('ices/50.png')
ice_50 = pygame.transform.scale(ice_50, (WIDTH, HEIGHT))  # Scale to fit screen

ice_75 = pygame.image.load('ices/75.png')
ice_75 = pygame.transform.scale(ice_75, (WIDTH, HEIGHT))  # Scale to fit screen

ice_100 = pygame.image.load('ices/100.png')
ice_100 = pygame.transform.scale(ice_100, (WIDTH, HEIGHT))  # Scale to fit screen

ice_125 = pygame.image.load('ices/125.png')
ice_125 = pygame.transform.scale(ice_125, (WIDTH, HEIGHT))  # Scale to fit screen

############################################ loading sugars #######################################

noneboba_img = None

brownsugar_img = pygame.image.load('bobas/brownsugar.png')
brownsugar_img = pygame.transform.scale(brownsugar_img, (WIDTH, HEIGHT))  # Scale to fit screen

sago_img = pygame.image.load('bobas/sago.png')
sago_img = pygame.transform.scale(sago_img, (WIDTH, HEIGHT))  # Scale to fit screen

fruit_jelly_img = pygame.image.load('bobas/fruitjelly.png')
fruit_jelly_img = pygame.transform.scale(fruit_jelly_img, (WIDTH, HEIGHT))  # Scale to fit screen

mango_jelly_img = pygame.image.load('bobas/mangojelly.png')
mango_jelly_img = pygame.transform.scale(mango_jelly_img, (WIDTH, HEIGHT))  # Scale to fit screen

ube_img = pygame.image.load('bobas/ube.png')
ube_img = pygame.transform.scale(ube_img, (WIDTH, HEIGHT))  # Scale to fit screen

############################################ loading sugars #######################################

shortcake_img = pygame.image.load('toppings/shortcake.png')
shortcake_img = pygame.transform.scale(shortcake_img, (WIDTH, HEIGHT))  # Scale to fit screen

cookie_bits_img = pygame.image.load('toppings/cookiebits.png')
cookie_bits_img = pygame.transform.scale(cookie_bits_img, (WIDTH, HEIGHT))  # Scale to fit screen

oreo_pieces_img = pygame.image.load('toppings/oreopieces.png')
oreo_pieces_img = pygame.transform.scale(oreo_pieces_img, (WIDTH, HEIGHT))  # Scale to fit screen

mango_topping_img = pygame.image.load('toppings/mangotopping.png')
mango_topping_img = pygame.transform.scale(mango_topping_img, (WIDTH, HEIGHT))  # Scale to fit screen

kiwi_img = pygame.image.load('toppings/kiwi.png')
kiwi_img = pygame.transform.scale(kiwi_img, (WIDTH, HEIGHT))  # Scale to fit screen

sprinkles_img = pygame.image.load('toppings/sprinkles.png')
sprinkles_img = pygame.transform.scale(sprinkles_img, (WIDTH, HEIGHT))  # Scale to fit screen

############################# dictionaries ################################
flavours = {
    "classic": classic_img,
    "matcha": matcha_img,
    "berry": berry_img,
    "mango": mango_img,
    "oreo": oreo_img,
    "taro": taro_img
}

ices = {
    "0%": ice_0,
    "25%": ice_25,
    "50%": ice_50,
    "75%": ice_75,
    "100%": ice_100,
    "125%": ice_125
}

sugars = {
    "0%": sugar_0,
    "25%": sugar_25,
    "50%": sugar_50,
    "75%": sugar_75,
    "100%": sugar_100,
    "125%": sugar_125
}

bobas = {
    "none": noneboba_img,
    "brown sugar": brownsugar_img,
    "sago": sago_img,
    "fruit jelly": fruit_jelly_img,
    "mango jelly": mango_jelly_img,
    "ube": ube_img
}

toppings = {
    "shortcake": shortcake_img,
    "cookie bits": cookie_bits_img,
    "oreo pieces": oreo_pieces_img,
    "mango": mango_topping_img,
    "kiwi": kiwi_img,
    "sprinkles": sprinkles_img
}


############################ selected options #######################
selected_flavour = None
selected_ice = None 
selected_sugar = None
selected_boba = None
selected_topping = None

############################################ drawing buttons #####################################################
def draw_home_button():
    # Check if the mouse is hovering over the button
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
        pygame.draw.rect(screen, DARK_PINK, (button_x, button_y, button_width, button_height), border_radius=15)
    else:
        pygame.draw.rect(screen, LIGHT_PINK, (button_x, button_y, button_width, button_height), border_radius=15)

    # Draw the text on the button
    text = get_starbim(50).render("START", True, WHITE)
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)

def draw_back_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if back_button_x <= mouse_x <= back_button_x + back_button_width and back_button_y <= mouse_y <= back_button_y + back_button_height:
        pygame.draw.rect(screen, DARK_GREEN, (back_button_x, back_button_y, back_button_width, back_button_height), border_radius=10)
    else:
        pygame.draw.rect(screen, LIGHT_GREEN, (back_button_x, back_button_y, back_button_width, back_button_height), border_radius=10)

    text = get_starbim(20).render("BACK", True, WHITE)
    text_rect = text.get_rect(center=(back_button_x + back_button_width // 2, back_button_y + back_button_height // 2))
    screen.blit(text, text_rect)

def draw_next_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if next_button_x <= mouse_x <= next_button_x + next_button_width and next_button_y <= mouse_y <= next_button_y + next_button_height:
        pygame.draw.rect(screen, DARK_GREEN, (next_button_x, next_button_y, next_button_width, next_button_height), border_radius=10)
    else:
        pygame.draw.rect(screen, LIGHT_GREEN, (next_button_x, next_button_y, next_button_width, next_button_height), border_radius=10)

    text = get_starbim(20).render("NEXT", True, WHITE)
    text_rect = text.get_rect(center=(next_button_x + next_button_width // 2, next_button_y + next_button_height // 2))
    screen.blit(text, text_rect)

def draw_volume_button():
    color = LIGHT_PINK if music_on else DARK_PINK  # light green if on, gray if off
    pygame.draw.circle(screen, color, volume_button_rect.center, 25)
    icon = arial.render("♫" if music_on else "-♫-", True, WHITE)
    icon_rect = icon.get_rect(center=volume_button_rect.center)
    screen.blit(icon, icon_rect)

# Function to draw the buttons with hover and click effects
def draw_option_buttons(text1, text2, text3, text4, text5, text6):
    mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
    mouse_click = pygame.mouse.get_pressed()  # Get the state of the mouse button (0=not pressed, 1=pressed)

    # Function to draw a button with hover/click effect
    def draw_button(button, is_hovered, is_clicked):
        if is_hovered:
            color = DARK_PINK if is_clicked else (255, 183, 193)  # Change color on hover and click
        else:
            color = LIGHT_PINK  # Normal button color
        pygame.draw.rect(screen, color, button, border_radius=10)

    # Draw each button with the appropriate color
    draw_button(option_button1, option_button1.collidepoint(mouse_pos), mouse_click[0])
    draw_button(option_button2, option_button2.collidepoint(mouse_pos), mouse_click[0])
    draw_button(option_button3, option_button3.collidepoint(mouse_pos), mouse_click[0])
    draw_button(option_button4, option_button4.collidepoint(mouse_pos), mouse_click[0])
    draw_button(option_button5, option_button5.collidepoint(mouse_pos), mouse_click[0])
    draw_button(option_button6, option_button6.collidepoint(mouse_pos), mouse_click[0])

    # Function to render text inside the buttons
    def label(text, rect):
        text_surf = get_kiwi(30).render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect)

    # Render text for each button
    label(text1, option_button1)
    label(text2, option_button2)
    label(text3, option_button3)
    label(text4, option_button4)
    label(text5, option_button5)
    label(text6, option_button6)



######################## handling clicks ############################
def handle_back_button_click(pos):
    x, y = pos
    return 20 <= x <= 120 and 20 <= y <= 60

# Function to handle button click
def handle_button_click(pos):
    x, y = pos
    return button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height


def handle_back_button_click(pos):
    return back_button_x <= pos[0] <= back_button_x + back_button_width and back_button_y <= pos[1] <= back_button_y + back_button_height

def handle_next_button_click(pos):
    return next_button_x <= pos[0] <= next_button_x + next_button_width and next_button_y <= pos[1] <= next_button_y + next_button_height

################### helper functions ######################
def get_flavour():
    global selected_flavour

    if option_button1.collidepoint(event.pos):
        selected_flavour = flavours["classic"]
        click_sound.play()
    elif option_button2.collidepoint(event.pos):
        selected_flavour = flavours["matcha"]
        click_sound.play()
    elif option_button3.collidepoint(event.pos):
        selected_flavour = flavours["berry"]
        click_sound.play()
    elif option_button4.collidepoint(event.pos):
        selected_flavour = flavours["mango"]
        click_sound.play()
    elif option_button5.collidepoint(event.pos):
        selected_flavour = flavours["oreo"]
        click_sound.play()
    elif option_button6.collidepoint(event.pos):
        selected_flavour = flavours["taro"]
        click_sound.play()

    return selected_flavour

def get_ice():
    global selected_ice

    if option_button1.collidepoint(event.pos):
        selected_ice = ices["0%"]
        click_sound.play()
    elif option_button2.collidepoint(event.pos):
        selected_ice = ices["25%"]
        click_sound.play()
    elif option_button3.collidepoint(event.pos):
        selected_ice = ices["50%"]
        click_sound.play()
    elif option_button4.collidepoint(event.pos):
        selected_ice = ices["75%"]
        click_sound.play()
    elif option_button5.collidepoint(event.pos):
        selected_ice = ices["100%"]
        click_sound.play()
    elif option_button6.collidepoint(event.pos):
        selected_ice = ices["125%"]
        click_sound.play()

    return selected_ice

def get_sugar():
    global selected_sugar

    if option_button1.collidepoint(event.pos):
        selected_sugar = sugars["0%"]
        click_sound.play()
    elif option_button2.collidepoint(event.pos):
        selected_sugar = sugars["25%"]
        click_sound.play()
    elif option_button3.collidepoint(event.pos):
        selected_sugar = sugars["50%"]
        click_sound.play()
    elif option_button4.collidepoint(event.pos):
        selected_sugar = sugars["75%"]
        click_sound.play()
    elif option_button5.collidepoint(event.pos):
        selected_sugar = sugars["100%"]
        click_sound.play()
    elif option_button6.collidepoint(event.pos):
        selected_sugar = sugars["125%"]
        click_sound.play()

    return selected_sugar

def get_boba():
    global selected_boba

    if option_button1.collidepoint(event.pos):
        selected_boba = bobas["none"]
        click_sound.play()
    elif option_button2.collidepoint(event.pos):
        selected_boba = bobas["brown sugar"]
        click_sound.play()
    elif option_button3.collidepoint(event.pos):
        selected_boba = bobas["sago"]
        click_sound.play()
    elif option_button4.collidepoint(event.pos):
        selected_boba = bobas["fruit jelly"]
        click_sound.play()
    elif option_button5.collidepoint(event.pos):
        selected_boba = bobas["mango jelly"]
        click_sound.play()
    elif option_button6.collidepoint(event.pos):
        selected_boba = bobas["ube"]
        click_sound.play()

    return selected_boba

def get_topping():
    global selected_topping

    if option_button1.collidepoint(event.pos):
        selected_topping = toppings["shortcake"]
        click_sound.play()
    elif option_button2.collidepoint(event.pos):
        selected_topping = toppings["cookie bits"]
        click_sound.play()
    elif option_button3.collidepoint(event.pos):
        selected_topping = toppings["oreo pieces"]
        click_sound.play()
    elif option_button4.collidepoint(event.pos):
        selected_topping = toppings["mango"]
        click_sound.play()
    elif option_button5.collidepoint(event.pos):
        selected_topping = toppings["kiwi"]
        click_sound.play()
    elif option_button6.collidepoint(event.pos):
        selected_topping = toppings["sprinkles"]
        click_sound.play()
        
    return selected_topping

################## drawing boba ##################
def draw_boba_assembly():
    # Base cup is always visible
    screen.blit(cup_outline, (0, 0))

    # Draw in the correct order to simulate layering
    if selected_flavour:
        screen.blit(selected_flavour, (0, 0))  # Adjust coords if needed
    if selected_ice:
        screen.blit(selected_ice, (0, 0))
    if selected_sugar:
        screen.blit(selected_sugar, (0, 0))
    if selected_boba:
        screen.blit(selected_boba, (0, 0))
    if selected_topping:
        screen.blit(selected_topping, (0, 0))
    
    screen.blit(cup_outline, (0, 0))


############# states ###############
# game_state = "home"
pages = ["home", "page2", "page3", "page4", "mixing", "page5", "page6", "page7"]
current_page = 0


###################### Main loop #######################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if volume_button_rect.collidepoint(event.pos):
                music_on = not music_on
                if music_on:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

            # START button on home page
            if pages[current_page] == "home" and handle_button_click(event.pos):
                click_sound.play()  # Play click sound
                current_page = 1

            # Navigation
            elif handle_back_button_click(event.pos):
                click_sound.play()  # Play click sound
                if current_page > 0:
                    current_page -= 1

            elif handle_next_button_click(event.pos):
                click_sound.play()  # Play click sound
                if current_page < len(pages) - 1:
                    current_page += 1

            elif pages[current_page] == "page2":
                get_flavour()  # <--- Move it here

            elif pages[current_page] == "page3":
                get_ice()  # <--- Move it here

            elif pages[current_page] == "page4":
                get_sugar()

            elif pages[current_page] == "page5":
                get_boba()

            elif pages[current_page] == "page6":
                get_topping()

    # Background & Titles
    screen.fill(WHITE)
    # screen.blit(background, (0, 0))

    # Page handling
    if pages[current_page] == "home":
        screen.blit(background_image, (0, 0))
        screen.blit(title_line1, title_line1_rect)
        screen.blit(title_line2, title_line2_rect)
        draw_home_button()

    elif pages[current_page] == "page2":
        draw_back_button()
        draw_next_button()
        draw_option_buttons("classic", "matcha", "berry", "mango", "oreo", "taro")
        screen.blit(page2_line1_title, page2_line1_title_rect)
        screen.blit(page2_line2_title, page2_line2_title_rect)
        draw_boba_assembly()
        

    elif pages[current_page] == "page3":
        draw_back_button()
        draw_next_button()
        draw_option_buttons("0%", "25%", "50%", "75%", "100%", "125%")
        screen.blit(page3_line1_title, page3_line1_title_rect)
        screen.blit(page3_line2_title, page3_line2_title_rect)
        draw_boba_assembly()

    elif pages[current_page] == "page4":
        draw_back_button()
        draw_next_button()
        draw_option_buttons("0%", "25%", "50%", "75%", "100%", "125%")
        screen.blit(page4_line1_title, page4_line1_title_rect)
        screen.blit(page4_line2_title, page4_line2_title_rect)
        draw_boba_assembly()

    elif pages[current_page] == "mixing": 
        if current_music != "sounds/special.mp3":
            previous_music = current_music
            play_music("sounds/special.mp3", loop=False)

        draw_boba_assembly()
        screen.blit(mixing_img, (0, 0))
        draw_back_button()
        draw_next_button()


    elif pages[current_page] == "page5":
        if previous_music and current_music != previous_music:
            play_music(previous_music)
            previous_music = None

        selected_sugar = None
        selected_ice = None
        # screen.blit(frosting_background, (0, 0))
        draw_back_button()
        draw_next_button()
        draw_option_buttons("none", "brown sugar", "sago", "fruit jelly", "mango jelly", "ube")
        screen.blit(page5_line1_title, page5_line1_title_rect)
        screen.blit(page5_line2_title, page5_line2_title_rect)
        draw_boba_assembly()

    elif pages[current_page] == "page6":
        selected_sugar = None
        selected_ice = None
        # screen.blit(frosting_background, (0, 0))
        draw_back_button()
        draw_next_button()
        draw_option_buttons("shortcake", "cookie bits", "oreo pieces", "mango", "kiwi", "sprinkles")
        screen.blit(page6_line1_title, page6_line1_title_rect)
        screen.blit(page6_line2_title, page6_line2_title_rect)
        draw_boba_assembly()

    elif pages[current_page] == "page7":
        selected_sugar = None
        selected_ice = None
        screen.blit(frosting_background, (0, 0))
        # pygame.draw.rect(screen, LIGHT_BLUE, page7_line1_bg_rect, border_radius=10)
        # pygame.draw.rect(screen, LIGHT_BLUE, page7_line2_bg_rect, border_radius=10)

        draw_back_button()
        screen.blit(page7_line1_title, page7_line1_title_rect)
        screen.blit(page7_line2_title, page7_line2_title_rect)

        draw_boba_assembly()

        # Play tada sound once and resume background music
        if not tada_played:
            pygame.mixer.music.stop()
            tada_sound.play()
            tada_played = True
            pygame.time.set_timer(pygame.USEREVENT, int(tada_sound.get_length() * 550))  # Set timer for sound duration

        # Resume background music after tada sound
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                play_music(current_music)
                pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer

        

    draw_volume_button()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()


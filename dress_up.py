from drafter import *
from bakery import assert_equal
from dataclasses import dataclass

add_website_css("body", "background-color: lightpink;" "text-align: center;")
set_website_style("skeleton")



@dataclass
class OutfitItem:
    name: str
    category: str
    image_url: Image

@dataclass
class State:
    outfit_choices: list[OutfitItem]
    outfit_completed: bool
    theme: str
    name : str

@route
def index(state: State) -> Page:
    """
    The main page of the dress-up game, letting the player enter their name and start the game.

    Args:
        state (State): The initial state of the game.

    Returns:
        Page: The main page displaying a welcome message, text box for the player's name, and a start button.
    """
    text = ("Wardrobe Wearhouse! Enter your name and press start to begin!")
    text_box = TextBox("name")
    button = Button("Start", url="/wardrobe",style_color="black", background_color='thistle')
    return Page(state, [text, text_box,button])

@route
def wardrobe(state: State, name: str) -> Page:
    """
    The wardrobe page to select outfit categories like tops, bottoms, shoes, and accessories.

    Args:
        state (State): The current state of the game.
        name (str): The player's name.

    Returns:
        Page: The wardrobe page with buttons to navigate each outfit category.
    """
    state.name = name
    text = "Hello " + state.name + " please choose an outfit category and have fun dressing up!"
    button_tops = Button("🧥 Tops", url="/tops", style_color="black", background_color='deepPink')
    button_bottoms = Button("👖 Bottoms", url="/bottoms", style_color="black", background_color='hotpink')
    button_shoes = Button("👟 Shoes", url="/shoes", style_color="black", background_color='mediumvioletred')
    button_accessories = Button("🕶 Accessories", url="/accessories", style_color="black", background_color='palevioletred')
    button_preview = Button("All Chosen!☺", url = "/preview", style_color="black", background_color='plum')
    
    return Page(state, [text, button_tops, button_bottoms, button_shoes, button_accessories, button_preview])


@route
def tops(state: State) -> Page:
    """
    The page for selecting a top item from the dropdown menu.

    Args:
        state (State): The current state of the game.

    Returns:
        Page: The tops selection page with dropdown options and images of options.
    """
    select_box = SelectBox("clothing_choice", ["Tee", "Tank Top", "Long Sleeve"], " ")    
    text = "Select an item from the dropdown and press wardrobe when you're done!"
    image1 = Image("tee.jpg", 115, 155)
    image2 = Image("tank.webp", 115, 155)
    image3 = Image("long.jpg", 115, 155)

        
    button_next = Button("Wardrobe", url="/update_tops", style_color="black", background_color='lavenderblush')
    return Page(state, [text, select_box, image1, image2, image3,button_next])

@route
def update_tops(state:State, clothing_choice:str) -> Page:
    """
    Updates the state with the selected top item and redirects to the wardrobe.

    Args:
        state (State): The current state of the game.
        clothing_choice (str): The selected clothing option.

    Returns:
        Page: The updated wardrobe page or preview page if all outfit categories are completed.
    """
    category = "Top"
    
    already_added = False
    for item in state.outfit_choices:
        if item.category == category:
            already_added = True
            
    if not already_added:
        if clothing_choice == "Tee":
            state.outfit_choices.append(OutfitItem("Tee", "Top", Image("tee.jpg", 100, 100) ))
        elif clothing_choice == "Tank Top":
            state.outfit_choices.append(OutfitItem("Tank Top", "Top", Image("tank.webp", 100, 100)))
        elif clothing_choice == "Long Sleeve":
            state.outfit_choices.append(OutfitItem("Long Sleeve", "Top", Image("long.jpg", 100, 100)))
        
    if len(state.outfit_choices) == 4:
        return preview(state)
        
            
    return wardrobe(state, state.name)
    
@route
def bottoms(state: State) -> Page:
    """
    The page for selecting a bottoms item from the dropdown menu.

    Args:
        state (State): The current state of the game.

    Returns:
        Page: The bottoms selection page with dropdown options and images of options.
    """
    text = "Select an item from the dropdown and press wardrobe when you're done!"
    select_box = SelectBox("clothing_choice", ["Shorts", "Skirt", "Pants"], " ")
    image1 = Image("shorts.webp", 115, 155)
    image2 = Image("skirt.jpg", 115, 155)
    image3 = Image("pants.jpg", 115, 155)
    
    button_next = Button("Wardrobe", url="/update_bottoms", style_color="black", background_color='lavenderblush')
    return Page(state, [text, select_box, image1, image2, image3, button_next])

@route
def update_bottoms(state: State, clothing_choice: str) -> Page:
    """
    Updates the state with the selected bottoms item and redirects to the wardrobe.

    Args:
        state (State): The current state of the game.
        clothing_choice (str): The selected clothing option.

    Returns:
        Page: The updated wardrobe page or preview page if all outfit categories are completed.
    """
    category = "Bottoms"
    
    already_added = False
    for item in state.outfit_choices:
        if item.category == category:
            already_added = True
            
    if not already_added:
        if clothing_choice == "Shorts":
            state.outfit_choices.append(OutfitItem("Shorts", "Bottoms", Image("shorts.webp", 100, 100)))
        elif clothing_choice == "Skirt":
            state.outfit_choices.append(OutfitItem("Skirt", "Bottoms", Image("skirt.jpg", 100, 100)))
        elif clothing_choice == "Pants":
            state.outfit_choices.append(OutfitItem("Pants", "Bottoms", Image("pants.jpg", 100, 100)))
        
    if len(state.outfit_choices) == 4:
        return preview(state)
        

    return wardrobe(state, state.name)
            
    

@route
def shoes(state: State) -> Page:
    """
    The page for selecting a shoes item from the dropdown menu.

    Args:
        state (State): The current state of the game.

    Returns:
        Page: The shoes selection page with dropdown options and images of options.
    """
    text = "Select an item from the dropdown and press wardrobe when you're done!"
    select_box = SelectBox("clothing_choice", ["Sneakers", "Sandals", "Boots"], " ")
    image1 = Image("sneakers.png", 115, 155)
    image2 = Image("sandals.jpg", 115, 155)
    image3 = Image("boots.webp", 115, 155)
    
    button_next = Button("Wardrobe", url="/update_shoes", style_color="black", background_color='lavenderblush')
    
    return Page(state, [text, select_box, image1, image2, image3, button_next])

@route
def update_shoes(state: State, clothing_choice: str) -> Page:
    """
    Updates the state with the selected shoes item and redirects to the wardrobe.

    Args:
        state (State): The current state of the game.
        clothing_choice (str): The selected clothing option.

    Returns:
        Page: The updated wardrobe page or preview page if all outfit categories are completed.
    """
    category = "Shoes"
    
    already_added = False
    for item in state.outfit_choices:
        if item.category == category:
            already_added = True
    
    if not already_added:
        if clothing_choice == "Sneakers":
            state.outfit_choices.append(OutfitItem("Sneakers", "Shoes", Image("sneakers.png", 100, 100)))
        elif clothing_choice == "Sandals":
            state.outfit_choices.append(OutfitItem("Sandals", "Shoes", Image("sandals.jpg", 100, 100)))
        elif clothing_choice == "Boots":
            state.outfit_choices.append(OutfitItem("Boots", "Shoes", Image("boots.webp", 100, 100)))
        
    if len(state.outfit_choices) == 4:
        return preview(state)
    
    return wardrobe(state, state.name)

    

@route
def accessories(state: State) -> Page:
    """
    The page for selecting an accessories item from the dropdown menu.

    Args:
        state (State): The current state of the game.

    Returns:
        Page: The accessories selection page with dropdown options and related images.
    """
    text = "Select an item from the dropdown!"
    select_box = SelectBox("clothing_choice", ["Necklace", "Hat", "Sunglasses"], " ")
    image1 = Image("neck.webp", 115, 155)
    image2 = Image("hat.webp", 115, 155)
    image3 = Image("glasses.webp", 115, 155)
    
    button_next = Button("Wardrobe", url="/update_accessories", style_color="black", background_color='lavenderblush')
    
    return Page(state, [text, select_box, image1, image2, image3, button_next])

@route
def update_accessories(state: State, clothing_choice: str) -> Page:
    """
    Updates the state with the selected accessories item and redirects to the wardrobe.

    Args:
        state (State): The current state of the game.
        clothing_choice (str): The selected clothing option.

    Returns:
        Page: The updated wardrobe page or preview page if all outfit categories are completed.
    """
    category = "Accessories"
    
    already_added = False
    for item in state.outfit_choices:
        if item.category == category:
            already_added = True
            
    
    if not already_added: 
        if clothing_choice == "Necklace":
            state.outfit_choices.append(OutfitItem("Necklace", "Accessories", Image("neck.webp", 100, 100)))
        elif clothing_choice == "Hat":
            state.outfit_choices.append(OutfitItem("Hat", "Accessories", Image("hat.webp", 100, 100)))
        elif clothing_choice == "Sunglasses":
            state.outfit_choices.append(OutfitItem("Sunglasses", "Accessories", Image("glasses.webp", 100, 100)))
    
    if len(state.outfit_choices) == 4:
        return preview(state)
        
    
    return wardrobe(state, state.name)
    

def check_outfit_completed(state: State) -> bool:
    """
    Checks if the player has selected an item from each outfit category.

    Args:
        state (State): The current state of the game.

    Returns:
        bool: True if all categories are completed, False otherwise.
    """
    categories = ["Top", "Bottoms", "Shoes", "Accessories"]

    for category in categories:
        selected = False
        for item in state.outfit_choices:
            if item.category == category:
                selected = True

        if not selected:
            state.outfit_completed = False
            return state.outfit_completed

    state.outfit_completed = True
    return state.outfit_completed


@route
def preview(state: State) -> Page:
    """
    Displays a preview determining whether the outfit is complete or not.

    Args:
        state (State): The current state of the game.

    Returns:
        Page: The preview page with the completed outfit or a message to return to the wardrobe.
    """
    value = check_outfit_completed(state)
    if value:
        button_next = Button("Finished ➡", url="/final", style_color="black", background_color='lavender')
        image = Image("heyes.jpg", 200, 200)
        text = "Your outfit looks stunning! Great job!"
        return Page(state, [ text, image, button_next])

    else:
        wardrobee = Button("Wardrobe", url = "/preview_to_wardrobe", style_color="black", background_color='lavenderblush')
        image = Image("sad.jpg", 200, 200)
        text2 = "You are missing a few things. Please go back to the wardrobe and complete your outfit."
        return Page(state, [text2, image, wardrobee])
    
@route
def preview_to_wardrobe(state: State) -> Page:
    """
    Redirects the player back to the wardrobe from the preview page.
    Cannot be unit tested.

    Args:
        state (State): The current state of the game.

    Returns:
        Page: The wardrobe page.
    """
    return wardrobe(state, state.name)
    
    
def theme(state: State) -> str:
    """
    Determines the theme of the outfit based on selected items.

    Args:
        state (State): The current state of the game.

    Returns:
        str: The theme of the outfit.
    """
    item_names = []
    for choice in state.outfit_choices:
        item_names.append(choice.name)

    if "Sandals" in item_names and "Sunglasses" in item_names:
        state.theme = "Summer Sunny"
    elif "Boots" in item_names and "Long Sleeve" in item_names:
        state.theme = "Winter Warmth"
    elif "Sneakers" in item_names and "Hat" in item_names:
        state.theme = "Casual Outdoorsy"
    else:
        state.theme = "Everyday Wear"
    
    return state.theme

def image(state: State) -> list:
    """
    Retrieves a list of images for the selected outfit items.

    Args:
        state (State): The current state of the game.

    Returns:
        list[Image]: A list of images for the outfit items.
    """
    images = []
    for element in state.outfit_choices:
        images.append(element.image_url)
    return images

def theme_image(state: State) -> Image:
    """
    Determines the image theme based on selected outfit items.

    Args:
        state (State): The current state of the game.

    Returns:
        Image: The image representing the outfit's theme.
    """
    item_names = []
    for choice in state.outfit_choices:
        item_names.append(choice.name)

    if "Sandals" in item_names and "Sunglasses" in item_names:
        image = Image("sun.avif", 959, 300)
    elif "Boots" in item_names and "Long Sleeve" in item_names:
        image = Image("winter.jpeg", 959, 300)
    elif "Sneakers" in item_names and "Hat" in item_names:
        image = Image("out.jpg", 959, 300)
    else:
        image = Image("sunr.jpg", 959, 300)
    
    return image
    

@route
def final(state: State) -> Page:
    """
    Displays the final page with the completed outfit and theme.

    Args:
        state (State): The current state of the game.

    Returns:
        Page: The final page with outfit images and theme message.
    """
    pics = image(state)
    page_list= ["OMG " + state.name.upper() + " I LOVE THIS!!!! The " +
                theme(state) + " vibe you're going for is so cute!",
                theme_image(state),
                "Take a look at the BEAUTIFUL outfit you've come up with!"]
    return Page(state, page_list+ image(state))


#assert_equal tests below
assert_equal(
 update_shoes(State(outfit_choices=[OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)), OutfitItem(name='Pants', category='Bottoms', image_url=Image(url='pants.jpg', width=100, height=100))], outfit_completed=False, theme='', name='Aiman'), 'Sandals'),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100)),
                                 OutfitItem(name='Pants',
                                            category='Bottoms',
                                            image_url=Image(url='pants.jpg', width=100, height=100)),
                                 OutfitItem(name='Sandals',
                                            category='Shoes',
                                            image_url=Image(url='sandals.jpg', width=100, height=100))],
                 outfit_completed=False,
                 theme='',
                 name='Aiman'),
     content=['Hello Aiman please choose an outfit category and have fun dressing up!',
              Button(text='🧥 Tops', url='/tops'),
              Button(text='👖 Bottoms', url='/bottoms'),
              Button(text='👟 Shoes', url='/shoes'),
              Button(text='🕶 Accessories', url='/accessories'),
              Button(text='All Chosen!☺', url='/preview')]))

assert_equal(
 bottoms(State(outfit_choices=[OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100))], outfit_completed=False, theme='', name='Aiman')),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100))],
                 outfit_completed=False,
                 theme='',
                 name='Aiman'),
     content=["Select an item from the dropdown and press wardrobe when you're done!",
              SelectBox(name='clothing_choice', options=['Shorts', 'Skirt', 'Pants'], default_value=' '),
              Image(url='shorts.webp', width=115, height=155),
              Image(url='skirt.jpg', width=115, height=155),
              Image(url='pants.jpg', width=115, height=155),
              Button(text='Wardrobe', url='/update_bottoms')]))

assert_equal(
 final(State(outfit_choices=[OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)), OutfitItem(name='Pants', category='Bottoms', image_url=Image(url='pants.jpg', width=100, height=100)), OutfitItem(name='Sandals', category='Shoes', image_url=Image(url='sandals.jpg', width=100, height=100)), OutfitItem(name='Necklace', category='Accessories', image_url=Image(url='neck.webp', width=100, height=100))], outfit_completed=True, theme='', name='Aiman')),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100)),
                                 OutfitItem(name='Pants',
                                            category='Bottoms',
                                            image_url=Image(url='pants.jpg', width=100, height=100)),
                                 OutfitItem(name='Sandals',
                                            category='Shoes',
                                            image_url=Image(url='sandals.jpg', width=100, height=100)),
                                 OutfitItem(name='Necklace',
                                            category='Accessories',
                                            image_url=Image(url='neck.webp', width=100, height=100))],
                 outfit_completed=True,
                 theme='Everyday Wear',
                 name='Aiman'),
     content=["OMG AIMAN I LOVE THIS!!!! The Everyday Wear vibe you're going for is so cute!",
              Image(url='sunr.jpg', width=959, height=300),
              "Take a look at the BEAUTIFUL outfit you've come up with!",
              Image(url='tank.webp', width=100, height=100),
              Image(url='pants.jpg', width=100, height=100),
              Image(url='sandals.jpg', width=100, height=100),
              Image(url='neck.webp', width=100, height=100)]))

assert_equal(
 index(State(outfit_choices=[], outfit_completed=False, theme='', name='')),
 Page(state=State(outfit_choices=[], outfit_completed=False, theme='', name=''),
     content=['Wardrobe Wearhouse! Enter your name and press start to begin!',
              TextBox(name='name', kind='text', default_value=''),
              Button(text='Start', url='/wardrobe')]))

assert_equal(
 update_accessories(State(outfit_choices=[OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)), OutfitItem(name='Pants', category='Bottoms', image_url=Image(url='pants.jpg', width=100, height=100)), OutfitItem(name='Sandals', category='Shoes', image_url=Image(url='sandals.jpg', width=100, height=100))], outfit_completed=False, theme='', name='Aiman'), 'Necklace'),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100)),
                                 OutfitItem(name='Pants',
                                            category='Bottoms',
                                            image_url=Image(url='pants.jpg', width=100, height=100)),
                                 OutfitItem(name='Sandals',
                                            category='Shoes',
                                            image_url=Image(url='sandals.jpg', width=100, height=100)),
                                 OutfitItem(name='Necklace',
                                            category='Accessories',
                                            image_url=Image(url='neck.webp', width=100, height=100))],
                 outfit_completed=True,
                 theme='',
                 name='Aiman'),
     content=['Your outfit looks stunning! Great job!',
              Image(url='heyes.jpg', width=200, height=200),
              Button(text='Finished ➡', url='/final')]))

assert_equal(
 shoes(State(outfit_choices=[OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)), OutfitItem(name='Pants', category='Bottoms', image_url=Image(url='pants.jpg', width=100, height=100))], outfit_completed=False, theme='', name='Aiman')),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100)),
                                 OutfitItem(name='Pants',
                                            category='Bottoms',
                                            image_url=Image(url='pants.jpg', width=100, height=100))],
                 outfit_completed=False,
                 theme='',
                 name='Aiman'),
     content=["Select an item from the dropdown and press wardrobe when you're done!",
              SelectBox(name='clothing_choice', options=['Sneakers', 'Sandals', 'Boots'], default_value=' '),
              Image(url='sneakers.png', width=115, height=155),
              Image(url='sandals.jpg', width=115, height=155),
              Image(url='boots.webp', width=115, height=155),
              Button(text='Wardrobe', url='/update_shoes')]))

assert_equal(
 update_tops(State(outfit_choices=[], outfit_completed=False, theme='', name='Aiman'), 'Tank Top'),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100))],
                 outfit_completed=False,
                 theme='',
                 name='Aiman'),
     content=['Hello Aiman please choose an outfit category and have fun dressing up!',
              Button(text='🧥 Tops', url='/tops'),
              Button(text='👖 Bottoms', url='/bottoms'),
              Button(text='👟 Shoes', url='/shoes'),
              Button(text='🕶 Accessories', url='/accessories'),
              Button(text='All Chosen!☺', url='/preview')]))

assert_equal(
 update_bottoms(State(outfit_choices=[OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100))], outfit_completed=False, theme='', name='Aiman'), 'Pants'),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100)),
                                 OutfitItem(name='Pants',
                                            category='Bottoms',
                                            image_url=Image(url='pants.jpg', width=100, height=100))],
                 outfit_completed=False,
                 theme='',
                 name='Aiman'),
     content=['Hello Aiman please choose an outfit category and have fun dressing up!',
              Button(text='🧥 Tops', url='/tops'),
              Button(text='👖 Bottoms', url='/bottoms'),
              Button(text='👟 Shoes', url='/shoes'),
              Button(text='🕶 Accessories', url='/accessories'),
              Button(text='All Chosen!☺', url='/preview')]))

assert_equal(
 wardrobe(State(outfit_choices=[], outfit_completed=False, theme='', name=''), 'Aiman'),
 Page(state=State(outfit_choices=[], outfit_completed=False, theme='', name='Aiman'),
     content=['Hello Aiman please choose an outfit category and have fun dressing up!',
              Button(text='🧥 Tops', url='/tops'),
              Button(text='👖 Bottoms', url='/bottoms'),
              Button(text='👟 Shoes', url='/shoes'),
              Button(text='🕶 Accessories', url='/accessories'),
              Button(text='All Chosen!☺', url='/preview')]))

assert_equal(
 accessories(State(outfit_choices=[OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)), OutfitItem(name='Pants', category='Bottoms', image_url=Image(url='pants.jpg', width=100, height=100)), OutfitItem(name='Sandals', category='Shoes', image_url=Image(url='sandals.jpg', width=100, height=100))], outfit_completed=False, theme='', name='Aiman')),
 Page(state=State(outfit_choices=[OutfitItem(name='Tank Top',
                                            category='Top',
                                            image_url=Image(url='tank.webp', width=100, height=100)),
                                 OutfitItem(name='Pants',
                                            category='Bottoms',
                                            image_url=Image(url='pants.jpg', width=100, height=100)),
                                 OutfitItem(name='Sandals',
                                            category='Shoes',
                                            image_url=Image(url='sandals.jpg', width=100, height=100))],
                 outfit_completed=False,
                 theme='',
                 name='Aiman'),
     content=['Select an item from the dropdown!',
              SelectBox(name='clothing_choice', options=['Necklace', 'Hat', 'Sunglasses'], default_value=' '),
              Image(url='neck.webp', width=115, height=155),
              Image(url='hat.webp', width=115, height=155),
              Image(url='glasses.webp', width=115, height=155),
              Button(text='Wardrobe', url='/update_accessories')]))

assert_equal(
 tops(State(outfit_choices=[], outfit_completed=False, theme='', name='Aiman')),
 Page(state=State(outfit_choices=[], outfit_completed=False, theme='', name='Aiman'),
     content=["Select an item from the dropdown and press wardrobe when you're done!",
              SelectBox(name='clothing_choice', options=['Tee', 'Tank Top', 'Long Sleeve'], default_value=' '),
              Image(url='tee.jpg', width=115, height=155),
              Image(url='tank.webp', width=115, height=155),
              Image(url='long.jpg', width=115, height=155),
              Button(text='Wardrobe', url='/update_tops')]))

assert_equal(
    check_outfit_completed(State(outfit_choices=[
        OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)),
        OutfitItem(name='Jeans', category='Bottoms', image_url=Image(url='jeans.jpg', width=100, height=100)),
        OutfitItem(name='Sneakers', category='Shoes', image_url=Image(url='sneakers.jpg', width=100, height=100)),
        OutfitItem(name='Watch', category='Accessories', image_url=Image(url='watch.jpg', width=100, height=100))
    ], outfit_completed=False, theme='', name='Aiman')),
    True
)

assert_equal(
    preview(State(outfit_choices=[
        OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)),
        OutfitItem(name='Jeans', category='Bottoms', image_url=Image(url='jeans.jpg', width=100, height=100)),
        OutfitItem(name='Sneakers', category='Shoes', image_url=Image(url='sneakers.jpg', width=100, height=100)),
        OutfitItem(name='Watch', category='Accessories', image_url=Image(url='watch.jpg', width=100, height=100))
    ], outfit_completed=False, theme='', name='Aiman')),
    Page(
        state=State(outfit_choices=[
            OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)),
            OutfitItem(name='Jeans', category='Bottoms', image_url=Image(url='jeans.jpg', width=100, height=100)),
            OutfitItem(name='Sneakers', category='Shoes', image_url=Image(url='sneakers.jpg', width=100, height=100)),
            OutfitItem(name='Watch', category='Accessories', image_url=Image(url='watch.jpg', width=100, height=100))
        ], outfit_completed=True, theme='', name='Aiman'),
        content=["Your outfit looks stunning! Great job!", 
                 Image(url='heyes.jpg', width=200, height=200),
                 Button(text="Finished ➡", url="/final")]
    )
)

assert_equal(theme(State(outfit_choices=[OutfitItem(name='Boots', category='Shoes', image_url=Image(url='boots.jpg', width=100, height=100)),
                                 OutfitItem(name='Long Sleeve', category='Top', image_url=Image(url='longsleeve.jpg', width=100, height=100))], outfit_completed=True, theme='', name='Aiman')), "Winter Warmth")

state = State(
    outfit_choices=[OutfitItem("Sneakers", "Shoes", Image("sneakers.png", 115, 155))],
    outfit_completed=False,
    theme="",
    name="Aiman"
)

assert_equal(
    image(state),
    [Image("sneakers.png", 115, 155)]
)


state = State(
    outfit_choices=[
        OutfitItem("Sandals", "Shoes", Image("sandals.jpg", 115, 155)),
        OutfitItem("Sunglasses", "Accessories", Image("glasses.webp", 115, 155))
    ],
    outfit_completed=False,
    theme="",
    name="Aiman"
)
assert_equal(
    theme_image(state),
    Image("sun.avif", 959, 300)
)

assert_equal(
    wardrobe(State(outfit_choices=[], outfit_completed=False, theme='', name=''), name = ''),
    Page(
        state=State(outfit_choices=[], outfit_completed=False, theme='', name=''),
        content=[
            'Hello  please choose an outfit category and have fun dressing up!',
            Button(text='🧥 Tops', url='/tops'),
            Button(text='👖 Bottoms', url='/bottoms'),
            Button(text='👟 Shoes', url='/shoes'),
            Button(text='🕶 Accessories', url='/accessories'),
            Button(text='All Chosen!☺', url='/preview')
        ]
    )
)

assert_equal(
    preview(State(outfit_choices=[
        OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)),
        OutfitItem(name='Shorts', category='Bottoms', image_url=Image(url='shorts.webp', width=100, height=100))
    ], outfit_completed=False, theme='', name='Aiman')),
    Page(
        state=State(outfit_choices=[
            OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)),
            OutfitItem(name='Shorts', category='Bottoms', image_url=Image(url='shorts.webp', width=100, height=100))
        ], outfit_completed=False, theme='', name='Aiman'),
        content=[
            "You are missing a few things. Please go back to the wardrobe and complete your outfit.",
            Image(url='sad.jpg', width=200, height=200),
            Button(text="Wardrobe", url="/preview_to_wardrobe")
        ]
    )
)

assert_equal(
    check_outfit_completed(State(outfit_choices=[
        OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100))
    ], outfit_completed=False, theme='', name='')),
    False
)

assert_equal(
    check_outfit_completed(State(outfit_choices=[
        OutfitItem(name='Tank Top', category='Top', image_url=Image(url='tank.webp', width=100, height=100)),
        OutfitItem(name='Shorts', category='Bottoms', image_url=Image(url='shorts.webp', width=100, height=100)),
        OutfitItem(name='Sneakers', category='Shoes', image_url=Image(url='sneakers.png', width=100, height=100)),
        OutfitItem(name='Hat', category='Accessories', image_url=Image(url='hat.webp', width=100, height=100))
    ], outfit_completed=False, theme='', name='')),
    True
)

start_server(State(outfit_choices=[], outfit_completed=False, theme="", name = ""))
default card_amount = 12
default card_rows = 3
default cards = []
default selected_cards = []
default hidden_cards = 0
default match_found = False


init python:

    def randomize_cards():
        global cards
        cards = []
        for i in range(int(card_amount / 2)):
            rand_card_num = renpy.random.randint(1, 8)
            cards.append(["card-%s" % rand_card_num, "deselected", "visible"])
            cards.append(["card-%s" % rand_card_num, "deselected", "visible"])
        renpy.random.shuffle(cards)

    def select_card(card_index):
        global selected_cards
        global match_found

        cards[card_index][1] = "selected"
        selected_cards.append(card_index)

        if len(selected_cards) == 2 and cards[selected_cards[0]][0] == cards[selected_cards[1]][0]:
            match_found = True

    def deselect_card():
        global selected_cards

        if len(selected_cards) == 2:
            for card in selected_cards:
                cards[card][1] = "deselected"
        selected_cards = []

    def hide_matches():
        global selected_cards
        global match_found
        global hidden_cards

        cards[selected_cards[0]][2] = "hidden"
        cards[selected_cards[1]][2] = "hidden"
        hidden_cards += 2
        deselect_card()
        match_found = False

    def reset_memory_game():
        global match_found
        global hidden_cards

        match_found = False
        hidden_cards = 0
        randomize_cards()

transform card_fadein:
    alpha 0.0
    easein 0.5 alpha 1.0
    
screen memory_mini_game:
    image "mini_game_BK.png"
    grid int(card_amount / card_rows) card_rows:
        align (0.5, 0.5)
        spacing 10
        
        for i, card in enumerate(cards):    
            if card[1] == "deselected" and card[2] == "visible":
                imagebutton idle "card-back.png"  sensitive (len(selected_cards) != 2) action Function(select_card, card_index=i) at card_fadein 
            elif card[1] == "selected" and card[2] == "visible":
                image "%s.png" % card[0] at card_fadein
            else:
                null

    if match_found:
        timer 1.0 action Function(hide_matches) repeat True
    elif len(selected_cards) == 2:
        timer 1.0 action Function(deselect_card) repeat True
    elif hidden_cards == card_amount:
        timer 0.5 action Function(reset_memory_game) repeat False
    

label mini_game:
    $ randomize_cards()
    call screen memory_mini_game
    return

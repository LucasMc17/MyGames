'''
v.1: capable of playing all standard hands, recognizing naturals and changing value of ace hands.
v.2: can recognize splits chances and ask player to split, can split hand to two new lists and print table, but can't
play the hand out yet.
v.3: hand splitting is fully functional. Terminology is changed, y for yes, n for no, etc. print table function
condensed. lose and win replaced with end. Fixed bug with reshuffle process.
v.4: Doubling down is functional. print table flips dealer's second card if he has blackjack.
v.5: Insurance is functional.
v.6: Insurance checks against chips remaining, pays 2:1 and displays on table. Fully functional. changed bj payout
v.7: added intro screen
v.8: tied hands now push the bet back to you. includes split hands, double downs and double blackjacks. Money now
formats to dollars and cents.
v.9: Added rules. Fixed a potential error with insurance bets.
still to do: add time delay before dealer's play
'''

import time

import random

p_s_hand1 = []
p_s_hand2 = []
play_again = True
pot = 0
p_chips = 50.00
deck_i = 0
deck = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, "X", "X", "X", "X", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
point_values = {
    "A": 1,
    "J": 10,
    "Q": 10,
    "K": 10,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    "X": 10
}


def rules_q():
    valid_choice = False
    while not valid_choice:
        choice = input("Would you like to review the rules? Enter 'y' for yes or 'n' for no: ").upper()
        if choice == "Y" or choice == "N":
            valid_choice = True
        else:
            print("Invalid input.")
    return choice


def rules(rules_q):
    if rules_q == "Y":
        print("")
        print("OVERVIEW: In Blackjack, players try to beat the dealer's hand with their own. The object of the game is")
        print("to get as close to the number 21 as possible, without going over, or \"busting.\" A player wins when")
        print("their hand is higher than the dealer's, or if the dealer busts.")
        print("CARD VALUES: In Blackjack, face cards, such as Jacks, Queens and Kings, are all ten points. Aces are")
        print("either one or eleven points, depending on whether the higher point value would cause the player to")
        print("bust. All other cards are equal to their pip value. In this game, a ten card will appear as an \"X.\"")
        print("THE PLAY: First, every player bets however much they wish. At the start of every hand, the dealer will")
        print("first deal one face-up card to you, then one to himself, then another to you, and finally one face-down")
        print("card to himself. During your turn, you will be asked to either \"hit\" or \"stand.\" Hitting means")
        print("requesting an additional card to increase the total value of your hand. Standing means opting to leave")
        print("your hand as is, effectively ending your turn. If a player's hand is worth more than 21, they bust, and")
        print("lose their bet. After all players have decided to stand or have bust, it is the dealer's turn. They")
        print("begin by flipping their face-down card. Where the player always decides whether to hit or stand, the")
        print("dealer must always hit if the total value of their current hand is less than 17, and must stand once")
        print("their hand is worth 17 or more. If the dealer busts, all players who did not bust during their turn win")
        print("their bets. If the dealer does not bust, all players who did not bust have their hands compared to the")
        print("dealer's. Those with higher hands win their bets, those with lower hands lose, and those whose hands")
        print("tie the dealer's have their bets returned to them.")
        print("BLACKJACK: If any player draws an Ace and any card with a value of ten at the start of a hand, they")
        print("\"blackjack,\" a special hand. If the dealer has blackjack, all players who do not also have blackjack")
        print("lose the hand immediately. If a player has blackjack and the dealer does not, that player immediately")
        print("wins 1.5 times their bet. If a player and the dealer both have blackjack, it is a push, and the")
        print("player's bet is returned to them. If the dealer's face-up card is an Ace or any card with a value of")
        print("ten, they must check their face-down card to confirm whether or not they have blackjack before play can")
        print("begin.")
        print("FIVE-CARD CHARLIE: If any player hits three times without busting so that their hand totals five cards,")
        print("they will immediately win 1.5 times their bet. Note that the dealer cannot win by five-card Charlie,")
        print("and neither can the hand be achieved during a split hand.")
        print("SPLIT: If a player's starting hand consists of two cards of the same type, (two fives, two aces, two")
        print("kings, etc.) they may choose to split their hand, playing each card as a separate hand. Splitting a")
        print("hand requires placing an additional bet on the second hand, equal to the initial bet placed on the")
        print("first hand. Players may hit each hand as many times as they please, and each hand's bet is settled")
        print("separately at the end of the round. If a player opts to split a pair of Aces, they will receive only")
        print("hit on each hand.")
        print("DOUBLING DOWN: if a player's starting hand is equal to 9, 10, or 11, they will be given the option of")
        print("\"doubling down,\" doubling their bet and receiving one additional card for the hand. If a player's")
        print("starting hand is two fives, they have the choice of splitting, doubling down, or playing the hand")
        print("normally.")
        print("INSURANCE: If the dealer's face-up card is an Ace, players will have the opportunity to place insurance")
        print("bets of up to one half of their initial bet before the dealer checks for blackjack. Insurance bets pay")
        print("out 2:1 if the dealer has blackjack, but return nothing if the dealer does not have blackjack. In this")
        print("way, a player can negate their losses when the dealer has blackjack, if they place the maximum")
        print("insurance bet.")


def cent_rounder(amount):
    return "%.2f" % amount


def main_screen():
    print(" ______   ___            _____         ____   ___   ___       ___    _____         ____   ___   ___ ")
    print("|_   _ \ |  _|    ____  |_    \       / __ \ |   | |  _|     |  _|  |_    \       / __ \ |  _| |  _|")
    print("  | | \ \ | |    _L_  |   | |\ \     / /  \ \ | |  / /        | |     | |\ \     / /  \ \ | |  / /  ")
    print("  | |  | || |  _L_  | |  | |  | |   | /    | || | / /         | |    | |  | |   | /    | || | / /   ")
    print("  | |_/ / | | |   | |_| | |____| |  | |    |_|| |/ /          | |   | |____| |  | |    |_|| |/ /    ")
    print("  |  _ <  | | | A |_|   | ______ |  | |       |   <    ___    | |   | ______ |  | |       |   <     ")
    print("  | | \ \ | | |___|    | |      | | | |     _ | |\ \  |  _|   | |  | |      | | | |     _ | |\ \    ")
    print("  | |  | || |     _    | |      | | | \    | || | \ \  | |    | |  | |      | | | \    | || | \ \   ")
    print(" _| |_/ / | |____| | _| |       _| | \ \__/ / | |  \ \_ \ \__/ / _| |       _| | \ \__/ / | |  \ \_ ")
    print("|______/  |________||___|      |___|  \____/ |___| |___| \____/ |___|      |___|  \____/ |___| |___|")
    print("v.9                                    coded by Lucas McGill\n\n\n\n")


def shuffle():
    random.shuffle(deck)
    # print(deck)


def deal_d(deck, deck_i):
    d_hand = []
    d_hand.append(deck[deck_i + 1])
    d_hand.append(deck[deck_i + 3])
    return d_hand


def deal_p(deck, deck_i):
    p_hand = []
    p_hand.append(deck[deck_i])
    p_hand.append(deck[deck_i + 2])
    return p_hand


def bet(p_chips):
    valid_bet = False
    while not valid_bet:
        try:
            pot = float(input(f"Choose how much to bet on the next hand (minimum bet: $1.00): $"))
            if 1 <= pot <= p_chips:
                valid_bet = True
            else:
                print("Invalid bet.")
        except ValueError:
            print("Invalid bet.")
    return pot


def hit(hand, deck, deck_i):
    hand.append(deck[deck_i])
    return hand


def p_choice():
    valid_choice = False
    while not valid_choice:
        choice = input("Please enter 's' for stand or 'h' for hit: ").upper()
        if choice == "H" or choice == "S":
            valid_choice = True
        else:
            print("Invalid input.")
    return choice


def can_play():
    if p_chips > 1 and play_again:
        return True


def play_again_q():
    valid_choice = False
    while not valid_choice:
        choice = input("Would you like to play again? Please enter 'y' for yes or 'n' for no: ").upper()
        if choice == "Y" or choice == "N":
            valid_choice = True
        else:
            print("Invalid input.")
    return choice


def bj_detect(hand):
    if any(["J" in hand, "Q" in hand, "K" in hand, "X" in hand]) and "A" in hand:
        return True


def chip_pot_comp(pot, p_chips):
    if p_chips >= (pot / 2):
        return pot / 2
    else:
        return p_chips


def insurance_detect():
    valid_choice = False
    while not valid_choice:
        try:
            choice = float(input(f"Would you like to place an insurance bet? (up to ${cent_rounder(chip_pot_comp(pot, p_chips))}, enter '0' to place no bet): $"))
            if 0 <= choice <= (chip_pot_comp(pot, p_chips)):
                valid_choice = True
            else:
                print("Invalid bet.")
        except ValueError:
            print("Invalid bet.")
    return choice


def d_bj_check(d_hand):
    global p_chips
    global insurance_bet
    if d_hand[0] in ["J", "Q", "K", "X", "A"]:
        print("The dealer checks for blackjack...\n")
        if d_hand[0] == "A" and p_chips >= 1:
            insurance_bet = insurance_detect()
            p_chips = p_chips - insurance_bet
        if bj_detect(d_hand):
            return True
        else:
            print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
            print("The dealer does not have blackjack.\n")
            if insurance_bet > 0:
                print(f"your insurance bet of ${cent_rounder(insurance_bet)} is forfeit.\n")
            insurance_bet = 0


def hand_value(hand):
    proto_val = sum(point_values.get(card) for card in hand)
    if proto_val < 12 and ("A" in hand):
        final_val = proto_val + 10
    else:
        final_val = proto_val
    return final_val


def d_show_card(d_hand):
    if d_hand[0] == "A":
        return "an Ace"
    else:
        return point_values.get(d_hand[0])


def split_detect(p_hand):
    if p_hand[0] == p_hand[1] and p_chips >= pot:
        valid_choice = False
        while not valid_choice:
            choice = input(f"Would you like to split your hand? Will require another bet of ${cent_rounder(pot)} for the second hand. Enter 'y' for yes or 'n' for no: ").upper()
            if choice == "Y" or choice == "N":
                valid_choice = True
            else:
                print("Invalid input.")
        return choice


def double_down_detect(p_hand):
    if 9 <= hand_value(p_hand) <= 11 and p_chips >= pot:
        valid_choice = False
        while not valid_choice:
            choice = input(f"Would you like to double down? Will require another bet of ${cent_rounder(pot)}. Enter 'y' for yes or 'n' for no: ").upper()
            if choice == "Y" or choice == "N":
                valid_choice = True
            else:
                print("Invalid input.")
        return choice


def hand_splitter(p_hand):
    p_s_hand1.append(p_hand[0])
    p_s_hand2.append(p_hand[1])


def detect_split_aces(p_s_hand1):
    if p_s_hand1[0] == "A":
        return True
    else:
        return False


def second_bet_amount(pot, pot_updated):
    if pot_updated:
        return pot
    else:
        return pot / 2


def print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2):
    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n")
    if not d_turn:
        print(" _____    _____")
        print("|" + str(d_hand[0]) + "    |  |XXXXX|")
        print("|  " + str(d_hand[0]) + "  |  |XXXXX|")
        print("|    " + str(d_hand[0]) + "|  |XXXXX|")
        print("|_____|  |_____|")
        print(f"Dealer shows: {d_show_card(d_hand)}\n\n")
    else:
        print("   ".join(" _____" for card in d_hand))
        print("|" + "    |  |".join(str(card) for card in d_hand) + "    |")
        print("|  " + "  |  |  ".join(str(card) for card in d_hand) + "  |")
        print("|    " + "|  |    ".join(str(card) for card in d_hand) + "|")
        print("  ".join("|_____|" for card in d_hand))
        print(f"Dealer's hand's total: {hand_value(d_hand)}\n\n")
    print(f"   Current pot: $" + str(cent_rounder(pot)) + "     Chips remaining: $" + str(cent_rounder(p_chips)) + "\n")
    if insurance_bet > 0:
        print(f"   Insurance bet: ${cent_rounder(insurance_bet)}")
    if not split:
        print("   ".join(" _____" for card in p_hand))
        print("|" + "    |  |".join(str(card) for card in p_hand) + "    |")
        print("|  " + "  |  |  ".join(str(card) for card in p_hand) + "  |")
        print("|    " + "|  |    ".join(str(card) for card in p_hand) + "|")
        print("  ".join("|_____|" for card in p_hand))
        print(f"Your hand's total: {hand_value(p_hand)}\n")
    else:
        print("   ".join(" _____" for card in p_s_hand1) + "           " + "   ".join(" _____" for card in p_s_hand2))
        print("|" + "    |  |".join(str(card) for card in p_s_hand1) + "    |" + "          " + "|" + "    |  |".join(str(card) for card in p_s_hand2) + "    |")
        print("|  " + "  |  |  ".join(str(card) for card in p_s_hand1) + "  |" + "          " + "|  " + "  |  |  ".join(str(card) for card in p_s_hand2) + "  |")
        print("|    " + "|  |    ".join(str(card) for card in p_s_hand1) + "|" + "          " + "|    " + "|  |    ".join(str(card) for card in p_s_hand2) + "|")
        print("  ".join("|_____|" for card in p_s_hand1) + "          " + "  ".join("|_____|" for card in p_s_hand2))
        print(f"Your first hand's total: {hand_value(p_s_hand1)}          Your second hand's total: {hand_value(p_s_hand2)}\n")


main_screen()
rules(rules_q())
shuffle()
# deck = ["X", "A", "X", 3, "X", "A", 8, "X", "X", "X", "X", "X", "X"]
while can_play():
    if deck_i > 25:
        shuffle()
        print("The dealer reshuffles...\n")
        deck_i = 0
    s_hand1_state = "W"
    s_hand2_state = "W"
    insurance_bet = 0
    double_down = False
    pot_updated = False
    p_s_hand1 = []
    p_s_hand2 = []
    split = False
    d_turn = False
    end = False
    pot = bet(p_chips)
    p_chips = p_chips - pot
    p_hand = deal_p(deck, deck_i)
    d_hand = deal_d(deck, deck_i)
    deck_i = deck_i + 4
    print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
    if d_bj_check(d_hand):
        end = True
        d_turn = True
        print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
        d_turn = False
        if hand_value(p_hand) == 21:
            print(f"You and the dealer both have blackjack! Your ${cent_rounder(pot)} bet is returned to you.\n")
            p_chips = p_chips + pot
        else:
            print(f"The dealer has blackjack! You lose your initial bet of ${cent_rounder(pot)}!\n")
            if insurance_bet > 0:
                print(f"You win back ${cent_rounder(insurance_bet * 2)} from your insurance bet!\n")
            p_chips = p_chips + (insurance_bet * 3)
    elif bj_detect(p_hand):
        print(f"You have blackjack and win ${cent_rounder(pot * 1.5)}, 1.5 times your original bet of ${cent_rounder(pot)}! Congratulations!\n")
        end = True
        p_chips = p_chips + (pot * 2.5)
    elif double_down_detect(p_hand) == "Y":
        p_chips = p_chips - pot
        pot = pot * 2
        p_hand = hit(p_hand, deck, deck_i)
        deck_i = deck_i + 1
        d_turn = True
    elif split_detect(p_hand) == "Y":
        split = True
        p_chips = p_chips - pot
        pot = pot * 2
        hand_splitter(p_hand)
        print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
        if detect_split_aces(p_s_hand1):
            hit(p_s_hand1, deck, deck_i)
            deck_i = deck_i + 1
            hit(p_s_hand2, deck, deck_i)
            deck_i = deck_i + 1
            print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
            d_turn = True
        else:
            while hand_value(p_s_hand1) <= 21 and p_choice() == "H":
                p_s_hand1 = hit(p_s_hand1, deck, deck_i)
                deck_i = deck_i + 1
                print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
                if hand_value(p_s_hand1) > 21:
                    print(f"Your first hand has bust, losing your first bet of ${cent_rounder(pot / 2)}!\n")
                    s_hand1_state = "L"
                    if not pot_updated:
                        pot = pot / 2
                        pot_updated = True
            while hand_value(p_s_hand2) <= 21 and p_choice() == "H":
                p_s_hand2 = hit(p_s_hand2, deck, deck_i)
                deck_i = deck_i + 1
                print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
                if hand_value(p_s_hand2) > 21:
                    print(f"Your second hand has bust, losing your second bet of ${cent_rounder(second_bet_amount(pot, pot_updated))}!\n")
                    s_hand2_state = "L"
                    if not pot_updated:
                        pot = pot / 2
                        pot_updated = True
        if "W" in [s_hand1_state, s_hand2_state]:
            d_turn = True
        else:
            print(f"Both of your hands have bust! You lose your full bet of ${cent_rounder(pot)}!\n")
        while d_turn:
            print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
            while hand_value(d_hand) < 17:
                d_hand = hit(d_hand, deck, deck_i)
                deck_i = deck_i + 1
                print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
            if hand_value(d_hand) > 21:
                if [s_hand1_state, s_hand2_state].count("W") == 2:
                    print(f"The dealer busts! Congratulations, you win with both hands, netting you the full pot of ${cent_rounder(pot)}!\n")
                else:
                    print(f"The dealer busts! You win with one of your two hands, winning ${cent_rounder(pot)} and breaking even.\n")
                p_chips = p_chips + (pot * 2)
                d_turn = False
            else:
                if s_hand1_state == "W" and hand_value(d_hand) > hand_value(p_s_hand1):
                    s_hand1_state = "L"
                    print(f"The dealer's hand beats your first hand, losing your first bet of ${cent_rounder(second_bet_amount(pot, pot_updated))}!\n")
                elif s_hand1_state == "W" and hand_value(d_hand) == hand_value(p_s_hand1):
                    s_hand1_state = "T"
                    print(f"Your first hand is tied with the dealer's, returning your first bet of ${cent_rounder(second_bet_amount(pot, pot_updated))}!\n")
                    p_chips = p_chips + second_bet_amount(pot, pot_updated)
                elif s_hand1_state == "W":
                    print(f"You beat the dealer with your first hand, winning your first bet of ${cent_rounder(second_bet_amount(pot, pot_updated))}!\n")
                    p_chips = p_chips + second_bet_amount(pot, pot_updated) * 2
                if s_hand2_state == "W" and hand_value(d_hand) > hand_value(p_s_hand2):
                    s_hand2_state = "L"
                    print(f"The dealer's hand beats your second hand, losing your second bet of ${cent_rounder(second_bet_amount(pot, pot_updated))}!\n")
                elif s_hand2_state == "W" and hand_value(d_hand) == hand_value(p_s_hand2):
                    s_hand2_state = "T"
                    print(f"Your second hand is tied with the dealer's, returning your second bet of ${cent_rounder(second_bet_amount(pot, pot_updated))}!\n")
                    p_chips = p_chips + second_bet_amount(pot, pot_updated)
                elif s_hand2_state == "W":
                    print(f"You beat the dealer with your second hand, winning your second bet of ${cent_rounder(second_bet_amount(pot, pot_updated))}!\n")
                    p_chips = p_chips + second_bet_amount(pot, pot_updated) * 2
                d_turn = False
            end = True
    while not end and not split and not d_turn:
        if len(p_hand) == 5:
            print(f"Five-card Charlie! You win ${cent_rounder(pot * 1.5)}, 1.5 times your original bet of ${cent_rounder(pot)}!\n")
            end = True
            p_chips = p_chips + (pot * 2.5)
        elif p_choice() == "H":
            p_hand = hit(p_hand, deck, deck_i)
            deck_i = deck_i + 1
            print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
            if hand_value(p_hand) > 21:
                print(f"Bust! You lose your bet of ${cent_rounder(pot)}!\n")
                end = True
        else:
            d_turn = True
    while d_turn:
        print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
        while hand_value(d_hand) < 17:
            d_hand = hit(d_hand, deck, deck_i)
            deck_i = deck_i + 1
            print_table(d_hand, p_hand, pot, p_chips, p_s_hand1, p_s_hand2)
        if hand_value(d_hand) > 21:
            print(f"The dealer busts! Congratulations, you win ${cent_rounder(pot)}!\n")
            end = True
            p_chips = p_chips + (pot * 2)
        elif hand_value(d_hand) == hand_value(p_hand):
            end = True
            print(f"Your hand is equal to the dealer's! Your ${cent_rounder(pot)} bet is returned to you!\n")
            p_chips = p_chips + pot
        elif hand_value(d_hand) > hand_value(p_hand):
            end = True
            print(f"The dealer's hand is greater than your hand! You lose your bet of ${cent_rounder(pot)}!\n")
        else:
            print(f"Your hand is greater than the dealer's hand! You win ${cent_rounder(pot)}!\n")
            end = True
            p_chips = p_chips + (pot * 2)
        d_turn = False
    if can_play():
        print(f"Chips remaining: ${cent_rounder(p_chips)}")
        if play_again_q() == "N":
            play_again = False
            print(f"After a long night at the Blackjack table, you walk away with ${cent_rounder(p_chips)} to your name.")
    else:
        print("You've bust out of the game with less than a dollar to your name. God help you.")

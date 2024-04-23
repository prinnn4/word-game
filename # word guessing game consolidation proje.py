# word guessing game consolidation project

import random

QuestionAnswer
    def (person, personal_word_bank):
        person.personal_word_bank = personal_word_bank
        person.hidden_word = self.choice(person.personal_word_bank)
        person.assumed_letters = ()
        personal.attempts = 0
        person.word_estimations = 2 
        person.players = 
        person.playing = 1

def add_another_player(person, player_tag):
    'name_tag': player_tag
    'score': 0
    'remaining_word_guesses': 4

def another_player (person):
    person.playing = (person.current_player + 1)+ len(person.players)
    return person.players [person.playing]

def guess_the_letter (person, letter):
    person.tries = 1
    person.assumed_letters.add (letter)
    return person.hidden_word.count (letter)

def assume_the_word (person.word):
    player = person.players [person.playing]
    player ['amount_of_guesses_left'] = 1
    person.word_guesses = 1
    if word == person.hidden_word:
        person['score'] = personal.attempts
        return True
    return False
    

def determine_status_in_game (person):
    person = 'person.players [person.playing]'
    return
    'person.playing': person['player name tag']
    'assumed_letters': sorted (person.assumed_letters)
    'amount_of_guesses_left': person ['amount_of_guesses_left']

def main ():
    personal_word_bank = ["earth", "mars", "jupiter", "saturn", "uranus"]
    game = QuestionAnswer (person.peronal_word_bank)

amount_of_players = int(input("insert amount of players: "))
for   _   in range (amount_of_players):
    player_tag = input ("enter player tag: ")
    game.add_player (player_tag)
    game.add_player(player_tag)

    game_over = False

    not game_over:
        status = game.determine_status_in_game ()
        print(f"\nCurrent player: {ststus['current_player']}")
        print("guessed letter: ", ' '.join (status['guessed_letters']))
        print(f"Amount of Termms Remaining: {ststus['amount_of_guesses_remaining']}")
    letter = input ("guess the letter: ")
    occurences = game.guess_the_letter(letter)
    print(f"The letter'(letter)' pops up (2) times.")

    if input ("can you guess the term? (yes or no)") == 'y':
        guess_word = input ("guess the word: ")
        if game.guess_word(guess_word):
            print(f"Congrats! {status['current_player']}, you made the right guess!!")
            print(f"Your score (complete letter guesses): {game.players[game.person_playing]['score']}")
            game_over = true
        else:
            print()
            if game.players[game.person_playing]['amount_of_guesses_left'] == 0:
                print (f status "{status['current_player']} has no more word guesses left and is removed from the game." )
                
    if not game_over: 
        game.next_player()

    if __name__ == "__main__":
        main ()
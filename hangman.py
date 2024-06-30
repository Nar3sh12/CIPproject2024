import random

def get_random_word(difficulty):
    easy_words = [
        "cat", "dog", "book", "apple", "car", "tree", "fish", "ball", "hat", "sun",
        "milk", "pen", "shoe", "bird", "frog", "cup", "clock", "chair", "box", "star",
        "fan", "glass", "key", "leaf", "lamp", "mouse", "coin", "moon", "shirt", "wall",
        "ring", "snake", "fork", "ship", "wave", "drum", "rain", "kite", "sock", "road"
    ]
    medium_words = [
        "python", "hangman", "program", "banana", "orange", "pencil", "guitar", "school", "puzzle", "flower",
        "cloud", "jacket", "rocket", "window", "garden", "coffee", "planet", "mirror", "ticket", "camera",
        "wallet", "umbrella", "bridge", "castle", "laptop", "bicycle", "subway", "concert", "island", "factory",
        "jungle", "sandwich", "airport", "hammock", "statue", "volcano", "fireplace", "library", "skateboard", "waterfall"
    ]
    hard_words = [
        "challenge", "dictionary", "algorithm", "function", "revolution", "butterfly", "mountain", "university", "astronaut", "laboratory",
        "philosophy", "environment", "metamorphosis", "architecture", "choreography", "constellation", "symphony", "encyclopedia", "evaporation", "telescope",
        "quarantine", "biochemistry", "infrastructure", "psychology", "microbiology", "cryptography", "nanotechnology", "parallelogram", "photosynthesis", "transformation",
        "bioluminescence", "biodiversity", "anthropology", "cardiovascular", "circumference", "electromagnetism", "geopolitics", "immunology", "neurotransmitter", "thermodynamics"
    ]
    
    if difficulty == "easy":
        return random.choice(easy_words)
    elif difficulty == "medium":
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)

def get_hint(word):
    hints = {
        "cat": "A common household pet that says 'meow'.",
        "dog": "A loyal animal often called 'man's best friend'.",
        "book": "Something you read, full of pages.",
        "apple": "A fruit that keeps the doctor away.",
        "car": "A vehicle with four wheels.",
        "tree": "A tall plant with leaves and branches.",
        "fish": "An aquatic animal that swims.",
        "ball": "A round object used in many sports.",
        "hat": "Something you wear on your head.",
        "sun": "The star at the center of our solar system.",
        "milk": "A white liquid produced by mammals.",
        "pen": "A tool used for writing with ink.",
        "shoe": "Something you wear on your feet.",
        "bird": "An animal with feathers that can fly.",
        "frog": "An amphibian that can live in water and on land.",
        "cup": "A small container used for drinking.",
        "clock": "A device that tells time.",
        "chair": "A piece of furniture you sit on.",
        "box": "A container with flat sides.",
        "star": "A celestial body that shines at night.",
        "fan": "A device that creates a breeze.",
        "glass": "A transparent material used for windows.",
        "key": "A tool used to open locks.",
        "leaf": "A green part of a plant.",
        "lamp": "A device that produces light.",
        "mouse": "A small rodent or a computer device.",
        "coin": "A small, flat, round piece of metal used as money.",
        "moon": "The natural satellite of the Earth.",
        "shirt": "A piece of clothing worn on the upper body.",
        "wall": "A vertical structure that divides or encloses.",
        "ring": "A circular piece of jewelry worn on the finger.",
        "snake": "A legless reptile.",
        "fork": "A utensil with prongs used for eating.",
        "ship": "A large vessel that travels on water.",
        "wave": "A moving ridge on the surface of water.",
        "drum": "A musical instrument played by striking.",
        "rain": "Water that falls from the sky.",
        "kite": "A toy that flies in the wind.",
        "sock": "A garment worn on the foot.",
        "road": "A paved way for vehicles to travel on.",
        "python": "A popular programming language and a type of snake.",
        "hangman": "The game you are playing right now.",
        "program": "A set of instructions for a computer.",
        "banana": "A yellow fruit that's high in potassium.",
        "orange": "A citrus fruit and a color.",
        "pencil": "A tool used for writing or drawing.",
        "guitar": "A stringed musical instrument.",
        "school": "A place where you go to learn.",
        "puzzle": "A game or problem that tests ingenuity.",
        "flower": "A colorful part of a plant.",
        "cloud": "A visible mass of condensed water vapor in the sky.",
        "jacket": "A piece of clothing worn on the upper body for warmth.",
        "rocket": "A vehicle designed to travel in space.",
        "window": "An opening in a wall to let in light and air.",
        "garden": "An area of ground where plants are grown.",
        "coffee": "A beverage made from roasted coffee beans.",
        "planet": "A celestial body orbiting a star.",
        "mirror": "A reflective surface that reflects a clear image.",
        "ticket": "A piece of paper or card that allows entry.",
        "camera": "A device used to take photographs or videos.",
        "wallet": "A small case for carrying money and cards.",
        "umbrella": "A device used for protection from rain.",
        "bridge": "A structure built to span a physical obstacle.",
        "castle": "A large fortified building or set of buildings.",
        "laptop": "A portable computer.",
        "bicycle": "A two-wheeled vehicle powered by pedaling.",
        "subway": "An underground railway system.",
        "concert": "A live music performance.",
        "island": "A piece of land surrounded by water.",
        "factory": "A building where goods are manufactured.",
        "jungle": "A dense forest in a tropical region.",
        "sandwich": "A food item consisting of two pieces of bread with a filling.",
        "airport": "A complex of runways and buildings for air travel.",
        "hammock": "A swinging bed made of fabric or netting.",
        "statue": "A carved or cast figure of a person or animal.",
        "volcano": "A mountain with a crater that can erupt with lava.",
        "fireplace": "A structure for holding a fire inside a building.",
        "library": "A place where books and other media are kept for reading or borrowing.",
        "skateboard": "A short board with wheels used for skating.",
        "waterfall": "A cascade of water falling from a height.",
        "challenge": "A task or problem that tests abilities.",
        "dictionary": "A reference book with words and definitions.",
        "algorithm": "A process or set of rules for calculations.",
        "function": "A block of code in programming that performs a task.",
        "revolution": "A fundamental change in political power or organizational structures.",
        "butterfly": "An insect with colorful wings.",
        "mountain": "A large natural elevation of the earth's surface.",
        "university": "An institution of higher learning.",
        "astronaut": "A person trained to travel in space.",
        "laboratory": "A place equipped for scientific experiments.",
        "philosophy": "The study of the fundamental nature of knowledge.",
        "environment": "The natural world or ecosystem.",
        "metamorphosis": "The process of transformation from an immature form to an adult form.",
        "architecture": "The art or practice of designing and constructing buildings.",
        "choreography": "The sequence of steps and movements in dance.",
        "constellation": "A group of stars forming a recognizable pattern.",
        "symphony": "A lengthy piece of music for an orchestra.",
        "encyclopedia": "A comprehensive reference work with information on a wide range of subjects.",
        "evaporation": "The process of turning from liquid into vapor.",
        "telescope": "An instrument for observing distant objects.",
        "quarantine": "A period of isolation to prevent the spread of disease.",
        "biochemistry": "The branch of science concerned with the chemical processes in living organisms.",
        "infrastructure": "The basic physical and organizational structures needed for operation.",
        "psychology": "The scientific study of the mind and behavior.",
        "microbiology": "The study of microorganisms.",
        "cryptography": "The art of writing or solving codes.",
        "nanotechnology": "The science of manipulating materials on an atomic or molecular scale.",
        "parallelogram": "A four-sided plane rectilinear figure with opposite sides parallel.",
        "photosynthesis": "The process by which green plants use sunlight to synthesize foods.",
        "transformation": "A thorough or dramatic change in form or appearance.",
        "bioluminescence": "The production and emission of light by living organisms.",
        "biodiversity": "The variety of life in the world or a particular habitat.",
        "anthropology": "The study of human societies and cultures.",
        "cardiovascular": "Relating to the circulatory system, which comprises the heart and blood vessels.",
        "circumference": "The distance around the edge of a circle.",
        "electromagnetism": "The branch of physics concerned with the study of electric and magnetic fields.",
        "geopolitics": "The study of the effects of geography on international politics.",
        "immunology": "The branch of medicine and biology concerned with immunity.",
        "neurotransmitter": "A chemical substance that transmits nerve impulses across a synapse.",
        "thermodynamics": "The branch of physical science that deals with the relations between heat and other forms of energy."
    }
    return hints.get(word, "No hint available.")

def display_word_progress(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print("Word:", display)

def get_guess():
    guess = input("Guess a letter: ").lower()
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Invalid input. Please guess a single letter: ").lower()
    return guess

def display_hangman(incorrect_guesses):
    stages = [
        """
           ------
           |    |
                |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        """
    ]
    print(stages[incorrect_guesses])

def play_hangman():
    print("Welcome to Hangman!")
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Invalid choice. Choose difficulty (easy, medium, hard): ").lower()

    word = get_random_word(difficulty)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        display_word_progress(word, guessed_letters)
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        if incorrect_guesses >= 3:
            hint = get_hint(word)
            print(f"Hint: {hint}\n")
        
        guess = get_guess()
        
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.\n")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word '{word}' correctly!")
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! '{guess}' is not in the word.\n")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left.\n")
            if incorrect_guesses == max_incorrect_guesses:
                display_hangman(incorrect_guesses)
                print(f"Sorry, you ran out of guesses. The word was '{word}'.")

if __name__ == '__main__':
    play_hangman()

'''
# =============================================================================
# LUCKY 7 GAME - Python Console Application
# =============================================================================
# A dice betting game where users can bet on whether the total of two dice
# will be greater than 7, less than 7, or exactly 7.
# =============================================================================

import random


# =============================================================================
# CONSTANTS
# =============================================================================

WIN_POINTS = 10
JACKPOT_POINTS = 20
LOSE_POINTS = -5
MIN_OTP = 1000
MAX_OTP = 9999
DICE_MIN = 1
DICE_MAX = 6


# =============================================================================
# DATA STORAGE
# =============================================================================

# Nested dictionary to store user data
# Structure: {username: {"name": str, "wins": int, "losses": int, "score": int}}
users = {}


# =============================================================================
# HELPER FUNCTIONS - Input Validation & Display
# =============================================================================

def display_header(title: str) -> None:
    """Display a formatted header."""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")


def display_menu(options: list, prompt: str = "Choose an option") -> None:
    """Display menu options."""
    for option in options:
        print(option)
    print("-" * 30)


def get_valid_input(prompt: str, valid_options: list = None, case_sensitive: bool = False) -> str:
    """
    Get valid input from user.
    
    Args:
        prompt: The message to display to user
        valid_options: List of valid options (if any)
        case_sensitive: Whether to consider case in validation
    
    Returns:
        Valid user input
    """
    # Check if empty string is allowed
    allow_empty = valid_options and "" in valid_options if valid_options else False
    
    while True:
        user_input = input(prompt).strip()
        
        # Allow empty input only if "" is in valid_options
        if not user_input:
            if allow_empty:
                return ""
            print("Input cannot be empty. Please try again.")
            continue
        
        if valid_options:
            if case_sensitive:
                if user_input in valid_options:
                    return user_input
            else:
                # Convert both to lowercase for comparison
                if user_input.lower() in [opt.lower() for opt in valid_options]:
                    # Return original valid option to maintain consistency
                    for opt in valid_options:
                        if user_input.lower() == opt.lower():
                            return opt
            print(f"Invalid input. Valid options: {', '.join(valid_options)}")
        else:
            return user_input


def display_separator(char: str = "-", length: int = 40) -> None:
    """Display a separator line."""
    print(char * length)


# =============================================================================
# AUTHENTICATION FUNCTIONS
# =============================================================================

def generate_otp() -> str:
    """Generate a 4-digit OTP."""
    return str(random.randint(MIN_OTP, MAX_OTP))


def signup() -> str:
    """
    Handle user signup process.
    
    Returns:
        Username if signup successful, None otherwise
    """
    display_header("SIGNUP")
    
    # Get username with validation
    username = get_valid_input("Enter Username: ")
    
    if username in users:
        print("❌ Username already exists. Please login.")
        return None
    
    name = get_valid_input("Enter Your Name: ")
    
    # Create user with default stats
    users[username] = {
        "name": name,
        "wins": 0,
        "losses": 0,
        "score": 0
    }
    
    print("✅ Signup Successful! Welcome,", name)
    return username


def login() -> str:
    """
    Handle user login process.
    
    Returns:
        Username if login successful, None otherwise
    """
    display_header("LOGIN")
    
    username = get_valid_input("Enter Username: ")
    
    if username not in users:
        print("❌ User not found. Please signup first.")
        return None
    
    # OTP Authentication
    otp = generate_otp()
    print(f"📧 Generated OTP: {otp}")
    
    entered_otp = get_valid_input("Enter OTP: ")
    
    if entered_otp == otp:
        print(f"✅ Login Successful! Welcome back, {users[username]['name']}!")
        return username
    else:
        print("❌ Invalid OTP!")
        return None


def logout() -> None:
    """Display logout message."""
    print("\n👋 Logging out... Thanks for playing!")
    print(f"{'=' * 50}")


# =============================================================================
# GAME FUNCTIONS
# =============================================================================

def roll_dice() -> tuple:
    """
    Roll two dice.
    
    Returns:
        Tuple of (die1, die2)
    """
    die1 = random.randint(DICE_MIN, DICE_MAX)
    die2 = random.randint(DICE_MIN, DICE_MAX)
    return die1, die2


def display_game_rules() -> None:
    """Display game rules and betting options."""
    print("\n🎲 BETTING OPTIONS:")
    print("  +7   → Bet that total is GREATER than 7")
    print("  -7   → Bet that total is LESS than 7")
    print("  ==7  → Bet that total is EXACTLY 7")
    display_separator()


def get_user_bet() -> str:
    """
    Get and validate user's bet.
    
    Returns:
        Valid bet option
    """
    valid_bets = ["+7", "-7", "==7"]
    return get_valid_input(
        "\nEnter your bet (+7 | -7 | ==7): ",
        valid_options=valid_bets
    )


def process_bet(bet: str, total: int, username: str) -> bool:
    """
    Process the bet and update user score.
    
    Args:
        bet: User's bet option
        total: Sum of rolled dice
        username: Current user's username
    
    Returns:
        True if user won, False otherwise
    """
    won = False
    
    if bet == "+7":
        if total > 7:
            won = True
            print(f"✅ YOU WON! +{WIN_POINTS} Points")
            users[username]["wins"] += 1
            users[username]["score"] += WIN_POINTS
        else:
            print(f"❌ YOU LOST! {LOSE_POINTS} Points")
            users[username]["losses"] += 1
            users[username]["score"] += LOSE_POINTS
            
    elif bet == "-7":
        if total < 7:
            won = True
            print(f"✅ YOU WON! +{WIN_POINTS} Points")
            users[username]["wins"] += 1
            users[username]["score"] += WIN_POINTS
        else:
            print(f"❌ YOU LOST! {LOSE_POINTS} Points")
            users[username]["losses"] += 1
            users[username]["score"] += LOSE_POINTS
            
    elif bet == "==7":
        if total == 7:
            won = True
            print(f"🎉 JACKPOT! YOU WON! +{JACKPOT_POINTS} Points")
            users[username]["wins"] += 1
            users[username]["score"] += JACKPOT_POINTS
        else:
            print(f"❌ YOU LOST! {LOSE_POINTS} Points")
            users[username]["losses"] += 1
            users[username]["score"] += LOSE_POINTS
    
    return won


def display_user_stats(username: str) -> None:
    """Display current user's statistics."""
    user_data = users[username]
    print(f"\n📊 YOUR STATS:")
    print(f"   Wins:   {user_data['wins']}")
    print(f"   Losses: {user_data['losses']}")
    print(f"   Score:  {user_data['score']}")


def play_game(username: str) -> None:
    """
    Main game loop.
    
    Args:
        username: Current logged-in user's username
    """
    display_header("LUCKY 7 GAME")
    
    while True:
        display_game_rules()
        
        # Get user's bet
        bet = get_user_bet()
        
        # Roll dice and display results
        die1, die2 = roll_dice()
        total = die1 + die2
        
        print(f"\n🎲 Rolling dice...")
        print(f"   Dice 1: {die1}  |  Dice 2: {die2}")
        print(f"   Total:  {total}")
        
        display_separator()
        
        # Process the bet
        process_bet(bet, total, username)
        
        # Display updated stats
        display_user_stats(username)
        
        display_separator()
        
        # Ask to play again
        choice = get_valid_input(
            "Press Enter to play again | 0 to exit: ",
            valid_options=["0", ""]
        )
        
        if choice == "0":
            print("\n✅ Game ended successfully!")
            break
    
    logout()


# =============================================================================
# MAIN MENU FUNCTIONS
# =============================================================================

def show_main_menu() -> None:
    """Display the main menu."""
    display_header("WELCOME TO LUCKY 7 APPLICATION")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    print("-" * 30)


def main() -> None:
    """Main application loop."""
    while True:
        show_main_menu()
        
        option = get_valid_input(
            "Choose an option (1-3): ",
            valid_options=["1", "2", "3"]
        )
        
        if option == "1":
            user = signup()
            if user:
                play_game(user)
                
        elif option == "2":
            user = login()
            if user:
                play_game(user)
                
        elif option == "3":
            display_header("APPLICATION CLOSED")
            print("👋 Thank you for playing Lucky 7!")
            print("=" * 50)
            break


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()

'''
import random

# Nested dictionary to store user data
users = {}

# ---------------------- FUNCTIONS ----------------------

def generate_otp():
    """Generate a 4-digit OTP"""
    return str(random.randint(1000, 9999))


def signup():
    username = input("Enter Username: ")

    if username in users:
        print("Username already exists. Please login.")
        return None

    name = input("Enter Your Name: ")

    # Creating nested dictionary for user
    users[username] = {
        "name": name,
        "wins": 0,
        "losses": 0,
        "score": 0
    }

    print("Signup Successful!")
    return username


def login():
    username = input("Enter Username: ")

    if username not in users:
        print("User not found. Please signup first.")
        return None

    otp = generate_otp()
    print("Generated OTP:", otp)

    entered_otp = input("Enter OTP: ")

    if entered_otp == otp:
        print("Login Successful!")
        return username
    else:
        print("Invalid OTP!")
        return None


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def play_game(username):

    while True:

        print("\n------ Lucky 7 Game ------")
        print("Bet Options: +7  |  -7  |  ==7")
        print("Type 'exit' to logout")

        bet = input("Enter your bet: ")

        if bet == "exit":
            print("Logging out...")
            break

        if bet not in ["+7", "-7", "==7"]:
            print("Invalid Bet! Try again.")
            continue

        die1, die2 = roll_dice()
        total = die1 + die2

        print(f"Dice Rolled: {die1} and {die2}")
        print("Total:", total)

        # Conditional Statements

        if bet == "+7":
            if total > 7:
                print("You Won! +10 Points")
                users[username]["wins"] += 1
                users[username]["score"] += 10
            else:
                print("You Lost! -5 Points")
                users[username]["losses"] += 1
                users[username]["score"] -= 5

        elif bet == "-7":
            if total < 7:
                print("You Won! +10 Points")
                users[username]["wins"] += 1
                users[username]["score"] += 10
            else:
                print("You Lost! -5 Points")
                users[username]["losses"] += 1
                users[username]["score"] -= 5

        elif bet == "==7":
            if total == 7:
                print("You Won! +20 Points")
                users[username]["wins"] += 1
                users[username]["score"] += 20
            else:
                print("You Lost! -5 Points")
                users[username]["losses"] += 1
                users[username]["score"] -= 5

        # Display Updated Data
        print("\nUpdated User Data:", users[username])

        choice = input("\nPress any key to play again | Press 0 to stop game: ")

        if choice == "0":
            print("Game Stopped.")
            break


# ---------------------- MAIN PROGRAM ----------------------

while True:

    print("\n===== Welcome to Lucky 7 Application =====")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        user = signup()
        if user:
            play_game(user)

    elif option == "2":
        user = login()
        if user:
            play_game(user)

    elif option == "3":
        print("Exiting Application...")
        break

    else:
        print("Invalid Choice! Try Again.")

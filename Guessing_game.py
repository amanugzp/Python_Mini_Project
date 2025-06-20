import random
from datetime import datetime
import json

# Difficulty-based word bank
WORDS = {
    'easy':    ["apple", "tiger", "train", "grape", "chair"],         # 5-letter words
    'medium':  ["bottle", "planet", "monkey", "guitar", "laptop"],    # 6-letter words
    'hard':    ["diamond", "mission", "journey", "picture", "monster"]  # 7-letter words
}

MAX_ATTEMPTS = 8  # Optional: set a max attempt limit

def choose_word(level):
    return random.choice(WORDS[level])

def give_hint(secret, guess):
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    return hint

def log_game_result(level, word, attempts):
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "level": level,
        "word": word,
        "attempts": attempts
    }
    with open("game_log.json", "a") as file:
        file.write(json.dumps(log) + "\n")

def main():
    print("🎮 Welcome to the Password Guessing Game!")
    print("Select difficulty level: easy / medium / hard")

    level = input("Enter difficulty: ").strip().lower()
    if level not in WORDS:
        print("⚠️ Invalid choice. Defaulting to easy level.")
        level = 'easy'

    secret = choose_word(level)
    secret_length = len(secret)
    attempts = 0
    guess_history = []

    print(f"\n🔐 A secret password has been selected! It has {secret_length} letters.")
    print("Start guessing...")

    while True:
        guess = input(f"Your guess ({secret_length} letters): ").strip().lower()

        if len(guess) != secret_length:
            print(f"⚠️ Your guess must be exactly {secret_length} letters long.")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n✅ Correct! You guessed the word '{secret}' in {attempts} attempts.")
            log_game_result(level, secret, attempts)
            break
        else:
            hint = give_hint(secret, guess)
            guess_history.append((guess, hint))
            print(f"❌ Incorrect. Hint: {hint}")

            # Optional: show past guesses
            print("\n📜 Previous guesses:")
            for g, h in guess_history:
                print(f"  {g} → {h}")

            # Optional: attempt limit
            if attempts >= MAX_ATTEMPTS:
                print(f"\n🚫 You've used all {MAX_ATTEMPTS} attempts. The correct word was '{secret}'.")
                log_game_result(level, secret, attempts)
                break

    print("🎉 Game Over. Thanks for playing!")

if __name__ == "__main__":
    main()

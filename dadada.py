import random   # built-in: lets us pick random characters during obfuscation
import re       # built-in: "regular expressions" — a way to find patterns in text
import sys      # built-in: lets the script read from a file instead of the clipboard if needed

# --- Load the clipboard library ---
# pyperclip is the one external library this script needs. It handles copy/paste
# across Mac, Windows, and Linux so you don't have to. If it's not installed,
# the script falls back to letting you type or paste text manually in the terminal.
try:
    import pyperclip
    HAS_CLIPBOARD = True
except ImportError:
    HAS_CLIPBOARD = False


# --- Typographic shape profiles ---
# Instead of replacing every letter randomly, we group letters by how they look.
# This keeps the visual rhythm of your text intact after obfuscation.
#
# ASCENDERS: letters with a tall stroke rising above the main body (like b, d, h)
# DESCENDERS: letters with a tail dropping below the baseline (like g, p, y)
# NEUTRALS: letters that sit fully within the main body height (like a, e, n, o)
# CAPITALS: all uppercase letters — they always stay uppercase
#
# When the script replaces a letter, it only picks from the same group,
# so an ascender always becomes another ascender, never a descender or neutral.

ASCENDERS = list("bdfhklt")
DESCENDERS = list("gjpqy")
NEUTRALS = list("aceimnorsuvwxz")
CAPITALS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Numbers are grouped by how they look on the page.
# Straight/angular digits look different from curved ones — swapping across
# groups would change the visual weight of a price or date.
DIGIT_STRAIGHT = list("147")  # made of straight lines and angles
DIGIT_CURVED   = list("0389") # made of loops and pure curves
DIGIT_MIXED    = list("256")  # straight strokes leading into a curve (6 opens with a straight entry before looping)


def get_visual_group(char):
    """Given a single character, return the list it belongs to (or None if unknown)."""
    if char in ASCENDERS:     return ASCENDERS
    if char in DESCENDERS:    return DESCENDERS
    if char in NEUTRALS:      return NEUTRALS
    if char in CAPITALS:      return CAPITALS
    if char in DIGIT_STRAIGHT: return DIGIT_STRAIGHT
    if char in DIGIT_CURVED:   return DIGIT_CURVED
    if char in DIGIT_MIXED:    return DIGIT_MIXED
    return None  # character not in any group (e.g. accented letters — handled below)


def obfuscate_char(char):
    """Replace one character with a random character from the same visual group."""
    group = get_visual_group(char)
    if group:
        return random.choice(group)  # pick any character from the same group at random

    # Accented Latin letters (é, ñ, ü, ç, ø, etc.) aren't in the profiles above.
    # We drop the accent and treat them by case: lowercase → neutral, uppercase → capital.
    # This avoids the accent surviving into the output and hinting at the original language.
    if char.isalpha():
        return random.choice(CAPITALS if char.isupper() else NEUTRALS)

    return char  # anything else (emoji, symbols, etc.) is left exactly as-is


def mutate_and_obfuscate_token(token):
    """
    Take a single word or number and do two things:
    1. Randomly adjust its length by ±1 character (stress-tests your layout)
    2. Replace every character with a visual lookalike from the same group
    """

    # Mixed tokens like "UX300" or "H2O" contain both letters and digits.
    # We can't cleanly mutate their length without breaking the pattern,
    # so we obfuscate each character in place and leave the length alone.
    if not token.isalpha() and not token.isdigit():
        return "".join(obfuscate_char(c) for c in token)

    # Randomly decide whether to shrink (-1), keep the same (0), or grow (+1) the word.
    delta = random.choice([-1, 0, 1])
    chars = list(token)  # split the word into a list of individual characters

    if delta == -1 and len(chars) > 2:
        # Shrink: remove one character at a random position.
        # We only shrink words longer than 2 characters so tiny words don't vanish.
        chars.pop(random.randint(0, len(chars) - 1))

    elif delta == 1:
        # Grow: duplicate one character at a random position.
        # The duplicate gets obfuscated in the next step, so it won't look like a repeat.
        idx = random.randint(0, len(chars) - 1)
        chars.insert(idx, chars[idx])

    # Now replace every character in the (possibly resized) list with its visual lookalike.
    return "".join(obfuscate_char(c) for c in chars)


def process_copy(text):
    """
    Split the full text into words/numbers and separators (spaces, punctuation, line breaks),
    obfuscate only the words and numbers, and reassemble everything in the original order.

    Spaces, punctuation, and line breaks are never touched — they anchor your layout.
    """

    # re.split with a capturing group keeps the separators in the output list.
    # Pattern ([^\w]+) means: "split on any sequence of non-word characters,
    # but keep those separators in the result so we can put them back."
    # Example: "Hi, world!" → ["Hi", ", ", "world", "!", ""]
    tokens = re.split(r'([^\w]+)', text)

    result = []
    for token in tokens:
        if token.isalnum():
            # Pure word (letters only) or pure number (digits only) — obfuscate it.
            result.append(mutate_and_obfuscate_token(token))
        else:
            # Space, comma, period, line break, emoji, etc. — pass through unchanged.
            result.append(token)

    return "".join(result)  # stitch everything back together into one string


def main():
    print("--- Dadada ---")

    if HAS_CLIPBOARD:
        # Read whatever text you last copied (Cmd+C / Ctrl+C).
        text = pyperclip.paste()

        if not text or not text.strip():
            print("[!] Your clipboard is empty. Copy some text first!")
            return

        print("-> Grabbing text from clipboard...")
        obfuscated_text = process_copy(text)

        # Write the obfuscated result back to the clipboard so you can paste it directly.
        pyperclip.copy(obfuscated_text)

        print("-> Success! Obfuscated layout text copied to clipboard.")
        print("\nPreview:")
        print("-" * 50)
        # Show the first 150 characters as a quick sanity check in the terminal.
        preview = obfuscated_text[:150] + ("..." if len(obfuscated_text) > 150 else "")
        print(preview)
        print("-" * 50)
        print("You can now paste (Cmd+V) directly into your design tool.")

    else:
        # pyperclip isn't installed — fall back to reading text from the terminal.
        # You can also pipe a file into the script: python3 dadada.py < myfile.txt
        print("\n[!] 'pyperclip' not found. Falling back to manual mode.")
        print("Paste your text below (Press Enter, then Ctrl+D to finish):")
        text = sys.stdin.read()

        obfuscated_text = process_copy(text)
        print("\n--- Obfuscated Output ---")
        print(obfuscated_text)


# This block means: only run main() if this file is executed directly
# (e.g. `python3 dadada.py`), not if it's imported by another script.
if __name__ == "__main__":
    main()

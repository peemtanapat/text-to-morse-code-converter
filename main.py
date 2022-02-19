from converter import text_to_morse
from regex import check_pattern

while True:
    text = input("Enter your text: ").strip()
    if not check_pattern(text):
        print("We support these characters: [A-Z a-z 0-9 / ? . , - ( )]\n"
              "Please try again...\n")
        continue
    if text == ':q':
        print("Thank you.")
        break
    print(f"Morse Code: \n{text_to_morse(text)}\n")

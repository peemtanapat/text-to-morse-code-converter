from dict import morse_dict


def text_to_morse(text: str) -> str:
    text = text.upper()
    converted_text: str = ""
    prev_is_blank = False
    for char in text:
        if char == ' ' and prev_is_blank:
            continue

        if char == ' ':
            converted_text += '\n'
            prev_is_blank = True
        else:
            print(char, morse_dict[char])
            converted_text += morse_dict[char] + ' '
            prev_is_blank = False
    return converted_text

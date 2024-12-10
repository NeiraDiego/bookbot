def main():
    dir = "books/frankenstein.txt"
    with open(dir) as f:
        file_contents = f.read()
    words = count_words(file_contents)
    char = count_char(file_contents)
    print_results(dir, words, char)

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_results(dir, words, char):
    print(f"""--- Begin report of {dir} ---
{words} words found in the document
          """)
    for x in char:
        print(f"The '{x}' character was found {char[x]} times")

main()
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))

def count_words(content):
    words = content.split()
    return len(words)


main()
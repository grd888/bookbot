from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(filepath):
   with open(filepath, 'r') as f:
        return f.read()

def main():
    book_path = "./books/frankenstein.txt"
    contents = get_book_text(book_path)
    word_count = get_num_words(contents)
    print(f"{word_count} words found in the document")
    char_counts = get_char_counts(contents)
    chars_sorted_list = get_sorted_char_counts(char_counts)
    print_report(book_path, word_count, chars_sorted_list)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
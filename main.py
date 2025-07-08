from stats import get_num_words
from stats import character_count
from stats import sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        book_path (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(book_path) as f:
        return f.read()

def main():
    """
    Main function to execute the script.
    """
    book_text = get_book_text(book_path)
    words = get_num_words(book_text)
    characters = character_count(book_text) 
    sorted_characters = sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        character = item["char"]
        count = item["num"]
        print(f"{character}: {count}") # Note: No single quotes around {character} here, as per example
    print("============= END ===============")


main()  # need to run from the same directory as main.py
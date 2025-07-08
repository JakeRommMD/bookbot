def get_num_words(book_text):
        words = len(book_text.split())
        return words

def character_count(book_text):
        book_characters = {}
        book_text = book_text.lower()   
        for char in book_text:
                if char not in book_characters:
                        book_characters[char] = 1
                else:
                        book_characters[char] += 1
        return book_characters

def sorted_list(book_characters):
        list_of_characters = []
        for char, count in book_characters.items():
                if char.isalpha():
                        new_dict = {"char": char, "num": count}
                        list_of_characters.append(new_dict)
        list_of_characters.sort(key=lambda x: x["num"], reverse=True)
        return list_of_characters




        return sorted(book_characters.items(), key=lambda item: item[1], reverse=True)
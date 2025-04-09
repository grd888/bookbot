def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in counts:
            counts[lower_char] += 1
        else:
            counts[lower_char] = 1
    return counts

def sort_on(d):
    return d["num"]


def get_sorted_char_counts(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

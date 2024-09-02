def sort_on(item):
    return item[1]

def main():
    path_file = "books/frankenstein.txt"
    with open(path_file) as f:
        file_content = f.read()

    words = file_content.split()
    words_count = len(words)
    
    words_l = [word.lower() for word in words]
    
    count_char = {}
    for word in words_l:
        for char in word:
            if char in count_char:
                count_char[char] += 1
            else:
                count_char[char] = 1

    print(f"---Begin report of {path_file}---")
    print(f"{words_count} words found in the document")

    sorted_char_count = sorted(count_char.items(), reverse=True, key=sort_on)
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
        
if __name__ == "__main__":
    main()

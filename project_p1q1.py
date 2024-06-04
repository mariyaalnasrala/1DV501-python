
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()

        unique_words = set(words)
        count = len(unique_words)

    return count


path_1 = 'new_life_of_brain'
path_2 = 'new.swe.news.output'
print(read_file(path_1))

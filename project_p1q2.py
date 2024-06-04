def count(item):
    return item[1]


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        unique_words = {}
        for word in words:
            if len(word) > 4:
                if word in unique_words:
                    unique_words[word] += 1
                else:
                    unique_words[word] = 1

        sorted_words = sorted(unique_words.items(), key=count, reverse=True)
        return sorted_words


path_1 = 'new_life_of_brain'
path_2 = 'new.swe.news.output'

result = read_file(path_1)
res = read_file(path_2)
print(result[:10])
print(res[:10])

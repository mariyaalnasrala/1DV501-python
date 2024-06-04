from BstMap_p3 import BstMap_p3

file1 = 'new_life_of_brain'
file2 = 'new.swe.news.output'

map_life_of_brain = BstMap_p3()
map_news_items = BstMap_p3()


def read_file(file_path, bst_map):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > 4:
                    count = bst_map.get(word)
                    if count is not None:
                        bst_map.add(word, count + 1)
                    else:
                        bst_map.add(word, 1)


def get_top_words(bst_map, top_count):
    word_list = bst_map.as_list()
    word_list.sort(key=lambda x: x[1], reverse=True)
    return word_list[:top_count]


read_file(file1, map_life_of_brain)
read_file(file2, map_news_items)

print("Life of Brian:")
print("  Number of tree nodes:", map_life_of_brain.inter_nodes())
print("  Max depth:", map_life_of_brain.max_depth())
print("  Top 10 words:", get_top_words(map_life_of_brain, 10))

print("\nNews Items:")
print("  Number of tree nodes:", map_news_items.inter_nodes())
print("  Max depth:", map_news_items.max_depth())
print("  Top 10 words:", get_top_words(map_news_items, 10))

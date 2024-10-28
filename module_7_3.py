from os.path import split


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for item in file_names:
            self.file_names.append(item)


    def get_all_words(self):
        all_words = dict()
        symbol_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            temp_str = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    #print(type(line))
                    #print(line)
                    for symbol in symbol_to_remove:
                        line = line.replace(symbol,"")
                    for word in line.split():
                        temp_str.append(word)
            all_words[name] = temp_str
        return all_words

    def find(self, word):
        temp_dict = self.get_all_words()
        find_point = dict()
        for name, words in temp_dict.items():
            i = 1
            for word_ in words:
                if word_.lower() == word.lower():
                    find_point[name] = i
                    return  find_point
                i +=1

    def count(self, word):
        temp_dict = self.get_all_words()
        find_count = dict()
        for name, words in temp_dict.items():
            i = 0
            for word_ in words:
                if word_.lower() == word.lower():
                    i +=1
            find_count[name] = i
        return find_count




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
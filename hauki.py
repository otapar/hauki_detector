
class Hauki:
    # Counts vowels in a text
    def count_vowels(self, inputtext):
        if inputtext is None:
            return 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        count = 0
        for letter in inputtext:
            if letter in vowels:
                count += 1
        return count

    # Counts contiguous vowels in a text
    # for a clean and shorter code regex can be used instead of this method.
    # But regex is more expensive than this primitive approach. It uses more cpu and memory.
    #   return len(re.findall("[aeiouy]{2}", inputText))

    def count_consecutive_vowels(self, inputtext):
        if inputtext is None:
            return 0
        vowels = ['a', 'e','i','o','u','y']
        count = 0
        candidate_flag = False
        consecutive_count = 0
        for letter in inputtext:
            if letter in vowels:
                candidate_flag = True
                consecutive_count += 1
            elif candidate_flag == True and consecutive_count > 1:
                count += 1
                candidate_flag = False
                consecutive_count = 0
            else:
                candidate_flag = False
                consecutive_count = 0

        if candidate_flag is True and consecutive_count > 1:
            count += 1
        return count

    # Reads file contents into a list
    def read_file_content(self, filename):
        with open(filename) as f:
            content = f.readlines()
        # Delete end of lines
        content = [x.strip() for x in content]
        return content

    def answer(self, file):
        file_lines = self.read_file_content(file)
        hauki_match = [5, 7, 5]

        for fileLine in file_lines:

            poem_lines = fileLine.split('/')
            poem_syllables = []

            for poemLine in poem_lines:
                vowel_count = self.count_vowels(poemLine)
                consecutive_vowel_count = self.count_consecutive_vowels(poemLine)
                count_syllable = vowel_count - consecutive_vowel_count
                poem_syllables.append(count_syllable)

            print(",".join(map(str, poem_syllables)), end=',')
            if poem_syllables == hauki_match:
                print("Yes")
            else:
                print("No")


ff = Hiker()
ff.answer("inputFile.txt")


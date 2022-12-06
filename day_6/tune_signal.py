class SignalTuner:

    def __init__(self):
        self.unique_letters = {}

    def update_mapping(self, num):
        new_mapping = {k: v for k, v in self.unique_letters.items() if v >= num}
        self.unique_letters = new_mapping
        return self.unique_letters


def tune_signal(file):
    with open(file) as f:
        line = f.read()

        i = 0
        buffer_len = len(line)
        while i < buffer_len:
            letter = line[i]
            second = line[i + 1]
            third = line[i + 2]
            fourth = line[i + 3]

            if letter != second and letter != third and letter != fourth and second != third \
                    and second != fourth and third != fourth:
                return i + 3 + 1
            else:

                i += 1


print(tune_signal('input.txt'))

signal_tuner = SignalTuner()


def part_two(file):
    with open(file) as f:
        line = f.read()

        i = 0

        letter_list = signal_tuner.unique_letters
        buffer_len = len(line)

        while i < buffer_len:
            letter = line[i]

            if letter not in letter_list:
                letter_list[letter] = i
            else:
                let_i = letter_list.get(letter)
                letter_list = signal_tuner.update_mapping(let_i + 1)
                letter_list[letter] = i
            i += 1
            if len(letter_list) == 14:
                return i


print(part_two('input.txt'))

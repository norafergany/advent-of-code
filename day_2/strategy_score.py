class GameRules:
    def __init__(self):
        self.rock_points = 1
        self.paper_points = 2
        self.scissors_points = 3

        self.win_points = 6
        self.draw_points = 3
        self.lose_points = 0

        self.rock_dict = {
            "points": {
                "X": self.draw_points + self.rock_points,
                "Y": self.win_points + self.paper_points,
                "Z": self.lose_points + self.scissors_points,
            },
            "strategy": {
                "X": self.lose_points + self.scissors_points,
                "Y": self.draw_points + self.rock_points,
                "Z": self.win_points + self.paper_points

            }

        }

        self.paper_dict = {
            "points": {
                "X": self.lose_points + self.rock_points,
                "Y": self.draw_points + self.paper_points,
                "Z": self.win_points + self.scissors_points
            },
            "strategy": {
                "X": self.lose_points + self.rock_points,
                "Y": self.draw_points + self.paper_points,
                "Z": self.win_points + self.scissors_points

            }
        }

        self.scissors_dict = {
            "points": {
                "X": self.win_points + self.rock_points,
                "Y": self.lose_points + self.paper_points,
                "Z": self.draw_points + self.scissors_points,
            },
            "strategy": {
                "X": self.lose_points + self.paper_points,
                "Y": self.draw_points + self.scissors_points,
                "Z": self.win_points + self.rock_points

            }
        }

        # The points dictionary to use based on Player 1's move
        self.player_1_dict = {
            "A": self.rock_dict,
            "B": self.paper_dict,
            "C": self.scissors_dict
        }


game = GameRules()


def part_1(file):
    total_points = 0
    with open(file) as f:
        lines = f.readlines()

        for line in lines:
            round_points = 0
            curr_round = line.strip().split(' ')

            calc_round = game.player_1_dict.get(curr_round[0])['points']
            player_2 = curr_round[1]
            round_points += calc_round.get(player_2)

            total_points += round_points
    return total_points


def part_2(file):
    total_points = 0
    with open(file) as f:
        lines = f.readlines()

        for line in lines:
            round_points = 0
            curr_round = line.strip().split(' ')

            calc_round = game.player_1_dict.get(curr_round[0])['strategy']
            player_2 = curr_round[1]
            round_points += calc_round.get(player_2)

            total_points += round_points
    return total_points


print(part_1('input.txt'))
print(part_2('input.txt'))

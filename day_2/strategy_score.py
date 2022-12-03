rock_points = 1
paper_points = 2
scissors_points = 3

win_points = 6
draw_points = 3
lose_points = 0

rock_dict = {
    "points": {
        "X": draw_points + rock_points,
        "Y": win_points + paper_points,
        "Z": lose_points + scissors_points
    },

}

paper_dict = {
    "points": {
        "X": lose_points + rock_points,
        "Y": draw_points + paper_points,
        "Z": win_points + scissors_points},
    "strategy": {

    }
}

scissors_dict = {
    "points": {
        "X": win_points + rock_points,
        "Y": lose_points + paper_points,
        "Z": draw_points + scissors_points
    }
}

# The points dictionary to use based on Player 1's move
player_1_dict = {
    "A": rock_dict,
    "B": paper_dict,
    "C": scissors_dict
}


def part_1(file):
    total_points = 0
    with open(file) as f:
        lines = f.readlines()

        for line in lines:
            round_points = 0
            curr_round = line.strip().split(' ')

            calc_round = player_1_dict.get(curr_round[0])['points']
            player_2 = curr_round[1]
            round_points += calc_round.get(player_2)

            total_points += round_points
    return total_points


print(part_1('input.txt'))

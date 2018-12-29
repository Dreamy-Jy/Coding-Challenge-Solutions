def find_program_strength(commands):
    beam_strength = 1
    damage_taken = 0

    for command in commands:
        if command == 'S':
            damage_taken += beam_strength
        elif command == 'C':
            beam_strength *= 2

    return damage_taken


def solve_single_case(endurance, beam_commands):
    lazer_count = beam_commands.count('S')

    if lazer_count > endurance:
        return "IMPOSSIBLE"
    if lazer_count == 0:
        return 0

    switch_count = 0
    alterned_commands = beam_commands
    beam_strength = find_program_strength(alterned_commands)

    while beam_strength > endurance:

        target_lazer_index = len(alterned_commands) - 1
        while alterned_commands[target_lazer_index] != 'S' or alterned_commands[target_lazer_index - 1] == 'S':
            target_lazer_index -= 1

        if target_lazer_index != 0:
            switch_count += 1

            temp = list(alterned_commands)
            temp[target_lazer_index], temp[target_lazer_index -
                                           1] = temp[target_lazer_index-1], temp[target_lazer_index]

            alterned_commands = "".join(temp)

            beam_strength = find_program_strength(alterned_commands)

            print("After " + str(switch_count) +
                  " switchs. The array look like: " + alterned_commands)
        else:
            print("Method broken...")
            break

    return switch_count


if __name__ == "__main__":

    print(solve_single_case(int(input("Put in a shield endurance: ")),
                            input("Put in a pattern: ")))

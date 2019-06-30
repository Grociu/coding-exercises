import copy


class Jug(object):
    def __init__(self, water, volume):
        self.water = water
        self.volume = volume

    def __eq__(self, other):
        return self.water == other.water and self.volume == other.volume

    def __repr__(self):
        return 'JUG: {} // {}'.format(self.water, self.volume)

    def pour_from_to(self, other):
        while other.water < other.volume and self.water:
            self.water -= 1
            other.water += 1
        return self, other


def perform_pours_on_state(state):
    # Creates unique instances of Jug for each possible pour.
    result = [copy.deepcopy(state) for i in range(6)]
    # Six possible combinations of pours.
    Jug.pour_from_to(result[0][0], result[0][1])
    Jug.pour_from_to(result[1][0], result[1][2])
    Jug.pour_from_to(result[2][1], result[2][0])
    Jug.pour_from_to(result[3][1], result[3][2])
    Jug.pour_from_to(result[4][2], result[4][0])
    Jug.pour_from_to(result[5][2], result[5][1])
    # We're only interested in new states.
    return [entry for entry in result if entry != state]


def waterjug(start, goal):
    initial = [
        Jug(0, start[0]),
        Jug(0, start[1]),
        Jug(start[2], start[2])
    ]

    target = [
        Jug(goal[0], start[0]),
        Jug(goal[1], start[1]),
        Jug(goal[2], start[2])
    ]

    reached_states, this_level_states = [initial], [initial]
    next_operation_states, performed_operations = [], 0

    while target not in reached_states:
        performed_operations += 1
        for state in this_level_states:
            next_operation_states.extend([
                new_state for new_state in perform_pours_on_state(state) if
                new_state not in reached_states
            ])
        reached_states.extend(next_operation_states)
        this_level_states, next_operation_states = next_operation_states, []
        if not this_level_states:
            return "No solution."
    return performed_operations

"""
Cake Data Structure:
    [
        ["G", "?", "?"],
        ["?", "C", "?"],
        ["?", "?",  "J"]
    ]

Valid search data structure:
    {
        Left: True,
        Right: True,
        Up: True,
        Down: True
    }


"""


def build_cake(template_cake):
    built_cake = template_cake

    def init_search_space(row, col):
        spaces = {
            "left": True,
            "right": True,
            "up": True,
            "down": True
        }

        if row == 0:
            spaces["up"] = False
        if row == len(built_cake) - 1:
            spaces["down"] = False

        if col == 0:
            spaces["left"] = False
        if col == len(built_cake[0]) - 1:
            spaces["right"] = False

        return spaces

    for row in range(len(built_cake)):
        for col in range(len(built_cake[row])):
            selected_piece = built_cake[row][col]
            if selected_piece != "?":
                valid_searchs = init_search_space(row, col)
                print("char {3} [row: {0}, col: {1}] = {2}".format(
                    row, col, valid_searchs, selected_piece))


"""
def build_cake(template_cake):
	built_cake = template_cake

	def init_search_space(row, col):
        space = {"left":True, "right":True, "up":True, "down":True}
        if row ==  0:
            space["up"] = False
        if row == len(built_cake) -1:
            space["down"] = False
        if col == 0:
            space["left"] = False
        if col == len(built_cake[0]):
            space["right"] = True

        return space
		
    for row in range(len(built_cake)):
            for col in range(len(built_cake)):
                selected_piece = built_cake[row][col]
                if selected_piece != "?":
                    valid_searchs = init_search_space(row, col)
                    print("[row: {0}, col: {1}] = {2}".format(row, col, valid_searchs))
"""

build_cake([["G", "?", "?"], ["?", "C", "?"], ["?", "?", "J"]])

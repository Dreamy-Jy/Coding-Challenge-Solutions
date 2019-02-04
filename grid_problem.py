"""
lamp format [X, Y]
"""


class Grid(object):

    # TODO validate inputs
    def __init__(self, size, lamps):
        self.SIZE = size
        # holds data on lamp coord, and wheither that lamp is on
        self.lamps = list(map(lambda lamp: (lamp, True), lamps))
        # a dictory of illuminated diagonals, value are linked to lamps by index
        self.lit_diagonals = self.get_diagonals()

    def __repr__(self):
        return "<Grid {0}x{0}, containing {1} lamps>".format(self.SIZE, len(self.lamps))

    def get_diagonals(self):
        illuminated = {}

        for l_i in range(len(self.lamps)):
            lamp_coord = self.lamps[l_i][0]
            s_x = x_left = x_right = lamp_coord[0] + 0
            s_y = y = lamp_coord[1] + 0

            # think about making this process a single loop
            # check up
            output = []
            for _ in range(s_y, 0, -1):
                y -= 1
                if x_right + 1 < self.SIZE:
                    x_right += 1
                    output.append([x_right, y])
                if x_left - 1 > -1:
                    x_left -= 1
                    output.append([x_left, y])

            # check down
            x_left = x_right = s_x
            y = s_y
            for _ in range(s_y, self.SIZE):
                y += 1
                if x_right + 1 < self.SIZE:
                    x_right += 1
                    output.append([x_right, y])
                if x_left - 1 > -1:
                    x_left -= 1
                    output.append([x_left, y])
            illuminated[l_i] = output

        return illuminated

    # Thimk abour this one. [below]

    def check_querys(self, querys):
        def _on_lamp_axis(qy):
            X = 0
            Y = 1
            is_lit = False

            for lamp in self.lamps:
                l_coord = lamp[0]
                is_on = lamp[1]
                if is_on and (qy[X] == l_coord[X] or qy[Y] == l_coord[Y]):
                    is_lit = True

            return is_lit

        def _on_diagonal(qy):
            ON = 1

            for key in self.lit_diagonals:
                if self.lamps[key][ON] and qy in self.lit_diagonals[key]:
                    return True
            return False

        are_illuminated = []

        for qy in querys:
            if _on_lamp_axis(qy):
                are_illuminated.append(True)
            else:
                are_illuminated.append(_on_diagonal(qy))

        return are_illuminated

    def whats_illuminated(self):
        strng = str(self) + "\n\taxis:\n\t\tx:{0}\n\t\ty:{1}\n\tdiagonals:{2}"
        x = [x[0][0] for x in self.lamps if x[1] == True]
        y = [y[0][1] for y in self.lamps if y[1] == True]
        diagonals = ""
        for i in self.lit_diagonals:
            diagonals = diagonals + \
                "\n\t\t{0}: {1}".format(i, self.lit_diagonals[i])

        return strng.format(x, y, diagonals)


class IntGrid(object):

    def __init__(self, size, lamps):
        self.lamps = lamps
        self.cols = [0 for _ in range(size)]
        self.rows = [0 for _ in range(size)]
        self.l_diags = [0 for _ in range((size - 1)*2 + 1)]
        self.r_diags = [0 for _ in range((size - 1)*2 + 1)]

        self._add_lamps()

    def _add_lamps(self):
        for lamp in self.lamps:
            l_x = lamp[0]
            l_y = lamp[1]

            self.cols[l_x] += 1
            self.rows[l_y] += 1
            self.l_diags[l_x + l_y] += 1
            self.r_diags[l_x - l_y] += 1

    def _remove_lamp(self, lamp):
        l_x = lamp[0]
        l_y = lamp[1]

        self.cols[l_x] -= 1
        self.rows[l_y] -= 1
        self.l_diags[l_x + l_y] -= 1
        self.r_diags[l_x - l_y] -= 1

        self.lamps.remove(lamp)

    def query_me(self, x, y):
        possible_turn_offs = [[x, y], [x + 1, y], [x - 1, y], [x, y + 1], [
            x, y - 1], [x + 1, y + 1], [x - 1, y - 1], [x + 1, y - 1], [x - 1, y + 1]]
        for postion in possible_turn_offs:
            if postion in self.lamps:
                self._remove_lamp(postion)

        if self.cols[x] > 0 or self.rows[y] > 0 or self.l_diags[x + y] > 0 or self.r_diags[x - y] > 0:
            return ""

    def query_these(self, queries):
        results = []
        X = 0
        Y = 1
        for query in queries:
            results.append(self.query_me(query[X], query[Y]))

        return results


'''
    def _init_lit(self, lamps):
        def find_upper_diagonals(lamp):
            lit_squrs = []

            left_x = lamp[0]
            right_x = lamp[0]
            for y_cord in range(lamp[1] - 1, -1, -1):
                if right_x > 0 and right_x < self.SIZE:
                    right_x -= 1
                    lit_squrs.append([right_x, y_cord])
                if left_x > 0 and left_x < self.SIZE:
                    left_x += 1
                    lit_squrs.append([left_x, y_cord])

            return lit_squrs

        def find_lower_diagonals(lamp):
            lit_squrs = []

            left_x = lamp[0]
            right_x = lamp[0]

            for y_cord in range(lamp[1] + 1, self.SIZE):
                if right_x > 0 and right_x < self.SIZE:
                    right_x -= 1
                    lit_squrs.append([right_x, y_cord])
                if left_x > 0 and left_x < self.SIZE:
                    left_x += 1
                    lit_squrs.append([left_x, y_cord])

            return lit_squrs
        lit = {}

        for lamp in lamps:
            lit[lamp] = []
'''

if __name__ == "__main__":
    grids_size = 1000000
    l1 = [[0, 0]]
    l2 = [[0, 0], [0, 1], [1, 0], [1, 1]]

    q1 = [
        [0, 0], [0, 1], [0, 2], [0, 3],
        [1, 0], [1, 1], [1, 2], [1, 3],
        [2, 0], [2, 1], [2, 2], [2, 3],
        [3, 0], [3, 1], [3, 2], [3, 3]
    ]

    ng = IntGrid(grids_size, l1)
    print("done")
    print(ng.query_these(q1))

    #g1 = Grid(grids_size, l2)
    # print("done")
    # print(g1.whats_illuminated())
    # print(g1.check_querys(q1))
    #g2 = Grid(grids_size, l2)
    # print(g2.whats_illuminated())

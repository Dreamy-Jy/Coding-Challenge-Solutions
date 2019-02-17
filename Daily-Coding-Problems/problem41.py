"""
🌩Dreamy Jy🌩 back it again ⚡️...

Daily Coding Problem: Problem #41

Given an unordered list of flights taken by someone, each represented as (origin, destination) 
pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, 
return null. If there are multiple possible itineraries, return the lexicographically smallest 
one. All flights must be used in the itinerary.

For example, given the list of flights 
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting 
airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and 
starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even 
though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one 
is lexicographically smaller.

NOTE
"""


def generate_itinerary(start, airports):

    # TODO make this only one loop
    itinerary = []

    # STEP 1:
    # find the first airport, we assume that it will always have at least
    # one entry with `start` as its [0]th value
    i = 0
    while i < len(airports):
        if airports[i][0] == start:
            itinerary.append(airports[i][0])
            itinerary.append(airports[i][1])
            del airports[i]
            i = len(airports)*2

        i += 1

    # print(itinerary[len(itinerary) - 1])
    # STEP 2:
    # Find the elements in the li
    while len(airports) > 0:
        last_place = itinerary[len(itinerary) - 1]
        port = 0
        STRT = 0
        END = 1

        stop = True
        while port < len(airports):
            stop = True
            if airports[port][STRT] == last_place:
                print("Something found: " + str(airports[port][END]))
                stop = False
                itinerary.append(airports[port][END])
                del airports[port]
                port += len(airports)*2

            port += 1
        if stop:
            print("Sorry No way to make this work")
            return None
    print(itinerary)
    print(airports)


def dynamic_solution(start, airports):
    def lex_ranking(route):
        return abs(ord(route[0][0])-ord(route[1][0]))

    STRT = 0
    END = 1
    itinerary = [start]

    while len(airports) > 0:

        port = 0
        pair_ranking = 27
        pair = None

        while port < len(airports):
            if (
                airports[port][STRT] == itinerary[len(itinerary) - 1] and
                lex_ranking(airports[port]) < pair_ranking
            ):
                pair = airports[port]
                pair_ranking = lex_ranking(pair)
            port += 1

        if pair == None:
            print("Empty Set Returned")
            return None

        itinerary.append(pair[END])
        airports.remove(pair)

    print(itinerary)
    return itinerary


if __name__ == "__main__":
    dynamic_solution(
        'YUL', [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')])
    dynamic_solution('COM', [('SFO', 'COM'), ('COM', 'YYZ')])
    dynamic_solution('A', [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')])
    dynamic_solution('A', [('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')])

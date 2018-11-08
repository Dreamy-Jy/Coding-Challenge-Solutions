"""
Q7. backpack (Knapsack) problem
Given a set of different items, each one with an associated value 
and weight, determine which items you should pick in order to 
maximize the value of the items without surpassing the capacity 
of your backpack

	  First 	Second 	Third 	Fourth 	Fifth
Value:	$5	 	$7($10)	$3		$2		$3
Weight:	 4 kg	 8 kg	 3 kg	 5 kg	 2 kg

backpack's weight limit is 10

(try dynamic programming)
"""
"""
set of items takes in a tuples of prices, & weights: (prices: int, weights: int).

all weights are assumpted to be in the range (0, MAX).
prices are assumed to between (0, ∞).

your answer should be a list of tuples representing the items you'd like to put in the bag.
"""
MAX = 10

def pack_knap_sack(item_list):
    pass
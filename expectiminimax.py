'''
    ---------------------------GAME DESCRIPTION----------------------------------------

    The game chosen for this implementation is a two player game with the objective
    of attaining a score of 24 exactly. Each turn, before both players roll the dice,
    they choose whether or not to add the value of the dice to player a's score.

    Both players start with a score of 0. So, each turn, the player rolls the dice
    and has two choices, to add or not add the score.


    Player A wins if he attains a score of 24 exactly. However, if he overshoots
    and gets a score greater than 24, he loses. The first player to attain this score
    exactly wins.


    The chance involved in this game is the rolling of dice which is outside the control
    of the players. The assumption is that both dice used are normal six sided dice.


    The strategy used by both players is to take the choice which minmizes the difference
    between 24 and the current score if each of the dice is chosen.

    This strategy is is modified slightly in the case of an overshoot case, in which one
    die gives an output which results in a sum that is greater than 24. In this case, the
    other die is selected. In the case that both dice give an overshoot, the other player
    wins anyway.

    -------------------------------------------------------------------------------------
'''

import random


class dice:

    def __init__(self):
        self.outcomes = [1,2,3,4,5,6]

    def roll(self):
        return random.choice(self.outcomes)
        

class Player:

    def __init__(self):
        self.score=0
        self.won=False

    def add_score(score):
        self.score = self.score+score
        if(self.score==24):
            self.won=True

    def get_score(self):
        return self.score

    def score_greater_than_24(self):
        if(score>24):
            return True
        return False

    def score_less_than_24(self):
        if(score<=24):
            return True
        return False

    def did_win(self):
        if(self.score==24):
            return True
        return False

class node:

    def __init__(self,state,terminal):
        self.state = state
        self.utility = 0
        self.terminal = terminal

class Binary_Tree:

    def __init__(self,right,left,utility):
        self.right = right
        self.left = left
        self.utility = utility

    def get_child(self):
        return self

    def are_children_None(self):
        if(self.left==None and self.right==None):
            return True
        return False

    def print_children(self):

        print(str(self.left)+" "+str(self.right))
        
class Six_Tree:

    def __init__(self,one,two,three,four,five,six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

    def get_child(self):
        return self.one

    def are_children_None(self):
        if(self.one==None and self.two==None and self.three==None and self.four==None and self.five==None and self.six==None):
            return True
        return False

    def print_children(self):
        print(str(self.one)+" "+str(self.two)+str(self.three)+" "+str(self.four)+" "+str(self.five)+" "+str(self.six))

def alpha_beta_pruning(game_tree):
    alpha = 0
    beta = 0
    for i in range(24):
        game_tree.left = None
        alpha = game_tree.right.six.right.utility
        game_tree = game_tree.right.six

def expectimax_algorithm(game_tree):
    expectimax_path = game_tree
    for i in range(24):
        if(expectimax_path.right != None):
            expectimax_path = expectimax_path.right.six
        if(expectimax_path.left != None):
            expectimax_path = expectimax_path.left.one
    return expectimax_path

    
def expand_tree(binary_tree):
    binary_tree.right = Six_Tree(Binary_Tree(None,None,binary_tree.utility+1),Binary_Tree(None,None,binary_tree.utility+2),Binary_Tree(None,None,binary_tree.utility+3),Binary_Tree(None,None,binary_tree.utility+4),Binary_Tree(None,None,binary_tree.utility+5),Binary_Tree(None,None,binary_tree.utility+6))
    binary_tree.left = Six_Tree(Binary_Tree(None,None,binary_tree.utility),Binary_Tree(None,None,binary_tree.utility),Binary_Tree(None,None,binary_tree.utility),Binary_Tree(None,None,binary_tree.utility),Binary_Tree(None,None,binary_tree.utility),Binary_Tree(None,None,binary_tree.utility))
    return binary_tree

def get_last_child(game_tree):

    while not(game_tree.are_children_None()):
         game_tree = game_tree.get_child()
    
    return game_tree


def form_game_tree():

    game_tree = Binary_Tree(None,None)

    for i in range(24):
        expand_tree(game_tree)
        game_tree = get_last_child(game_tree)

    return game_tree

def print_tree(game_tree):

    while True:
        game_tree.print_children()
        if game_tree.are_children_None():
            break;
        game_tree = game_tree.left.one

    
    
MAX = Player()
MIN = Player()

die = dice()

# GAME TREE IS THE FULL GAME TREE
# LEFT IS DECISION NOT TO ADD SCORE RIGHT IS DECISION TO ADD SCORE

game_tree = Binary_Tree(None,None,0)

for i in range(24):
    game_tree = expand_tree(game_tree)

expectimax_algorithm(game_tree)
alpha_beta_pruning(game_tree)

'''
    ---------------------------GAME DESCRIPTION----------------------------------------

    The game chosen for this implementation is a two player game with the objective
    of attaining a score of 24 exactly. Each turn, player A rolls two dice and chooses
    which number to add to his score.

    Both players start with a score of 0. So, each turn, the player rolls the dice
    and has two choices, the number shown by dice one or the number shown by dice two.


    A player wins if he attains a score of 24 exactly. However, if a player overshoots
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


'''

    Dice class representing an ordinary six-sided dice. The dice is not weighted and the
    roll function outputs a random number between one and six.

'''

class dice:

    def __init__(self):
        self.outcomes = [1,2,3,4]

    def roll(self):
        return random.choice(self.outcomes)
        
'''
    Adversarial agent in MAX position playing the game described above
'''

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
        if(score>24)
            return True
        return False

    def score_less_than_24(self):
        if(score<=24)
            return

    def did_win()
        if(self.score==24):
            return True
        return False

'''
    Node in expectimax tree

    State 0: MAX NODE
          1: MIN NODE
          2: CHANCE NODE
    
'''
class node:

    def __init__(self,state,terminal):
        self.state = state
        self.utility = 0
        self.terminal = terminal

class Binary_Tree:

    def __init__(self,right,left):
        self.right = right
        self.left = left

    def get_children(self):
        return [left,right]

    def are_children_None(self):
        if(self.left==None and self.right==None):
            return True
        return False
        
class Six_Tree:

    def __init__(self,one,two,three,four,five,six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

    def get_children(self):
        return [one,two,three,four,five,six]

    def are_children_None(self):
        if(self.one==None and self.two==None and self.three==None and self.four==None and self.five==None and self.six==None):
            return True
        return False
    
        



MAX = Player()
MIN = Player()




tree = Binary_Tree(None,None)
trees.right = six_Tree(Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None))
trees.left = six_Tree(Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None),Binary_Tree(None,None))
        


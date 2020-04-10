class max_node:
    
    def __init__(self,parent,parent_chance,terminal,utility):

        self.parent = parent
        self.parent_chance = parent_chance
        self.terminal = terminal
        self.utility = utility
        self.children = []


class min_node:

    def __init__(self,parent,parent_chance,terminal,utility):

        self.parent = parent
        self.parent_chance = parent_chance
        self.terminal = terminal
        self.utility = utility
        self.children = []

class tree:

    def __init__(self,levels):

        self.levels = levels;
        
        for i in range(levels):

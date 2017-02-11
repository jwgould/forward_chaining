"""
fc.py is a tic-tac-toe solver which uses a txt file
knowledge-base and forward chaining to suggest moves
"""
# Jason Gould
# File Created: November 16, 2016
# File Edited:  November 20, 2016
# -----------------------------------
# Forward Chaining Tic-Tac-Toe Solver
# Accepts input as follows:
# -----------------------------------
# x b x
# b b b
# o b o
# ABOVE board-state input as:
# > python fc.py ttt.kb "x11 b12 x13 b21 b22 b23 o31 b32 o33 turn_o"
# ...
# move_o32_can_win
# --------------------------------------------------------------------------
# NOTE ttt.kb is knowledge base of positive literals followed by a consonant
# A B C D  which means A ^ B ^ C -> D
# Propositional symbos can have multiple characters, digits, and underscore
# --------------------------------------------------------------------------

import sys

def main():
    """
    Main function
    """
    if len(sys.argv) > 2:                  # check for args
        sys.argv.pop(0)                    # remove first arg
        kb_file = sys.argv.pop(0)          # get the kb filename
        state = sys.argv.pop(0)            # get the board state

        knowledge = parse_kb_file(kb_file) # parse the KNOWLEDGE BASE - KB
        agenda = state.split(' ')          # split the board state symbols

        inferred = []                      # to hold the inferred conclusions
        # Perform forward chaining
        inferred = forward_chain(agenda, knowledge, inferred)

        print "Board State: " + state
        print "..."
        if len(inferred) > 0:
            print_suggested_move(inferred)

        else:
            print "No move inferred..."
    else:
        print"Error: Not enough input arguments."

def forward_chain(agenda, knowledge, inferred):
    """
    Performs a rough version of the forward chaining algorithm to determine
    which moves are possible given the available knowledge-base and agenda
    (board state) as input.
    """
    while agenda:
        item = agenda.pop(0)
        # Search the KB for each agenda item, change predicates to True
        for rule in knowledge:
            for j, premise in enumerate(rule[0]):
                if premise == item:             # if the proposition is found
                    rule[0][j] = True
            # Check if entire hypothesis true (then conclusion becomes true)
            if check_hypothesis(rule[0]):
                conclusion = rule[1]
                inferred.append(conclusion)
                agenda.append(conclusion)
                rule[0] = ['processed']
    return inferred

def check_hypothesis(hypothesis):
    """
    Checks if the entire list of propositions in a
    hypothesis list have been converted to True
    """
    for entry in hypothesis:
        if entry != True:
            return False
    return True

def parse_kb_file(filename):
    """
    Opens, reads and parses the knowledge base from a file and returns
    a list of lists that contain an antecedant and conclusion
    """
    kb_file = open(filename, 'rU')        # 'rU' is smart about line-endings
    kb_rules = []                         # to hold the list of rules

    for line in kb_file:                  # read the non-commented lines
        if not line.startswith('#') and line != '\n':
            kb_rules.append(split_and_build_literals(line.strip()))

    kb_file.close()
    return kb_rules


def split_and_build_literals(line):
    """
    Takes a string of literals, splits it on the spaces, then builds and
    returns a formatted list ex: [['b11'],['x12'],['x13'], 'x11_can_win']
    """
    rules = []
    # Split the line of literals
    literals = line.split(' ')

    hypothesis = []
    while len(literals) > 1:
        hypothesis.append(literals.pop(0))
    rules.append(hypothesis)
    rules.append(literals.pop(0))

    return rules

def print_suggested_move(inferred):
    for i, entry in enumerate(inferred):
        if 'move' in entry and 'can_win' in entry:
            print inferred.pop(i)
            return
    for i, entry in enumerate(inferred):
        if 'move' in entry and 'forced' in entry:
            print inferred.pop(i)
            return
    for i, entry in enumerate(inferred):
        if 'move' in entry and 'setup' in entry:
            print inferred.pop(i)
            return
    else:
        # print the last conclusion found
        print inferred.pop()

# Standard code to run main() function
if __name__ == '__main__':
    main()

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    # from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    start = problem.getStartState()
    start_state = problem.getStartState()
    explored_state = [start]
    states = util.Stack()
    state_tuple = (start, [])
    states.push(state_tuple)
    while not states.isEmpty() and not problem.isGoalState(start_state):
        state, actions = states.pop()
        explored_state.append(state)
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if coordinates not in explored_state:
                start_state = i[0]
                direction = i[1]
                states.push((coordinates, actions + [direction]))
    return actions + [direction]


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    DICA: Utilizar util.PriorityQueue
    *** YOUR CODE HERE ***
    """
    start = problem.getStartState()
    start_state = problem.getStartState()
    explored_state = [start]
    states = util.Queue()
    state_tuple = (start, [])
    states.push(state_tuple)
    while not states.isEmpty() and not problem.isGoalState(start_state):
        state, actions = states.pop()
        explored_state.append(state)
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if coordinates not in explored_state:
                start_state = i[0]
                direction = i[1]
                states.push((coordinates, actions + [direction]))
    return actions + [direction]

    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    start_state = problem.getStartState()
    explored_state = [start]
    states = util.Queue()
    state_tuple = (start, [])
    states.push(state_tuple)
    while not states.isEmpty() and not problem.isGoalState(start_state):
        state, actions = states.pop()
        explored_state.append(state)
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if coordinates not in explored_state:
                start_state = i[0]
                direction = i[1]
                states.push((coordinates, actions + [direction]))
        """Ordering the stack at cost"""
        states.list = sorted(states.list, key=lambda x: problem.getCostOfActions(x[1]))
    return actions + [direction]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start_state = problem.getStartState()
    open_list = [(start_state, '', 0)]
    closed_list = []
    while len(open_list) > 0:
        current = open_list.pop()
        for successor in problem.getSuccessors(current[0]):
            if problem.isGoalState(successor):
                break
            successor_cost = current[2]+successor[2] + heuristic(successor, problem)
            actions = (current[1] or []) + [successor[1]]
            t = (successor[0], actions, successor_cost)
            if t[0] not in [i[0] for i in open_list] and t[0] not in [i[0] for i in closed_list]:
                open_list.insert(0, t)
        closed_list.insert(0, current)
    return closed_list[0][1]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


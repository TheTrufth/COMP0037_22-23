from math import sqrt, dist
from queue import PriorityQueue

from .planner_base import PlannerBase

class GreedyShortestDistancePlanner(PlannerBase):

    # This order the cells on a priority queue, sorted in terms of distance to target: shorter is better
    
    def __init__(self, occupancyGrid):
        PlannerBase.__init__(self, occupancyGrid)
        self._priority_queue = PriorityQueue()

    # Sort in order of distance from the target and use that
    def push_cell_onto_queue(self, cell):

        # Q4a:
        # Complete the implementation of the priority queue with the
        # priority p being the Euclidean distance from the cell to
        # the goal.
        p = dist(self.goal.coords(), cell.coords())

        # Q4b:
        # Change the priority to 10^6-p.
        
        # self._priority_queue.put((p, cell))
        self._priority_queue.put(((10 ** 6) - p, cell))

    # Check the queue size is zero
    def is_queue_empty(self):
        return self._priority_queue.empty()

    # Simply pull from the front of the list
    def pop_cell_from_queue(self):
        t = self._priority_queue.get()
        return t[1]

    def resolve_duplicate(self, cell, parent_cell):
        # Nothing to do in this case
        pass

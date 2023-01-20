#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.greedy_shortest_distance_planner \
    import GreedyShortestDistancePlanner

# Create the occupancy grid
occupancy_grid = OccupancyGrid("Greedy Shortest Distance Example", 21, 21, 0.5)

# Change to range(1, 20) for the simpler example
for y in range(0, 20):
    occupancy_grid.set_cell(11, y, 1)

start = (0, 20)
goal = (20, 0)

planner = GreedyShortestDistancePlanner(occupancy_grid)
planner.set_pause_time(0.01)
planner.update_graphics_each_iteration(True)

# Run the planner to work out the path from the start to the goal
planner.plan(start, goal)

search_grid_drawer = planner.search_grid_drawer()
    
# Pause
search_grid_drawer.wait_for_key_press()
    
# Show the path

planner.extract_path_to_goal()

# Pause again
search_grid_drawer.wait_for_key_press()

# Set some configuration values for showing the graphics. On different
# OS combinations, the update can be very fast or very slow. If it's
# slow, set update_graphics_each_iteration to False.

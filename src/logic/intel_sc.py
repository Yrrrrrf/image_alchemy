import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt  # for visualization


def get_cost_matrix(image: np.ndarray) -> np.ndarray:
    """
    Compute the cost matrix of an image.

    ## Steps:
        - Convert the image to grayscale
        - Apply Canny edge detection
        - Compute the gradient of the image
        - Compute the cost matrix
            - f(x, y) = 1 / (gradient_cost + direction_cost + laplacian_cost + 1e-6)

    ## Arguments:
        - image: `np.ndarray`: the image

    ## Returns:
        - cost_matrix: `np.ndarray`: the cost matrix
    """
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # * Canny edge detection
    # low_threshold = image.mean() * 0.66
    # upper_threshold = image.mean() * 1.33
    lower_threshold = 32
    upper_threshold = 100
    # img_std = np.std(image)  # type: ignore
    # lower_threshold = image.mean() - img_std
    # upper_threshold = image.mean() - 0.66 * img_std
    # * Canny edge detection
    edges = cv.Canny(gray_image, lower_threshold, upper_threshold)
    # * Gradient
    gradient_x: np.ndarray = cv.Sobel(edges, cv.CV_64F, 1, 0, ksize=3)  # type: ignore
    gradient_y: np.ndarray = cv.Sobel(edges, cv.CV_64F, 0, 1, ksize=3)  # type: ignore
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_direction = cv.phase(gradient_x, gradient_y)
    # * Calculate the cost matrix
    return np.vectorize(lambda gradient_magnitude, gradient_direction: 
        1.0 / (  # * the reciprocal of the sum of the costs
            0.14 * gradient_magnitude +  # ^ the gradient cost
            0.43 * (1 - np.cos(gradient_direction)) +  # ^ the direction cost 
            0.43 * (1 - np.tanh(gradient_magnitude / 255.0)) +   # ^ the laplacian cost
            1e-6  # to avoid division by zero
        ))(gradient_magnitude, gradient_direction)  # * Apply the function to each element of the matrix


# route_image = draw_path(cost_matrix, test_path)


# ? dijkstra ------------------------------------------------------------------------
import networkx
# NetworkX is a Python library for studying graphs and networks.
# https://networkx.github.io/documentation/stable/index.html

# This function finds the minimum cost path between two points in the image 
def find_minimum_cost_path(cost_matrix, start_point, end_point):
    height, width = cost_matrix.shape
    G = networkx.Graph()

    for y in range(height):  # For all columns
        for x in range(width):  # For all rows
            G.add_node((y, x))  # Add the node to the graph

    neighbors = [  # Define neighbors for 8-connected pixels
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
        ]

    for y in range(height):  # For all columns
        for x in range(width):  # For all rows
            for dy, dx in neighbors:  # Add edges between neighboring pixels
                ny, nx = y + dy, x + dx  # Calculate the neighbor's coordinates
                if 0 <= ny < height and 0 <= nx < width:  # Check if the neighbor is within the image
                    G.add_edge((y, x), (ny, nx), weight=cost_matrix[y, x])  # Add the edge to the graph

    try:  # Find the shortest path using Dijkstra's algorithm
        return networkx.shortest_path(G, source=start_point, target=end_point, weight='weight')
    except networkx.NetworkXNoPath:  # If the path does not exist
        return []  # Return an empty path


import heapq

# Own implementation of Dijkstra's algorithm
def dijkstra(cost_matrix, start, end):
    height, width = cost_matrix.shape  # Get dimensions of the cost matrix
    visited = np.zeros((height, width), dtype=bool)  # Create a 2D array to track visited nodes
    min_cost = np.inf * np.ones((height, width))  # Create a 2D array to store the minimum cost to reach each pixel
    min_cost[start[0], start[1]] = 0  # Initialize the starting point
    priority_queue = [(0, start)]  # Create a priority queue to store pixels and their costs
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # Define possible moves (8-connectivity)

    while priority_queue:
        current_cost, (y, x) = heapq.heappop(priority_queue)  # Get the pixel with the minimum cost
        visited[y, x] = True  # Mark the pixel as visited
        if (y, x) == end: break  # Check if we reached the end point
        for dy, dx in moves:  # Explore neighbor pixels
            ny, nx = y + dy, x + dx
            # Check if the neighbor is within bounds
            if 0 <= ny < height and 0 <= nx < width and not visited[ny, nx]:
                neighbor_cost = current_cost + cost_matrix[ny, nx]  # Calculate the cost to reach the neighbor
                if neighbor_cost < min_cost[ny, nx]:  # If the new cost is lower than the current cost, update it
                    min_cost[ny, nx] = neighbor_cost
                    heapq.heappush(priority_queue, (neighbor_cost, (ny, nx)))

    # Backtrack to find the path
    path = []
    y, x = end
    while (y, x) != start:
        path.append((y, x))
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width and min_cost[y, x] == min_cost[ny, nx] + cost_matrix[y, x]:
                y, x = ny, nx
                break
    path.append(start)
    path.reverse()
    return path

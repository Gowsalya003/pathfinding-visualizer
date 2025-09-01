import pygame
import heapq

def dijkstra(draw, grid, start, end):
    count = 0
    pq = [(0, count, start)]
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0
    came_from = {start: None}
    visited = set()

    while pq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_dist, _, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == end:
            while current in came_from and came_from[current]:
                current = came_from[current]
                current.make_path()
                draw()
                pygame.time.delay(30)
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor.is_barrier():
                continue
            new_dist = current_dist + 1
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                came_from[neighbor] = current
                count += 1
                heapq.heappush(pq, (new_dist, count, neighbor))
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()
        pygame.time.delay(30)

    return False

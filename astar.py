import pygame
import heapq

def h(p1, p2):
    # Manhattan distance
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def astar(draw, grid, start, end):
    count = 0
    pq = [(0, count, start)]
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    came_from = {start: None}
    visited = set()

    while pq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        _, _, current = heapq.heappop(pq)

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

            temp_g = g_score[current] + 1
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + h(neighbor.get_pos(), end.get_pos())
                count += 1
                heapq.heappush(pq, (f_score[neighbor], count, neighbor))
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()
        pygame.time.delay(30)

    return False

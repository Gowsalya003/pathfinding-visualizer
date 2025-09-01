import pygame
from collections import deque

def bfs(draw, grid, start, end):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()

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
            if neighbor not in came_from and not neighbor.is_barrier():
                came_from[neighbor] = current
                queue.append(neighbor)
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()
        pygame.time.delay(30)

    return False

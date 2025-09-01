import pygame

def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {start: None}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

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
                stack.append(neighbor)
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()
        pygame.time.delay(30)

    return False

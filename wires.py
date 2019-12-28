#!/usr/bin/env python3


def get_coordinates(trace):
    x = 0
    y = 0
    coordinates = [(x, y)]
    for movement in trace.split(','):
        new_x = 0
        new_y = 0
        if movement.startswith('R'):
            new_x = int(movement.replace('R', ''))
        if movement.startswith('L'):
            new_x = 0 - int(movement.replace('L', ''))
        if movement.startswith('U'):
            new_y = int(movement.replace('U', ''))
        if movement.startswith('D'):
            new_y = 0 - int(movement.replace('D', ''))
        if new_x != 0:
            for _ in range(abs(new_x)):
                if new_x > 0:
                    x += 1
                else:
                    x -= 1
                coordinates.append((x, y))
        if new_y != 0:
            for _ in range(abs(new_y)):
                if new_y > 0:
                    y += 1
                else:
                    y -= 1
                coordinates.append((x, y))
    return coordinates


def get_intersect(coordinates):
    return set(coordinates[0][1:]) & set(coordinates[1][1:])


def get_closest_distance(intersects):
    distances = []
    for element in intersects:
        x, y = element
        distances.append(abs(x)+abs(y))
    return min(distances)


if __name__ == '__main__':
    coordinates = []
    with open('traces.txt') as traces:
        for trace in traces:
            coordinates.append(get_coordinates(trace))

    intersections = get_intersect(coordinates)
    distance = get_closest_distance(intersections)
    print(distance)
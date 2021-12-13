import collections
from copy import copy, deepcopy


class Cave:
    def __init__(self, name):
        self.name = name
        self.is_large = name.isupper()
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Solution:

    def __init__(self):
        self.caves = {}
        self.inbound_connections = collections.defaultdict(list)
        self.outbound_connections = collections.defaultdict(list)

    def read_input(self):
        input_file = open("input_012_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            from_cave, to_cave = input_line.split('-')
            self.inbound_connections[from_cave].append(to_cave)
            if from_cave != "start" and to_cave != "end":
                self.outbound_connections[to_cave].append(from_cave)

        input_file.close()

    def build_tree(self):
        for from_cave, to_caves in self.inbound_connections.items():
            if from_cave not in self.caves:
                self.caves[from_cave] = Cave(from_cave)
            for to_cave in to_caves:
                if to_cave not in self.caves:
                    self.caves[to_cave] = Cave(to_cave)

        for from_cave, to_caves in self.outbound_connections.items():
            if from_cave not in self.caves:
                self.caves[from_cave] = Cave(from_cave)
            for to_cave in to_caves:
                if to_cave not in self.caves:
                    self.caves[to_cave] = Cave(to_cave)

        for from_cave, to_caves in self.inbound_connections.items():
            for to_cave in to_caves:
                self.caves[from_cave].add_child(self.caves[to_cave])
        for from_cave, to_caves in self.outbound_connections.items():
            for to_cave in to_caves:
                self.caves[from_cave].add_child(self.caves[to_cave])

    def dfs(self, node, target, visited, path_count):

        if not node.is_large:
            visited.add(node.name)

        if node == target:
            path_count[0] += 1
        else:

            for child in node.children:
                if child.name not in visited:
                    self.dfs(child, target, visited, path_count)

        if node.name in visited:
            visited.remove(node.name)



    def dfs_2(self, node, target):
        visited = set()
        stack = [node]
        level = 0

        while len(stack) > 0:
            cur = stack.pop()
            print("{}. {}".format(level, cur.name))
            level += 1
            if cur == target:
                return True

            for child in cur.children:
                if child.name not in visited:
                    stack.append(child)
                    if not child.is_large:
                        visited.add(child.name)
        return False


    def calculate(self):
        # print(self.inbound_connections)
        # print(self.outbound_connections)
        self.build_tree()

        for name, cave in self.caves.items():
            print("{} ({}): {}".format(cave.name, 'L' if cave.is_large else 'S', [c.name for c in cave.children]))

        path_count = [0]
        self.dfs(self.caves["start"], self.caves["end"], set(), path_count)
        print(path_count)


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())

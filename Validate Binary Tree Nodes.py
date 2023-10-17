class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        in_degree = [0] * n
        root_count = 0

        for i in range(n):
            if leftChild[i] != -1:
                in_degree[leftChild[i]] += 1
                if in_degree[leftChild[i]] > 1:
                    return False
            if rightChild[i] != -1:
                in_degree[rightChild[i]] += 1
                if in_degree[rightChild[i]] > 1:
                    return False

        for i in range(n):
            if in_degree[i] == 0:
                root_count += 1
                if root_count > 1:
                    return False

        if root_count != 1:
            return False

        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                root = i
                break

        visited = set()

        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)
            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(root) and len(visited) == n

# Example usage:
solution = Solution()
n = 4
leftChild = [1, 0, 3, -1]
rightChild = [-1, -1, -1, -1]
print(solution.validateBinaryTreeNodes(n, leftChild, rightChild))  # Output: False

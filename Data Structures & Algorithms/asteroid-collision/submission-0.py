class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True

            # collision coniditon: incoming is negative, top of stack is positive:
            while alive and ast < 0 and stack and stack[-1] > 0:
                if abs(ast) > stack[-1]:
                    # case top is smaller. Pop it and keep fighting
                    stack.pop()
                elif stack[-1] == abs(ast):
                    # Case: both are equal size. Pop stack and destory incoming
                    stack.pop()
                    alive = False
                else:
                    # Case top is bigger. Keep it and destory incoming
                    alive = False
            if alive:
                stack.append(ast)
        return stack


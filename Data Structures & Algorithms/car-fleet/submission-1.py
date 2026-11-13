class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = list(zip(position, speed))
        cars = sorted(cars, key=lambda x:x[0], reverse=True)

        for i in range(len(position)):
            time = (target - cars[i][0]) / cars[i][1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)


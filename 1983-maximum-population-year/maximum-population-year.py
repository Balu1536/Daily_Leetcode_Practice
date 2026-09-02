class Solution:
    def maximumPopulation(self, logs):

        diff = [0] * 101

        for birth, death in logs:
            diff[birth - 1950] += 1
            diff[death - 1950] -= 1

        current = 0
        max_population = 0
        answer = 1950

        for i in range(101):

            current += diff[i]

            if current > max_population:
                max_population = current
                answer = 1950 + i

        return answer
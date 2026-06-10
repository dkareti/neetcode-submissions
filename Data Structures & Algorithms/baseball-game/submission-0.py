class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """Record the points for a baseball game."""
        scores = []
        result = 0
        for operation in operations:
            if operation == "+":
                first_score = int(scores[-1])
                second_score = int(scores[-2])
                scores.append(first_score + second_score)
            elif operation == "D":
                recent_score = int(scores[-1])
                scores.append(2*recent_score)
            elif operation == "C":
                scores.pop()
            else:
                scores.append(int(operation))

        return sum(scores)
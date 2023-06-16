class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n):
            element = ""
            if (i + 1) % 3 == 0: element ="Fizz"
            if (i + 1) % 5 == 0: element += "Buzz"
            result.append(element if element != "" else str(i + 1))
        return result
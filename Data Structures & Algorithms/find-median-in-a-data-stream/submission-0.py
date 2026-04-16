class MedianFinder:

    def __init__(self):
        self.numbers = []

    def addNum(self, num: int) -> None:
        self.numbers.append(num)

    def findMedian(self) -> float:
        size = len(self.numbers)
        self.numbers.sort()
        if size % 2 == 1:
            return float(self.numbers[(size-1)//2])
        else:
            n1 = self.numbers[size//2]
            n2 = self.numbers[size//2 - 1]
            return (n1 + n2) / 2
        
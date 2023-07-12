class MathDojo:

    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        for n in (num,) + nums:
            self.result += n
        return self.result

    def subtract(self, num, *nums):
        for n in (num,) + nums:
            self.result -= n
        return self.result


def main():
    md = MathDojo()
    result = md.add(2)
    result = md.add(result, 2, 5, 1)
    print(result)


if __name__ == "__main__":
    main()

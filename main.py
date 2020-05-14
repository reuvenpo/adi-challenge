
def solve(mul, base, max_len=100):
    solution = base  # starting position
    digit = len(str(base))

    while digit <= max_len and str(solution * mul) != (str(base) + str(solution // 10**(len(str(base))))):
        print('solution        =', solution)
        multiplied = str(solution * mul)
        print('solution * base =', multiplied)
        solution = int(multiplied[-digit:]+str(base))
        digit += 1

    return solution


def main():
    mul = 4
    base = 5

    solution = solve(mul, base)

    print('\nAnswer:')
    print(solution)
    print(solution * mul)


if __name__ == '__main__':
    main()

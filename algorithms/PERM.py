def main_PERM(fname):
    with open(fname, 'r') as f:
        number = f.readline()
    number = int(number)
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
    print(numbers)
    return permutations(numbers)


def permutations(numbers):
    permutation_list = []
    print(len(numbers))
    if len(numbers) == 1:
        print("end" + str(numbers))
        #print(numbers)
        return numbers
    else:
        for i in range(0, len(numbers)-1):
            temp = [numbers[i]]
            print(temp)
            print("Not me")
            if i == len(numbers)-1:
                new_numbers = [numbers[0:i]]
            else:
                new_numbers = numbers[0:i] + numbers[i+1:]
            print(new_numbers)
            print("This me")
            new_list = temp + permutations(new_numbers)
            print(new_list)
            print("This newlist")


    return permutation_list


if __name__ == '__main__':
    print(main_PERM('../datasets/PERM_1.txt'))  # pragma: no cover

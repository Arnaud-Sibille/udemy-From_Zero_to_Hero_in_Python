
def print_arr(arr):
    print(f"    1   2   3\n1 | {arr[0]} | {arr[1]} | {arr[2]} |\n2 | {arr[3]} | {arr[4]} | {arr[5]} | \n3 | {arr[6]} | {arr[7]} | {arr[8]} |")

def ft_replace(arr, symb):
    try:
        row, col = input("Enter row and column separated by a space: ").split()
    except:
        print("Please enter strictly 2 arguments")
        return 0
    try:
        r = int(row) - 1
        c = int(col) - 1
    except:
        print("Arguments must be integer")
        return 0
    if (r > 2 or r < 0 or c > 2 or c < 0):
        print("Invalid row or column")
        return 0
    if (arr[r * 3 + c] != ' '):
        print("Already occupied position")
        return 0
    else:
        arr[r * 3 + c] = symb
        return 1

def ft_won(arr):
    for i in range(3):
        if arr[i * 3] != ' ' and arr[i * 3] == arr[i * 3 + 1] == arr[i * 3 + 2]:
            return 1
    for j in range(3):
        if arr[j] != ' ' and arr[j] == arr[3 + j] == arr[6 + j]:
            return 1
    if arr[0] != ' ' and arr[0] == arr[4] == arr[8]:
        return 1
    if arr[6] != ' ' and arr[6] == arr[4] == arr[2]:
        return 1
    return 0

def main():
    arr = [' '] * 9
    i = 0
    symb = ['X', 'O']
    while (i < 9):
        print_arr(arr)
        print(f"Player{(i % 2) + 1}'s turn to play, where do you want to put your {symb[i % 2]}?")
        while (ft_replace(arr, symb[i % 2]) == 0):
            pass
        if ft_won(arr) == 1:
            print_arr(arr)
            print(f"Congratulation Player{(i % 2) + 1}, you won the game!")
            return 0
        i += 1
    print_arr(arr)
    print("The game ended in a draw")

if __name__ == "__main__":
    main()

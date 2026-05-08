move_count = 0

def hanoi(n, src, aux, dst):
    global move_count

    if n == 1:
        print(f"Move disk 1 from {src} -> {dst}")
        move_count += 1
        return

    hanoi(n-1, src, dst, aux)
    print(f"Move disk {n} from {src} -> {dst}")
    move_count += 1
    hanoi(n-1, aux, src, dst)    


print("Move sequence for n = 3:\n")
move_count = 0
hanoi(3, 'A', 'B', 'C')
print("\nTotal moves for n=3:", move_count)

move_count = 0
hanoi(4, 'A', 'B', 'C')
print("\nTotal moves for n=4:", move_count)
for i in range(10):  # Outer loop
    for j in range(10):  # Inner loop
        print(j * i, end='')
        if i <=j:
            break
        print()
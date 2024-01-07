import time

BAR_LEN = 24
elements = ['-', '\\', '|', '/']

def main():
    for i in range(BAR_LEN+1)    :
        frame = i % len(elements)
        print(f'\r[{elements[frame]*i:=<{BAR_LEN}}]', end=' ')
        time.sleep(0.2)
    print('')

    
if __name__ == "__main__":
    main()
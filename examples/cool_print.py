import time
import sys

# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=CarlOS

def cool_print(line, t_ms_line):
    nChars = len(line)
    sleep_time_per_ch = t_ms_line / nChars / 1000
    for i in range(nChars):
        print(line[i], end='')
        time.sleep(sleep_time_per_ch)
        sys.stdout.flush()
    print('')

def main():
    nameCarlos =   ["_________               __  ________    _________",
                    "\\_   ___ \\_____ _______|  | \\__     \\  /   _____/",
                    "/    \\  \\/\\__  \\\\_  __ \\  |  /   |   \\ \\_____  \\ ",
                    "\\     \\____/ __ \\|  | \\/  |_/    |    \\/        \\",
                    " \\______  (____  /__|  |___/\\_______  /_______  /",
                    "        \\/     \\/                   \\/        \\/ "]
  
    for line in nameCarlos:
        cool_print(line,500)

    
if __name__ == "__main__":
    main()
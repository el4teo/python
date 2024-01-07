from lib.pd_csv import PD_CSV as PD
from lib.colors import color as C
import sys
import os


PREFIX = 'I:\\dbs\\DB_AC_LCOE__FULL\\'
EXPORT_PATH = 'prpd_pngs\\'
N_MAX_FILES = 15

def export_csv(file_prpd):
    pd_file = PD(file_prpd)
    print(pd_file)
    filename = os.path.basename(pd_file.filename)
    pd_file.save_png(EXPORT_PATH + filename[:-3])

def read_names(listname):
    try:
        with open(listname, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except FileNotFoundError:
        return []
    
def get_filename():
    nargs = len(sys.argv)
    filename_list = ''
    if nargs < 2 or nargs > 2:
        print(C.RED + "Ivalid usage: You must provide an argument with the path of a *.names file" + C.END)
        print(C.YELLOW + r'Example: python prpd2png.py "full path\list_defs.names"'+ C.END)
        return filename_list
    for ar in sys.argv:
        print(ar)
    try:
        filename_list = sys.argv[1]
        if filename_list.endswith(".names"):
            print(f"Reading file: '{filename_list}'")
        else:
            print(C.RED + f"'{sys.argv[1]}' is not an existing file or does not end with .names." + C.END)
            return ''
    except Exception as e:
        print(C.RED + "Unable to read the *.names file" + C.END)
    return filename_list
    
def main():
    os.makedirs(EXPORT_PATH, exist_ok=True)
    list_names = get_filename()
    if(list_names == ''):
        return
    
    cont = 0
    defects = read_names(list_names)
    for defect in defects:
        export_csv(PREFIX + defect)
        cont = cont + 1
        if cont == N_MAX_FILES:
            break


if __name__ == "__main__":
    main()

# Calling example:
# python .\python\PDs\tools\prpd2png.py "I:\repos\PDDB_Navigator\exported\comps\T5 Cavidad en sólido en SF6.names"
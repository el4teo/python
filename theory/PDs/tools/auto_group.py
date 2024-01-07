from lib.pd_csv import PD_CSV as PD
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import struct

COMP_FILE = r'I:\repos\PDDB_Navigator\exported\comps\231031_1906\T5 Cavidad en solido.pdcmp'
NAME_FILE = r'I:\repos\PDDB_Navigator\exported\comps\T5 Cavidad en solido.names'
PREFIX = 'I:\\dbs\\DB_AC_LCOE__FULL\\'

COMP_FILE = r'I:\repos\PDDB_Navigator\exported\comps\231031_1900\HF T5 Void.pdcmp'
NAME_FILE = r'I:\repos\PDDB_Navigator\exported\comps\HF T5 Void.names'
PREFIX = 'I:\\dbs\\AC0\\'

def read_pdcmp(filename):
    try:
        with open(filename, 'rb') as file:
            # Get the file size
            file_size_bytes = file.seek(0, 2)
            file.seek(0)
            # Calculate the number of readings and read the data
            n_comps = file_size_bytes // 4
            float_data = np.fromfile(file, dtype=np.float32, count=n_comps)
    except FileNotFoundError:
        print("Failed to open the file.")
    return float_data

def read_names(listname):
    try:
        with open(listname, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except FileNotFoundError:
        return []
    
def firstTimeF1(n_files, idxF1):
    n_comps = n_files * (n_files - 1) / 2;
    return n_comps - ((n_files-idxF1) * (n_files-idxF1 - 1) / 2) 

def idxInArr(n_files, idxF1, idxF2):
    firstIdxF1 = firstTimeF1(n_files, idxF1)
    idxInArr = firstIdxF1 + idxF2 - idxF1 - 1
    return int(idxInArr)

def main():
    vals = read_pdcmp(COMP_FILE)
    names = read_names(NAME_FILE)
    n_files = len(names)
    n_comps = n_files * (n_files - 1) / 2;
    if n_comps != len(vals):
        print("Something strange happen.")
        return
    
    # Comparing two files
    idx_1 = 10
    idx_2 = 20
    idx_in_arr = idxInArr(n_files, idx_1, idx_2)
    pd_file_1 = PD(PREFIX + names[idx_1])
    pd_file_2 = PD(PREFIX + names[idx_2])
    print(pd_file_1)
    print(pd_file_2)
    print(f'\nSim. Idx.: {vals[idx_in_arr]:.4f}')
    pd_file_1.plot(show_plot=False)
    pd_file_2.plot(show_plot=False)
    plt.show()



if __name__ == "__main__":
    main()
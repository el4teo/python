import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

from pathlib import Path


class PD_CSV:
    def __init__(self, filename) -> None:
        if Path(filename).is_file() == False:
            raise Exception(f'ERROR: This is not a file: "{filename}"')
        
        self.filename = filename
        self.times = []
        self.phases = []
        self.amps = []
        self.absAmps = []

        self.n = 0
        self.maxAbsAmp = 0
        self.meanAbsAmp = 0
        self.stdAbsAmp = 0

        self.read_file()

    
    def __str__(self) -> str:
        rep_str = f'{self.filename}\n' + \
            f'  n = {self.n}\n' + \
            f'  maxAbs = {self.maxAbsAmp}\n'  + \
            f'  meanAbs = {self.meanAbsAmp}\n'  + \
            f'  stdAbs = {self.stdAbsAmp}'
        return rep_str
    
    def read_file(self):
        df = pd.read_csv(self.filename)
        # For CIGRE format use this header:
        # time_s,phase_deg,amp_10bit
        self.times = df['time[s]'].tolist()
        self.phases = df['angle[deg]'].tolist()
        self.amps = df['amplitude[mV]'].tolist()
        self.absAmps = [abs(value) for value in self.amps]
        self.n = df.shape[0]
        self.maxAbsAmp = np.max(self.absAmps)
        self.meanAbsAmp = np.mean(self.absAmps)
        self.stdAbsAmp = np.std(self.absAmps)
    
    def get_title(self) -> str:
        return os.path.splitext(os.path.basename(self.filename))[0]

    def plot(self, show_plot):
        plt.figure(self.get_title())

        x = np.linspace(0, 2 * np.pi, 101)
        x_deg = np.linspace(0, 360, 101)
        y = np.sin(x) * self.maxAbsAmp
        plt.plot(x_deg, y, color='#9A0000')

        plt.scatter(self.phases, self.amps, color='#001E9A', marker='.', s=10)
        plt.xlim(0, 360)
        plt.xticks([0, 90, 180, 270, 360])
        plt.grid(True)
        
        plt.xlabel('Phase angle (deg)')
        plt.ylabel('Amp. (mV)')
        plt.title(self.get_title())
        
        plt.gca().set_facecolor('lightgoldenrodyellow')
        if show_plot:
            plt.show()
    
    def save_png(self, file_png=''):
        if file_png=='':
            file_png=self.filename[:-3] + 'png'
        if file_png.endswith('.png') == False:
            file_png += '.png'
        self.plot(show_plot=False)
        plt.savefig(file_png)

def testing():
    cwd = os.getcwd()
    print(f'cwd: {cwd}')
    filename = r'python\PDs\ficheros\T5 003 absSign thMin -0.1 thMax 0.1.csv'
    print(filename[:-3] + 'png')

def main():
    origin_path = r'python\PDs\ficheros'
    origin_path = r'I:\dbs\pd\0. Ruido'
    origin_path = r'C:\Users\carlo\My Drive\lcoe\Carlos-UMP-LCOE\ruidos\Impulsional Noise'
    origin_path = r'I:\dbs\pd\CIGRE'
    # origin_path = os.getcwd()
    csv_files = glob.glob(os.path.join(origin_path, '*.csv'))

    for filename in csv_files:
        pd_file = PD_CSV(filename)
        print(pd_file)
        pd_file.save_png()
    # plt.show()

if __name__ == '__main__':
    main()
    # testing()
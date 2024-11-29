import numpy as np
import os 

if __name__ == "__main__":
    for zcond in ['const', 'line', 'squares']:
        for bcond in ['zero', 'linear']:
            for gcond in ['gauss', 'const']:
                for dt in ['5.0e-3', '1.0e-3', '5.0e-4']:
                    for tol in ['1.0e-3', '1.0e-5', '1.0e-9']:
                        
                        outpath = f"./ref-solutions/heat-1T/z{zcond}-b{bcond}-g{gcond}/T1_{dt}-{tol}.txt"
                        if os.path.exists(outpath):
                            data = np.loadtxt(outpath)
                            if data.shape[0] == 128*128:
                                print(outpath, " EXISTS")
                                exit()

                        cmd = "FreeFem++ heat-1T-Nonlinear_diffusion.edp " +\
                            f"-zeff {zcond} -beta {bcond} -g {gcond} " +\
                            f"-dt {dt} -tol {tol} " +\
                            f"-out {outpath}"
                        
                        os.system(cmd)
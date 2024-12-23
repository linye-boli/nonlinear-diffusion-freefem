import numpy as np
import os 

if __name__ == "__main__":
    zcond = 'squares'
    bcond = 'linear'
    gcond = 'const'

    for dt in ['1.0e-3', '5.0e-4']:
        for tol in ['1.0e-3', '1.0e-9']:
            
            outpath = f"./ref-solutions/heat-1T/z{zcond}-b{bcond}-g{gcond}/T1_{dt}-{tol}.txt"
            if os.path.exists(outpath):
                data = np.loadtxt(outpath)
                if data.shape[0] == 129*129:
                    print(outpath, " EXISTS")
                    exit()

            cmd = f"FreeFem++ heat-1T-z{zcond}.edp " +\
                f" -beta {bcond} -g {gcond} " +\
                f"-dt {dt} -tol {tol} " +\
                f"-out {outpath}"
            
            os.system(cmd)
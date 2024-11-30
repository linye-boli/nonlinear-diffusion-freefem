import numpy as np
import os 

if __name__ == "__main__":
    zcond = 'squares'
    bcond = 'linear'
    gcond = 'const'

    for dt in ['5.0e-4']:
        for tol in ['1.0e-9', '1.0e-3']:
            rootpath = f"./ref-solutions/heat-2T/z{zcond}-b{bcond}-g{gcond}"
            if not os.path.exists(rootpath):
                os.makedirs(rootpath)
            outpath = rootpath + f"/T2_{dt}-{tol}.txt"


            if os.path.exists(outpath):
                data = np.loadtxt(outpath)
                if data.shape[0] == 257*257:
                    print(outpath, " EXISTS")
                    exit()
            print("outpath : ", outpath)
            cmd = f"FreeFem++ heat-2T-z{zcond}.edp " +\
                f" -beta {bcond} -g {gcond} " +\
                f"-dt {dt} -tol {tol} " +\
                f"-out {outpath}"
            
            os.system(cmd)
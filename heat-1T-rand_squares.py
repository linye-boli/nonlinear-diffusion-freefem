import numpy as np
import os 
import argparse
np.random.seed(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='reference dataset generation')
    parser.add_argument('--n', type=int, default=1,
                        help='piece range')
    args = parser.parse_args()

    rand_pts = np.random.rand(1000, 4) * 12 
    for idx, pts in enumerate(rand_pts):

        if (idx >= args.n * 100) & (idx < (args.n+1)*100):
            outname = "./heat-1T-zsquares-blinear-gconst/sample_{:}.txt".format(str(idx).zfill(4))
            if os.path.exists(outname):
                pass
            else:
                cmd = "FreeFem++ heat-1T-zsquares.edp " +\
                    "-beta linear -g const " + \
                    "-dt 1.0e-3 -tol 1.0e-3 " +\
                    "-ax {:.4f} -ay {:.4f} -bx {:.4f} -by {:.4f} ".format(pts[0], pts[1], pts[2], pts[3]) +\
                    "-out " + outname
                print(cmd)
                os.system(cmd)
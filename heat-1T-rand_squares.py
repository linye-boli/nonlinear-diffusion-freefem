import numpy as np
import os 
np.random.seed(0)

if __name__ == "__main__":
    rand_pts = np.random.rand(1000, 4) * 12 
    for idx, pts in enumerate(rand_pts):
        cmd = "FreeFem++ heat-1T-Nonlinear_diffusion.edp " +\
              "-zeff squares -beta linear -g const " + \
              "-dt 1.0e-3 -tol 1.0e-3 " +\
              "-ax {:.4f} -ay {:.4f} -bx {:.4f} -by {:.4f} ".format(pts[0], pts[1], pts[2], pts[3]) +\
              "-out ./heat-1T-zsquares-blinear-gconst/sample_{:}.txt".format(str(idx).zfill(4))
        os.system(cmd)
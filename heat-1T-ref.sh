for zcond in const line squares 
do
    for bcond in zero linear
    do
        for gcond in gauss const
        do 
            for dt in 5.0e-3 1.0e-3 5.0e-4
            do
                for tol in 1.0e-3 1.0e-5 1.0e-9
                do
                    FreeFem++ heat-1T-Nonlinear_diffusion.edp -zeff $zcond -beta $bcond -g $gcond -dt $dt -tol $tol -out ./ref-solutions/heat-1T/z$zcond-b$bcond-g$gcond/T1_$dt-$tol.txt
                done
            done
        done
    done
done
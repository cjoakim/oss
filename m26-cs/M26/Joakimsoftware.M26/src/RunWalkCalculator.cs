using System;
using System.Collections.Generic;

// Instances of this class are used to calculate the elapsed time and average speed
// for a given set of walk and run intervals.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26 {
    public class RunWalkCalculator {

        public RunWalkCalculator() {

        }

        public RunWalkCalculation calculate(string runHHMMSS, string runPPM, string walkHHMMSS, string walkPPM, double miles) {

            RunWalkCalculation result = new RunWalkCalculation();
            result.runHHMMSS  = runHHMMSS;
            result.runPPM     = runPPM;
            result.walkHHMMSS = walkHHMMSS;
            result.walkPPM    = walkPPM;
            result.miles      = miles;

            ElapsedTime runDurationET  = new ElapsedTime(runHHMMSS);
            ElapsedTime runPaceET      = new ElapsedTime(runPPM);
            ElapsedTime walkDurationET = new ElapsedTime(walkHHMMSS);
            ElapsedTime walkPaceET     = new ElapsedTime(walkPPM);
            Distance mile = new Distance(1.0);
            Distance dist = new Distance((double) Math.Abs(miles));

            double intervalSeconds = runDurationET.secs + walkDurationET.secs;
            double runPercentage   = runDurationET.secs / intervalSeconds;
            double walkPercentage  = ((double) 1.0) - runPercentage;
            double runSeconds  = runPercentage * runPaceET.secs;
            double walkSeconds = walkPercentage * walkPaceET.secs;
            double avgSeconds  = runSeconds + walkSeconds;
            ElapsedTime avgET  = new ElapsedTime(avgSeconds);
            Speed  avgSpeed    = new Speed(mile, avgET);

            result.averageSpeed  = avgSpeed;
            result.projectedTime = avgSpeed.projectedTime(dist).asHHMMSS();
            return result;
        }
    }
}

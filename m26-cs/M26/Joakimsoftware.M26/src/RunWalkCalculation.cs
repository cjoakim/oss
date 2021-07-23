using System;

// Instances of this class represent an Age of an athlete.
// Heart-rate training zones are calculated for the age.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26 {

    public struct RunWalkCalculation {  

        // Input fields:
        public string runHHMMSS;
        public string runPPM;
        public string walkHHMMSS;
        public string walkPPM;
        public double miles;

        // Calculated fields:
        public Speed averageSpeed;
        public string projectedTime;
    } 

}
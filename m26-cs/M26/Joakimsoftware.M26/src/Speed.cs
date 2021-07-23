using System;

// Instances of this class represent the calculated Speed for a given
// Distance and ElapsedTime pair. 
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26 {
    public class Speed {

        public Distance distance { get; }
        public ElapsedTime elapsedTime { get; }

        public Speed(Distance dist, ElapsedTime time) {

            distance = dist;
            elapsedTime = time;
        }

        public double mph() {

            return distance.asMiles() / elapsedTime.hours();
        }

        public double kph() {

            return distance.asKilometers() / elapsedTime.hours();
        }

        public double yph() {

            return distance.asYards() / elapsedTime.hours();
        }

        public double secondsPerMile() {

            return elapsedTime.secs / distance.asMiles();
        }

        public string pacePerMile() {

            double spm = secondsPerMile();
            int mm = (int) Math.Floor(spm / 60.0f);
            double ss = (spm - (mm * 60.0f));
            if (ss > 59.999999) {
                ss = 59.999999;
            }
            string mms = mm.ToString("00");
            string sss = ss.ToString("00.00");
            return $"{mms}:{sss}";
        }

        public Speed ageGraded(Age eventAge, Age gradedAge) {

            double agFactor = eventAge.maxPulse() / gradedAge.maxPulse();
            double gradedSecs = ((double) elapsedTime.secs) * agFactor;
            ElapsedTime gradedEt = new ElapsedTime(gradedSecs);
            return new Speed(distance, gradedEt);
        }

        public ElapsedTime projectedTime(Distance anotherDistance, string formula = Constants.SpeedFormulaSimple) {

            if (Constants.SpeedFormulaRiegel.Equals(formula.Trim().ToLower())) {
                double s1 = elapsedTime.secs;
                double m1 = distance.asMiles();
                double m2 = anotherDistance.asMiles();
                double s2 = s1 * Math.Pow((m2/m1), (double) 1.06);
                return new ElapsedTime(s2);
            }
            else {
                double secs = secondsPerMile() * anotherDistance.asMiles();
                return new ElapsedTime(secs);
            }
        }
    }
}

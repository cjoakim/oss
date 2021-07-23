using System;

// Instances of this class represent an Age of an athlete.
// Heart-rate training zones are calculated for the age.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26 {

    public class Age {
            public double value { get; }

            public Age(double val) {

                value = val;
            }

            public double maxPulse() {

                if (value < 20) {
                    return 200.0;
                }
                else {
                    return 220.0 - value;
                }
            }

            public Age add(Age anotherInstance) {

                return new Age(value + anotherInstance.value);
            }

            public Age subtract(Age anotherInstance) {

                return new Age(value - anotherInstance.value);
            }

            public double[] trainingZones() {

                double[] zone_percentages = { 0.95, 0.90, 0.85, 0.80, 0.75 };
                double[] pulses = new double[zone_percentages.Length];

                for (int i = 0; i < zone_percentages.Length; i++) {
                    pulses[i] = maxPulse() * zone_percentages[i];
                }
                return pulses;
            }
    }
}

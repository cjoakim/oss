using System;

// This class defines constant values used in this library.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26 {
    public class Constants {
        public const string UomMiles      = "m";
        public const string UomKilometers = "k";
        public const string UomYards      = "y";
        public static string[] UnitsOfMeasure() {
            return new string[] {UomMiles, UomKilometers, UomYards};
        }
        public const double KilometersPerMile = 1.609344;
        public const double MilesPerKilometer = 0.621371192237334;
        public const double YardsPerKilometer = 1093.6132983377076;
        public const double FeetPerKilometer = 3280.839895013123;
        public const double FeetPerMeter = 3.280839895013123;
        public const long YardsPerMile = 1760;
        public const long SecondsPerHour = 3600;

        public const long SecondsPerMinute = 60;
        public const string SpeedFormulaSimple = "simple";
        public const string SpeedFormulaRiegel = "riegel";
    }
}

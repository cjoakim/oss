using System;
using Joakimsoftware.M26;

// This program demonstrates the use of the Joakimsoftware.M26 classlib.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26.Example {
    
    class Program {

        static void Main(string[] args) {

            Console.WriteLine("M26 Examples Program");

            // Construct a Distance from a given miles value
            Distance d = new Distance(26.2);

            // Unit-of-measure translations
            double m = d.asMiles();
            double k = d.asKilometers();
            double y = d.asYards();
            Console.WriteLine($"Distance - miles:        {m}");
            Console.WriteLine($"Distance - kilometers:   {k}");
            Console.WriteLine($"Distance - yards:        {y}");

            // Constructors for Kilometers and Yards are supported
            Distance dk = new Distance(10, Constants.UomKilometers);
            Distance dy = new Distance(1760, Constants.UomYards);

            // Construct an ElapsedTime from HH, MM, and SS values
            ElapsedTime et = new ElapsedTime(3, 47, 30);
            double secs = et.secs;
            double hours = et.hours();
            Console.WriteLine($"ElapsedTime - secs:      {secs}");
            Console.WriteLine($"ElapsedTime - hours:     {hours}");
            Console.WriteLine($"ElapsedTime - hhmmss:    {et.asHHMMSS()}");

            // Alternative constructor, equivalent to the above et instance
            ElapsedTime et2 = new ElapsedTime(13650.0);

            // Construct a Speed from a Distance and ElapsedTime
            Speed sp = new Speed(d, et);
            double mph = sp.mph();
            double kph = sp.kph();
            double yph = sp.yph();
            double spm = sp.secondsPerMile();
            string ppm = sp.pacePerMile();
            Console.WriteLine($"Speed - mph:             {mph}");
            Console.WriteLine($"Speed - kph:             {kph}");
            Console.WriteLine($"Speed - yph:             {yph}");
            Console.WriteLine($"Speed - secondsPerMile:  {spm}");
            Console.WriteLine($"Speed - pacePerMile:     {ppm}");

            // Project the Speed to another Distance, simple formula
            ElapsedTime etp1 = sp.projectedTime(new Distance(31.0));
            Console.WriteLine($"Speed projected to 31m:  {etp1.asHHMMSS()}");

            // Project the Speed to another Distance, riegel exponential formula
            ElapsedTime etp2 = sp.projectedTime(new Distance(31.0), Constants.SpeedFormulaRiegel);
            Console.WriteLine($"Speed projected to 31m:  {etp2.asHHMMSS()}");

            Age a1 = new Age(42.4);
            Age a2 = new Age(61.05);

            Speed agsp = sp.ageGraded(a1, a2);
            Console.WriteLine($"age-graded to 61.05:     {agsp.elapsedTime.asHHMMSS()}");

            RunWalkCalculator rwc = new RunWalkCalculator();
            // method signature: calculate(runHHMMSS, runPPM, walkHHMMSS, walkPPM, miles)
            // returns a RunWalkCalculation struct
            RunWalkCalculation calc = rwc.calculate("9:10", "9:09", "00:45", "17:00", 26.2);
            Console.WriteLine($"RunWalkCalc - mph:       {calc.averageSpeed.mph()}");
            Console.WriteLine($"RunWalkCalc - proj time: {calc.projectedTime}");
        }
    }
}

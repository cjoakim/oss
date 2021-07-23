using System;
using Xunit;
using Joakimsoftware.M26;

// Xunit test for class RunWalkCalculator.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26.Tests {

    public class RunWalkCalculatorTest {

        [Theory]
        [InlineData("10:00", "08:00", "10:00", "16:00", 4,   5.000, "00:48:00")]
        [InlineData("09:00", "09:00", "01:00", "18:00", 26.2,  6.060606, "04:19:22")]
        public void TestCalculate(string runHHMMSS, string runPPM, string walkHHMMSS, string walkPPM, double miles, double projectedMph, string projectedTime) {
            
            RunWalkCalculator rwc = new RunWalkCalculator();
            RunWalkCalculation calc = rwc.calculate(runHHMMSS, runPPM, walkHHMMSS, walkPPM, miles);
            double tolerance = 0.000001;
            // Console.WriteLine($"calc: {calc.averageSpeed.mph()} {calc.projectedTime}");

            Assert.Equal(calc.projectedTime, projectedTime);
            Assert.True(calc.averageSpeed.mph() + tolerance > projectedMph);
            Assert.True(calc.averageSpeed.mph() - tolerance < projectedMph);
        }
    }
}

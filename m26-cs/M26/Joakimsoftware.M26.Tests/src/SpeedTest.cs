using System;
using Xunit;
using Joakimsoftware.M26;

// Xunit test for class Speed.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26.Tests {

    public class SpeedTest {

        [Fact]
        public void TestConstructor() {

            double v = 26.2f;
            Distance d = new Distance(v);
            ElapsedTime et = new ElapsedTime("3:47:30");
            Speed sp = new Speed(d, et);

            Assert.True(sp.distance.isMiles());
            Assert.False(sp.distance.isYards());
            Assert.Equal("03:47:30", sp.elapsedTime.asHHMMSS());
        }

        [Theory]
        [InlineData(6.000000, "1:00:00", 6.000000, 9.656064, 10560.000)] 
        [InlineData(2.000000, "30:00", 4.000000, 6.437376, 7040.000000)] 
        [InlineData(26.2, "3:47:30", 6.909890, 11.120390, 12161.406593)] 
        public void TestXphMethods(double miles, string time, double mph, double kph, double yph) {

            double tolerance = 0.000001;
            Distance d = new Distance(miles);
            ElapsedTime et = new ElapsedTime(time);
            Speed sp = new Speed(d, et);
            //Console.WriteLine($"{miles} {time} -> {sp.mph()} {sp.kph()} {sp.yph()}");

            Assert.True(sp.mph() + tolerance > mph);
            Assert.True(sp.mph() - tolerance < mph);

            Assert.True(sp.kph() + tolerance > kph);
            Assert.True(sp.kph() - tolerance < kph);

            Assert.True(sp.yph() + tolerance > yph);
            Assert.True(sp.yph() - tolerance < yph);
        }

        [Theory]
        [InlineData(6.000000, "1:00:00", 600.0, "10:00.00")] 
        [InlineData(2.000000, "30:00", 900.0, "15:00.00")] 
        [InlineData(26.2, "3:47:30", 520.992366, "08:40.99")] 
        public void TestPerMileMethods(double miles, string time, double spm, string ppm) {

            double tolerance = 0.000001;
            Distance d = new Distance(miles);
            ElapsedTime et = new ElapsedTime(time);
            Speed sp = new Speed(d, et);
            //Console.WriteLine($"{miles} {time} -> {sp.secondsPerMile()} {sp.pacePerMile()}");
            Assert.True(sp.secondsPerMile() + tolerance > spm);
            Assert.True(sp.secondsPerMile() - tolerance < spm);
            Assert.Equal(sp.pacePerMile(), ppm);
        }

        [Fact]
        public void TestAgeGraded() {

            double v = 26.2f;
            Distance d = new Distance(v);
            ElapsedTime et = new ElapsedTime("3:47:30");
            Speed s1 = new Speed(d, et);
            Age a1 = new Age(42.5);
            Age a2 = new Age(43.5);
            Age a3 = new Age(57.1);
            Speed s2 = s1.ageGraded(a1, a2);
            Speed s3 = s1.ageGraded(a1, a3);
            double tolerance = 0.000001;
            // Console.WriteLine($"{s1.mph()}  {s2.mph()}  {s3.mph()}");

            Assert.True(s1.mph() + tolerance > 6.9098903);
            Assert.True(s1.mph() - tolerance < 6.9098903);
 
            Assert.True(s2.mph() + tolerance > 6.871130);
            Assert.True(s2.mph() - tolerance < 6.871130);

            Assert.True(s3.mph() + tolerance > 6.341693);
            Assert.True(s3.mph() - tolerance < 6.341693);
        }

        [Theory]
        [InlineData(10.0, "1:30:00", "simple", 20.0, "03:00:00")] 
        [InlineData(10.0, "1:30:00", "riegel", 20.0, "03:07:38")] 
        public void TestProjectedTime(double miles1, string time1, string formula, double miles2, string time2) {

            Distance d1 = new Distance(miles1);
            Distance d2 = new Distance(miles2);
            ElapsedTime et1 = new ElapsedTime(time1);
            Speed sp = new Speed(d1, et1);
            ElapsedTime et2 = sp.projectedTime(d2, formula);
            string projHhmmss = et2.asHHMMSS();
            // Console.WriteLine($"{miles1} {miles2} {formula} -> {projHhmmss}");
            Assert.Equal(projHhmmss, time2);
        }
    }
}

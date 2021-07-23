using System;
using Xunit;
using Joakimsoftware.M26;

// Xunit test for class Distance.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26.Tests {

    public class DistanceTest {

        [Fact]
        public void TestConstructor() {

            double tolerance = 0.000001;
            double v = 26.2f;

            Distance d = new Distance(v);  // default to miles
            Assert.Equal(d.uom, Constants.UomMiles);
            Assert.True(d.isMiles());
            Assert.False(d.isKilometers());
            Assert.False(d.isYards());
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, null);
            Assert.Equal(d.uom, Constants.UomMiles);
            Assert.True(d.isMiles());
            Assert.False(d.isKilometers());
            Assert.False(d.isYards());
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, "");
            Assert.Equal(d.uom, Constants.UomMiles);
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, "   ");
            Assert.Equal(d.uom, Constants.UomMiles);
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, " M ");
            Assert.Equal(d.uom, Constants.UomMiles);
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, "m");
            Assert.Equal(d.uom, Constants.UomMiles);
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, " K ");
            Assert.Equal(d.uom, Constants.UomKilometers);
            Assert.False(d.isMiles());
            Assert.True(d.isKilometers());
            Assert.False(d.isYards());
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, "k");
            Assert.Equal(d.uom, Constants.UomKilometers);
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, " Y ");
            Assert.Equal(d.uom, Constants.UomYards);
            Assert.False(d.isMiles());
            Assert.False(d.isKilometers());
            Assert.True(d.isYards());
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);

            d = new Distance(v, "y");
            Assert.Equal(d.uom, Constants.UomYards);
            Assert.True(d.value + tolerance > v);
            Assert.True(d.value - tolerance < v);
        }

        [Theory]
        [InlineData(26.2, "m", 26.2, 42.1648128, 46112.0)]
        [InlineData(10.0, "k", 6.2137119, 10.000, 10936.1329833)]
        [InlineData(1800.0, "y", 1.022727, 1.64592, 1800.000000)]
        public void TestTranslations(double v, string u, double xm, double xk, double xy) {

            double tolerance = 0.000001;
            Distance d = new Distance(v, u);
            double m = d.asMiles();
            double k = d.asKilometers();
            double y = d.asYards();
            Assert.True(m + tolerance > xm);
            Assert.True(m - tolerance < xm);
            Assert.True(k + tolerance > xk);
            Assert.True(k - tolerance < xk);
            Assert.True(y + tolerance > xy);
            Assert.True(y - tolerance < xy);
        }

        [Theory]
        [InlineData(26.2, "m", 26.2, "m", 52.4)]
        [InlineData(26.2, "m", 4.8, "m", 31.0)]
        [InlineData(26.2, "m", 5.0, "k", 29.3068559)]
        [InlineData(26.2, "m", 1800.0, "y", 27.222727)]
        [InlineData(10.0, "k", 5.0, "k", 15.000000)]
        [InlineData(10.0, "k", 3.1, "m", 14.988966)]
        [InlineData(10.0, "k", 1800.0, "y", 11.64592)]
        [InlineData(1800.0, "y", 3600.0, "y", 5400.0)]
        [InlineData(1800.0, "y", 1.0, "m", 3560.0)]
        [InlineData(1800.0, "y", 1.0, "k", 2893.61329833)]
        public void TestAdd(double v1, string u1, double v2, string u2, double xv) {

            double tolerance = 0.000001;
            Distance d1 = new Distance(v1, u1);
            Distance d2 = new Distance(v2, u2);
            Distance d3 = d1.add(d2);

            Assert.Equal(d1.uom, u1);
            Assert.Equal(d2.uom, u2);
            Assert.Equal(d1.uom, d3.uom);
            double v = d3.value;
            //Console.WriteLine("add d3.value: " + d3.value);
            Assert.True(v + tolerance > xv);
            Assert.True(v - tolerance < xv);
        }

        [Theory]
        [InlineData(26.2, "m", 16.2, "m", 10.0)]
        [InlineData(26.2, "m", 5.0, "k", 23.0931440)]
        [InlineData(26.2, "m", 1800.0, "y", 25.177273)]
        [InlineData(50.0, "k", 5.0, "k", 45.000000)]
        [InlineData(10.0, "k", 3.1, "m", 5.0110336)]
        [InlineData(10.0, "k", 1800.0, "y", 8.35408)]
        [InlineData(3600.0, "y", 3000.0, "y", 600.0)]
        [InlineData(1800.0, "y", 0.5, "m", 920.0)]
        [InlineData(1800.0, "y", 0.5, "k", 1253.1933508)]
        public void TestSubtract(double v1, string u1, double v2, string u2, double xv) {
            
            double tolerance = 0.000001;
            Distance d1 = new Distance(v1, u1);
            Distance d2 = new Distance(v2, u2);
            Distance d3 = d1.subtract(d2);

            Assert.Equal(d1.uom, u1);
            Assert.Equal(d2.uom, u2);
            Assert.Equal(d1.uom, d3.uom);
            double v = d3.value;
            //Console.WriteLine("subtract d3.value: " + d3.value);
            Assert.True(v + tolerance > xv);
            Assert.True(v - tolerance < xv);
        }
    }
}

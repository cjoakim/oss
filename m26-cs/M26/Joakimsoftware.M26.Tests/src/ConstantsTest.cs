using System;
using Xunit;
using Joakimsoftware.M26;

// Xunit test for class Constants.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26.Tests {
    public class ConstantsTest {
        [Fact]
        public void TestUnitsOfMeasureConstants() {

            Assert.Equal("m", Constants.UomMiles);
            Assert.Equal("k", Constants.UomKilometers);
            Assert.Equal("y", Constants.UomYards);
        }

        [Fact]
        public void TestUnitsOfMeasureArray() {

            string[] constants = Constants.UnitsOfMeasure();
            Assert.Equal(3, constants.Length);
            Assert.Equal(constants[0], Constants.UomMiles);
            Assert.Equal(constants[1], Constants.UomKilometers);
            Assert.Equal(constants[2], Constants.UomYards);
        }

        [Fact]
        public void TestKilometersPerMile() {

            double expected  = 1.609344;
            double tolerance = 0.000001;
            Assert.True(expected + tolerance > Constants.KilometersPerMile);
            Assert.True(expected - tolerance < Constants.KilometersPerMile);
        }

        [Fact]
        public void TestMilesPerKilometer() {

            double expected  = 0.621371192237334;
            double tolerance = 0.000000000000001;
            Assert.True(expected + tolerance > Constants.MilesPerKilometer);
            Assert.True(expected - tolerance < Constants.MilesPerKilometer);
        } 

        [Fact]
        public void TestYardsPerKilometer() {

            double expected  = 1093.6132983377076;
            double tolerance =    0.000000000001;
            Assert.True(expected + tolerance > Constants.YardsPerKilometer);
            Assert.True(expected - tolerance < Constants.YardsPerKilometer);
        } 

        [Fact]
        public void TestFeetPerKilometer() {

            double expected  = 3280.839895013123;
            double tolerance =    0.000000000001;
            Assert.True(expected + tolerance > Constants.FeetPerKilometer);
            Assert.True(expected - tolerance < Constants.FeetPerKilometer);
        }

        [Fact]
        public void TestFeetPerMeter() {

            double expected  = 3.280839895013123;
            double tolerance = 0.000000000000001;
            Assert.True(expected + tolerance > Constants.FeetPerMeter);
            Assert.True(expected - tolerance < Constants.FeetPerMeter);
        }

        [Fact]
        public void TestYardsPerMile() {

            long expected  = 1760;
            Assert.True(expected == Constants.YardsPerMile);
        }

        [Fact]
        public void TestSecondsPerHour() {

            long expected  = 3600;
            Assert.True(expected == Constants.SecondsPerHour);
        }

        [Fact]
        public void TestSecondsPerMinute() {

            long expected  = 60;
            Assert.True(expected == Constants.SecondsPerMinute);
        }

        [Fact]
        public void TestSpeedFormulas() {
            
            Assert.Equal("simple", Constants.SpeedFormulaSimple);
            Assert.Equal("riegel", Constants.SpeedFormulaRiegel);
        }
    }
}

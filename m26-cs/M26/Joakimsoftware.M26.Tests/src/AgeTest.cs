using System;
using Xunit;
using Joakimsoftware.M26;

// Xunit test for class Age.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26.Tests {
    public class AgeTest {
        [Fact]
        public void TestConstructor()
        {
            double expected  = 34.56;
            double tolerance = 0.000001;
            Age a = new Age(expected);
            Assert.True(expected + tolerance > a.value);
            Assert.True(expected - tolerance < a.value);
        }

        [Theory]
        [InlineData(16.0, 200.0)]
        [InlineData(20.0, 200.0)]
        [InlineData(21.0, 199.0)]
        [InlineData(58.1, 161.9)]
        public void TestMaxPulse(double ageYears, double expectedMax) {
            double tolerance = 0.000001;
            double actualMax = new Age(ageYears).maxPulse();
            Assert.True(actualMax + tolerance > expectedMax);
            Assert.True(actualMax - tolerance < expectedMax);
        }

        [Theory]
        [InlineData(16.0, 58.0, 74.0)]
        [InlineData(42.5,  2.6, 45.1)]
        public void TestAdd(double ageYears1, double ageYears2, double expected) {
            double tolerance = 0.000001;
            Age a1 = new Age(ageYears1);
            Age a2 = new Age(ageYears2);
            Age a3 = a1.add(a2);
            Assert.True(a3.value + tolerance > expected);
            Assert.True(a3.value - tolerance < expected);
        }

        [Theory]
        [InlineData(58.0, 16.0, 42.0)]
        [InlineData(42.5,  2.6, 39.9)]
        public void TestSubtract(double ageYears1, double ageYears2, double expected) {
            double tolerance = 0.000001;
            Age a1 = new Age(ageYears1);
            Age a2 = new Age(ageYears2);
            Age a3 = a1.subtract(a2);
            Assert.True(a3.value + tolerance > expected);
            Assert.True(a3.value - tolerance < expected);
        }

        [Fact]
        public void TestTrainingZones() {
            Age a1 = new Age(58.0);
            double tolerance = 0.000001;
            double[] zonePulses = a1.trainingZones();

            Assert.True(5 == zonePulses.Length);

            double expected = 153.9;
            Assert.True(expected + tolerance > zonePulses[0]);
            Assert.True(expected - tolerance < zonePulses[0]);

            expected = 121.5;
            Assert.True(expected + tolerance > zonePulses[4]);
            Assert.True(expected - tolerance < zonePulses[4]);
        }
    }
}

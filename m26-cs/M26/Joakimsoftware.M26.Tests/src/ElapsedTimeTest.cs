using System;
using Xunit;
using Joakimsoftware.M26;

// Xunit test for class ElapsedTime.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26.Tests {

    public class ElapsedTimeTest {

        [Fact]
        public void TestThreeNumericConstructor() {

            ElapsedTime et = new ElapsedTime(1, 2, 3);
            Assert.Equal(1, et.hh);
            Assert.Equal(2, et.mm);
            Assert.Equal(3, et.ss);
            Assert.Equal(3723, et.secs);
        }

        [Theory]
        [InlineData(3723.0, 1, 2, 3, 3723)]
        [InlineData(11, 0, 0, 11, 11)]
        [InlineData(61, 0, 1, 1, 61)]
        [InlineData(60, 0, 1, 0, 60)]
        [InlineData(3600.1, 1, 0, 0, 3600)]
        [InlineData(3600.9, 1, 0, 0, 3600)]
        public void TestOneNumericConstructor(double arg, long h, long m, long s, long secs) {

            ElapsedTime et = new ElapsedTime(arg);
            Assert.Equal(h, et.hh);
            Assert.Equal(m, et.mm);
            Assert.Equal(s, et.ss);
            Assert.Equal(secs, et.secs);
        }

        [Theory]
        [InlineData("1", 0, 0, 1, 1)]
        [InlineData(" 1 ", 0, 0, 1, 1)]
        [InlineData("01:12", 0, 1, 12, 72)]
        [InlineData(" 1 : 12 ", 0, 1, 12, 72)]
        [InlineData("01:02:03", 1, 2, 3, 3723)]
        [InlineData("03:47:30", 3, 47, 30, 13650)]
        public void TestStringConstructor(string s, long hh, long mm, long ss, long secs) {

            ElapsedTime et = new ElapsedTime(s);
            Assert.Equal(hh, et.hh);
            Assert.Equal(mm, et.mm);
            Assert.Equal(ss, et.ss);
            Assert.Equal(secs, et.secs);
        }

        [Theory]
        [InlineData("1:00:00", 1.000000)]
        [InlineData("0:00:10", 0.002777)]
        [InlineData("4:20:00", 4.333333)]
        public void TestHours(string s, double hours) {

            double tolerance = 0.000001;
            ElapsedTime et = new ElapsedTime(s);
            Assert.True(et.hours() + tolerance > hours);
            Assert.True(et.hours() - tolerance < hours);
        }

        [Theory]
        [InlineData("1", "00:00:01")]
        [InlineData("1:2", "00:01:02")]
        [InlineData("1:6:12", "01:06:12")]
        public void TestAsHHMMSS(string s, string expected) {
            
            ElapsedTime et = new ElapsedTime(s);
            Assert.Equal(expected, et.asHHMMSS());
        }
    }
}

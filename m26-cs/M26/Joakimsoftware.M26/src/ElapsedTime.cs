using System;

// Instances of this class represent the elapsed time of an event - such as
// a run or swim.  Two constructors are provided which receive the hours,
// minutes, and seconds of time.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26 {
    public class ElapsedTime {
        public long hh { get; }
        public long mm { get; }
        public long ss { get; }
        public long secs { get; }

        public ElapsedTime(int h, int m, int s) {
            hh = Math.Abs(h);
            mm = Math.Abs(m);
            ss = Math.Abs(s);
            secs = (hh * Constants.SecondsPerHour) + (mm * Constants.SecondsPerMinute) + ss;
        }

        public ElapsedTime(double totalSeconds) {
            hh = (long) Math.Floor(totalSeconds / (double) Constants.SecondsPerHour);
            double remainder = totalSeconds - (hh * (double) Constants.SecondsPerHour);
            mm = (long) Math.Floor(remainder / (double) 60.0);
            ss = (long) remainder - (mm * 60);
            secs = (hh * Constants.SecondsPerHour) + (mm * Constants.SecondsPerMinute) + ss;
            if (secs < 1) {
                throw new Exception("Invalid zero seconds value; " + secs);
            }
        }

        public ElapsedTime(string hhmmss) {

            hh = 0;
            mm = 0; 
            ss = 0;
            secs = 0;

            try {            
                string[] tokens = hhmmss.Split(':');
                if (tokens.Length == 1) {
                    ss = toLong(tokens[0]);
                }
                else if (tokens.Length == 2) {
                    mm = toLong(tokens[0]);
                    ss = toLong(tokens[1]);
                }
                else {
                    hh = toLong(tokens[0]);
                    mm = toLong(tokens[1]);
                    ss = toLong(tokens[2]);
                }
            }
            catch (Exception e) {
                throw e;
            }
            if (mm > 59) {
                throw new Exception("Invalid mm value; " + mm);
            }
            if (ss > 59) {
                throw new Exception("Invalid ss value; " + ss);
            }
            secs = Math.Abs((hh * Constants.SecondsPerHour) + (mm * Constants.SecondsPerMinute) + ss);
            if (secs < 1) {
                throw new Exception("Invalid zero seconds value; " + secs);
            }
        }

        public double hours() {
            
            return (double) secs / (double) Constants.SecondsPerHour;
        }

        public string asHHMMSS() {
            string h = hh.ToString("00");
            string m = mm.ToString("00");
            string s = ss.ToString("00");
            return $"{h}:{m}:{s}";
        }

        private long toLong(string s) {

            return Math.Abs(Convert.ToInt64(s));
        }
    }
}

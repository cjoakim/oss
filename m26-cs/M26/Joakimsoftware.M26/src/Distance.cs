using System;

// Instances of this class represent a Distance of an event, such as a run or swim or cycling.
// The distance can be expressed in miles, kilometers, or yards.
// Chris Joakim, 2021/07/19

namespace Joakimsoftware.M26 {
    public class Distance {
        public double value { get; }
        public string uom { get; }

        public Distance(double val, string unitOfMeasure=Constants.UomMiles) {

            value = val;

            if (string.IsNullOrEmpty(unitOfMeasure)) {
                uom = Constants.UomMiles;  // default to miles
            }
            else {
                if (string.Equals(unitOfMeasure.Trim(), Constants.UomKilometers, StringComparison.OrdinalIgnoreCase)) {
                    uom = Constants.UomKilometers;
                }
                else if (string.Equals(unitOfMeasure.Trim(), Constants.UomYards, StringComparison.OrdinalIgnoreCase)) {
                    uom = Constants.UomYards;
                }
                else {
                    uom = Constants.UomMiles;
                }
            }
        }

        public Boolean isMiles() {

            return uom.Equals(Constants.UomMiles);
        }

        public Boolean isKilometers() {

            return uom.Equals(Constants.UomKilometers);
        }

        public Boolean isYards() {

            return uom.Equals(Constants.UomYards);
        }

        public double asMiles() {

            if (isKilometers()) {
                return value / Constants.KilometersPerMile;
            }
            else if (isYards()) {
                return value / Constants.YardsPerMile;
            }
            else {
                return value;
            }
        }

        public double asKilometers() {

            if (isKilometers()) {
                return value;
            }
            else if (isYards()) {
                return value / Constants.YardsPerKilometer;
            }
            else {
                return value * Constants.KilometersPerMile;
            }
        }

        public double asYards() {

            if (isKilometers()) {
                return value * Constants.YardsPerKilometer;
            }
            else if (isYards()) {
                return value;
            }
            else {
                return value * Constants.YardsPerMile;
            }
        }

        public Distance add(Distance d2) {

            if (d2 == null) {
                return new Distance(value, uom);
            }

            if (isKilometers()) {
                double v = value + d2.asKilometers();
                return new Distance(v, uom);
            }
            else if (isYards()) {
                double v = value + d2.asYards();
                return new Distance(v, uom);
            }
            else {
                double v = value + d2.asMiles();
                return new Distance(v, uom);
            }
        }

        public Distance subtract(Distance d2) {

            if (d2 == null) {
                return new Distance(value, uom);
            }

            if (isKilometers()) {
                double v = value - d2.asKilometers();
                return new Distance(v, uom);
            }
            else if (isYards()) {
                double v = value - d2.asYards();
                return new Distance(v, uom);
            }
            else {
                double v = value - d2.asMiles();
                return new Distance(v, uom);
            }
        }
    }
}

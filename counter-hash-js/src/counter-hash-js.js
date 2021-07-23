// Copyright 2015, Christopher Joakim <christopher.joakim@gmail.com>
var CounterHash = (function () {
    function CounterHash() {
        this.values = {};
    }
    CounterHash.prototype.value = function (key) {
        var n = this.values[key];
        if (this.populated(n)) {
            return n;
        }
        else {
            return 0;
        }
    };
    CounterHash.prototype.sum = function () {
        var sum = 0;
        var keys = Object.getOwnPropertyNames(this.values);
        for (var i = 0; i < keys.length; i++) {
            var key = keys[i];
            var val = this.value(key);
            sum = sum + val;
        }
        return sum;
    };
    CounterHash.prototype.increment = function (key) {
        if (this.populated(key)) {
            var val = this.value(key);
            this.values[key] = val + 1;
        }
    };
    CounterHash.prototype.decrement = function (key) {
        if (this.populated(key)) {
            var val = this.value(key);
            this.values[key] = val - 1;
        }
    };
    CounterHash.prototype.add = function (key, n) {
        if (this.populated(key)) {
            if (this.populated(n)) {
                var val = this.value(key);
                this.values[key] = val + n;
            }
        }
    };
    CounterHash.prototype.subtract = function (key, n) {
        if (this.populated(key)) {
            if (this.populated(n)) {
                var val = this.value(key);
                this.values[key] = val - n;
            }
        }
    };
    CounterHash.prototype.sorted_keys = function () {
        var keys = Object.getOwnPropertyNames(this.values);
        return keys.sort();
    };
    CounterHash.prototype.sorted_tuples = function () {
        var array = [];
        var keys = Object.getOwnPropertyNames(this.values);
        for (var i = 0; i < keys.length; i++) {
            var key = keys[i];
            var val = this.value(key);
            array.push([key, val]);
        }
        return array.sort();
    };
    CounterHash.prototype.populated = function (s) {
        if (s === undefined) {
            return false;
        }
        if (s === null) {
            return false;
        }
        return true;
    };
    CounterHash.VERSION = '0.2.0';
    return CounterHash;
})();
exports.CounterHash = CounterHash;

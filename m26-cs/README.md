# m26-cs

The **m26** library for running, cycling, and swimming calculations; implemented in C# and DotNet Core.

The current version, 2.0.0, targets the **net5.0** framework.

## Links
- M26 at NuGet: https://www.nuget.org/packages/Joakimsoftware.M26/
- This repository: https://github.com/cjoakim/m26-cs

## Usage

See the xunit test app **Joakimsoftware.M26.Tests**, and console app **Joakimsoftware.M26.Example**
in this repo.

Sample code, see Program.cs:

```
using System;
using Joakimsoftware.M26;

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
```

The above code produces the following output:

```
$ dotnet run
M26 Examples Program
Distance - miles:        26.2
Distance - kilometers:   42.1648128
Distance - yards:        46112
ElapsedTime - secs:      13650
ElapsedTime - hours:     3.7916666666666665
ElapsedTime - hhmmss:    03:47:30
Speed - mph:             6.90989010989011
Speed - kph:             11.120390189010989
Speed - yph:             12161.406593406595
Speed - secondsPerMile:  520.9923664122138
Speed - pacePerMile:     08:40.99
Speed projected to 31m:  04:29:10
Speed projected to 31m:  04:31:54
age-graded to 61.05:     04:14:11
RunWalkCalc - mph:       6.164383561643836
RunWalkCalc - proj time: 04:15:00
```

## Version History

| Version  |    Date    | Target Framework |
| -------- | ---------- | ---------------- |
|  2.0.0   | 2021/07/19 |      net5.0      |
|  1.0.0   | 2018/10/13 |  netstandard2.0  |


## Project Creation

See **project_creation.sh** in the root of this repository which used the
dotnet CLI to create the solution with three subprojects.

## Publishing to NuGet

```
$ dotnet build

$ ./test.sh
...
Passed!  - Failed:     0, Passed:    75, Skipped:     0, Total:    75, Duration: 31 ms

$ dotnet pack
...
  Successfully created package '.../m26-cs/M26/Joakimsoftware.M26/bin/Debug/Joakimsoftware.M26.2.0.0.nupkg'.
...


$ dotnet nuget push bin/Debug/Joakimsoftware.M26.2.0.0.nupkg -k $NUGET_M26_KEY -s https://api.nuget.org/v3/index.json

Pushing Joakimsoftware.M26.2.0.0.nupkg to 'https://www.nuget.org/api/v2/package'...
  PUT https://www.nuget.org/api/v2/package/

warn : All published packages should have license information specified. Learn more: https://aka.ms/deprecateLicenseUrl.
  Created https://www.nuget.org/api/v2/package/ 705ms

Your package was pushed.
```

## Package Description

```
<package xmlns="http://schemas.microsoft.com/packaging/2012/06/nuspec.xsd">
  <metadata>
    <id>Joakimsoftware.M26</id>
    <version>2.0.0</version>
    <authors>Chris Joakim</authors>
    <requireLicenseAcceptance>false</requireLicenseAcceptance>
    <description>Package Description</description>
    <dependencies>
      <group targetFramework="net5.0" />
    </dependencies>
  </metadata>
</package>
```

---

## M26 Implementations in other programming languages

### Python

- https://pypi.org/project/m26/
- https://github.com/cjoakim/m26-py

### Node.js

- https://www.npmjs.com/package/m26-js
- https://github.com/cjoakim/m26-js

### Ruby

- https://rubygems.org/gems/m26/versions/1.0.1
- https://github.com/cjoakim/m26

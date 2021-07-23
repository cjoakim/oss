#!/bin/bash

echo '========== Building Project ...'
dotnet build

cd ../Joakimsoftware.M26.Tests/

echo '========== Building Tests ...'
dotnet build

echo '========== Executing Tests ...'
dotnet test

cd ../Joakimsoftware.M26/


# Results 10/13
# Total tests: 75. Passed: 75. Failed: 0. Skipped: 0.
# Test Run Successful.
# Test execution time: 1.4133 Seconds
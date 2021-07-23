#!/bin/bash

# Recreate the project structure for net5.0 version 2 of this library.
# Chris Joakim, 2021/07/19 

# V1 README docs:
# [~/github/m26-cs/M26/Joakimsoftware.M26]$ dotnet new classlib
# [~/github/m26-cs/M26/Joakimsoftware.M26]$ dotnet new xunit
# [~/github/m26-cs/M26/Joakimsoftware.M26.Example]$ dotnet new console

# ./M26/Joakimsoftware.M26.Tests/Joakimsoftware.M26.Tests.csproj
# ./M26/Joakimsoftware.M26.Example/Joakimsoftware.M26.Example.csproj
# ./M26/Joakimsoftware.M26/Joakimsoftware.M26.csproj

rm -rf  M26/

mkdir -p M26/Joakimsoftware.M26
mkdir -p M26/Joakimsoftware.M26.Tests
mkdir -p M26/Joakimsoftware.M26.Example

cd M26/Joakimsoftware.M26
dotnet new classlib
dotnet build
cd ../..

cd M26/Joakimsoftware.M26.Tests
dotnet new xunit
dotnet add reference ../Joakimsoftware.M26/Joakimsoftware.M26.csproj
dotnet build
cd ../..

cd M26/Joakimsoftware.M26.Example
dotnet new console
dotnet add reference ../Joakimsoftware.M26/Joakimsoftware.M26.csproj
dotnet build
cd ../..

dotnet new sln -o M26
cd M26 

dotnet sln M26.sln add Joakimsoftware.M26/Joakimsoftware.M26.csproj
dotnet sln M26.sln add Joakimsoftware.M26.Tests/Joakimsoftware.M26.Tests.csproj
dotnet sln M26.sln add Joakimsoftware.M26.Example/Joakimsoftware.M26.Example.csproj

dotnet build

cd ..

echo ''
echo 'pwd is:'
pwd 

echo ''
echo 'done'

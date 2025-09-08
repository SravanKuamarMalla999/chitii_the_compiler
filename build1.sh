#!/bin/bash

set -e  # Exit on error

echo "Cleaning previous build artifacts..."
rm -f program.ll program.exe

echo "Generating LLVM IR with Python compiler..."
/mingw64/bin/python -m build.main

echo "Compiling LLVM IR to native executable with clang..."
clang program.ll -o program.exe

echo "Build succeeded!"

read -p "Run program now? (y/n) " runprog
if [[ "$runprog" =~ ^[Yy]$ ]]; then
  echo "Running program.exe..."
  ./program.exe
else
  echo "You can run the program later with ./program.exe"
fi

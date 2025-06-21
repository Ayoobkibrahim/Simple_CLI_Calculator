#!/bin/bash

echo "Simple CLI Calculator"
read -p "Enter first number " num1
read -p "Enter operatot(+,-,*,/) : " operator
read -p "Enter second number " num2

python3 calculator.py "$num1" "$operator" "$num2"
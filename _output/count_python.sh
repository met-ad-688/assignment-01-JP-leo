#!/bin/bash
count=$(grep -i "python" ../stackoverflow/*.csv | wc -l)
echo "Number of lines containing 'python' in CSV files: $count"

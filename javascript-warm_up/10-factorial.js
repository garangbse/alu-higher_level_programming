#!/usr/bin/node
// Script that computes and prints a factorial

function factorial(n) {
    // Convert argument to integer
    n = parseInt(n);
    
    // If n is NaN or less than or equal to 1, return 1
    if (isNaN(n) || n <= 1) {
        return 1;
    } else {
        // Compute factorial recursively
        return n * factorial(n - 1);
    }
}

// Get command line argument
const num = process.argv[2];

// Calculate and print the factorial
console.log(factorial(num));

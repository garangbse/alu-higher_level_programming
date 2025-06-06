#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments

// Get arguments excluding the first two elements (node and script name)
const args = process.argv.slice(2);

// Convert all arguments to integers
const numbers = args.map(arg => parseInt(arg));

// If no argument or only one, print 0
if (args.length <= 1) {
    console.log(0);
} else {
    // Sort numbers in descending order
    numbers.sort((a, b) => b - a);
    
    // Print the second biggest integer
    console.log(numbers[1]);
}

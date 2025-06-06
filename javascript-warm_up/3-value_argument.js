#!/usr/bin/node
// Script that prints the first argument passed to it

// process.argv contains command line arguments
// process.argv[0] is 'node'
// process.argv[1] is the script path
// process.argv[2] is the first actual argument

if (process.argv[2] === undefined) {
    console.log("No argument");
} else {
    console.log(process.argv[2]);
}

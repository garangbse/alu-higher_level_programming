#!/usr/bin/node
// Script that prints the addition of 2 integers

function add(a, b) {
    return parseInt(a) + parseInt(b);
}

const args = process.argv.slice(2);
const firstInt = args[0];
const secondInt = args[1];

console.log(add(firstInt, secondInt));

#!/usr/bin/node
const firstArg = process.argv[2];
const parsedInt = parseInt(firstArg);

if (!isNaN(parsedInt)) {
    console.log(`My number: ${parsedInt}`);
} else {
    console.log("Not a number");
}

#!/usr/bin/node
// Function that prints number of arguments already printed and new argument value

// Counter variable to track number of arguments printed
let counter = 0;

// The logMe function as specified in the prototype
exports.logMe = function (item) {
    console.log(`${counter}: ${item}`);
    counter++; // Increment counter after logging
};

#!/usr/bin/node
// Script to replace the value 12 with 89 in an object

const myObject = {
    type: 'object',
    value: 12
};

console.log(myObject);

// Replace value 12 with 89
myObject.value = 89;

console.log(myObject);

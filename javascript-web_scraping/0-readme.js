#!/usr/bin/node
const fs = require('fs');

// Check if file path is provided
const filePath = process.argv[2];

// Read file
fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});

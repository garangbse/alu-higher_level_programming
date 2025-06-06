#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
    console.error('Usage: node 5-request_store.js <URL> <file path>');
    process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the URL
request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        process.exit(1);
    }

    // Write the response body to the file (UTF-8 encoded by default)
    fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            process.exit(1);
        }
    });
});

#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error(`Error: Status code ${response.statusCode}`);
        return;
    }

    try {
        const todos = JSON.parse(body);
        const completedTasksByUser = {};

        // Count completed tasks for each user
        todos.forEach(todo => {
            if (todo.completed) {
                if (completedTasksByUser[todo.userId]) {
                    completedTasksByUser[todo.userId]++;
                } else {
                    completedTasksByUser[todo.userId] = 1;
                }
            }
        });

        // Only print users with completed tasks
        console.log(completedTasksByUser);
    } catch (parseError) {
        console.error('Error parsing JSON response:', parseError);
    }
});

#!/usr/bin/node
// 7-occurrences.js
// Returns the number of occurrences of searchElement in a list

exports.nbOccurences = function (list, searchElement) {
  // Initialize counter for occurrences
  let count = 0;

  // Iterate through each element in the list
  for (let i = 0; i < list.length; i++) {
    // If the current element matches the search element, increment counter
    if (list[i] === searchElement) {
      count++;
    }
  }

  // Return the total count of occurrences
  return count;
};

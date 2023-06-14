#!/usr/bin/node
const numOfTime = process.argv[2];
const numOfOccurence = parseInt(numOfTime);

if (!isNaN(numOfOccurence)) {
	for (let i = 0; i < numOfOccurence; i++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurences');
}

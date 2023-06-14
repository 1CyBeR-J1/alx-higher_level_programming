#!/usr/bin/node
const firstArg = process.argv[2]
const changedToInt = parseInt(firstArg)
if (!isNaN(changedToInt)) {
  console.log('My number: ' + changedToInt)
} else {
  console.log('Not a number')
}

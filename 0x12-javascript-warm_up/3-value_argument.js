#!/usr/bin/node
const argName = process.argv[2]
if (argName === undefined) {
  console.log('No argument')
} else {
  console.log(argName)
}

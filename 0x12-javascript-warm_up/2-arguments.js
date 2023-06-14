#!/usr/bin/node

const numArgv = process.argv.length - 2
if (numArgv === 0) {
  console.log('No argument')
} else if (numArgv === 1) {
  console.log('Argument found')
} else {
  console.log('Arguments found')
}

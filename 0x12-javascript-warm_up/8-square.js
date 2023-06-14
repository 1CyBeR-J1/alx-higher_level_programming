#!/usr/bin/node
const firstArgv = process.argv[2];
const sizOfSquare = parseInt(firstArgv);
if (!isNaN(sizOfSquare)) {
  if (sizOfSquare > 0) {
    for (let i = 0; i < sizOfSquare; i++) {
      let row = '';
      for (let j = 0; j < sizOfSquare; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}

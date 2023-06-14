#!/usr/bin/node
const orgList = process.argv.slice(2);
const changeToInt = orgList.map(arg => parseInt(arg));

if (changeToInt.length < 2) {
  console.log(0);
} else {
  const sortedInt = changeToInt.sort((a, b) => b - a);
  const secBig = sortedInt[1];
  console.log(secBig);
}

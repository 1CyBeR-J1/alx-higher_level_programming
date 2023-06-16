#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((number, index) => number * index);

console.log(list);
console.log(newList);

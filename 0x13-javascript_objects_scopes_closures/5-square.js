#!/usr/bin/node
const Square = require('./4-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

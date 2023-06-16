#!/usr/bin/node
exports.converter = function (base) {
  return numConv => numConv.toString(base);
};

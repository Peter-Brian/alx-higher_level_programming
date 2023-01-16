#!/usr/bin/node

nbArgs = 0;
exports.logMe = function (item) {
  console.log(nbArgs + ': ' + item);
  nbArgs++;
};

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let new_arr = [];
    for (const [i, num] of arr.entries()) {
        const curr = fn(num, i);
        new_arr.push(curr);
    }

    return new_arr;
};
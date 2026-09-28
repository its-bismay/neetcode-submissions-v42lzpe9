/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const my_obj = {
        val1: val,

        toBe: function (val2) {
            if (this.val1 === val2){
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },

        notToBe: function (val3){
            if (this.val1 !== val3){
                return true
            }else {
                throw new Error("Equal");
            }
        }
    }

    return my_obj
}; 

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
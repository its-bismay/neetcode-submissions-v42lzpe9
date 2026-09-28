/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  const my_obj = {
    int_val: init,
    curr_val: init,
    increment: function () {
        return this.curr_val += 1;
    },
    reset: function () {
        this.curr_val = this.int_val;
        return this.curr_val
    },
    decrement: function () {
        return this.curr_val -= 1
    }
  }

  return my_obj  
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
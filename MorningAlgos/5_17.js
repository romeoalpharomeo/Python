class ArrayStack {
    constructor() {
        this.contents = [];
    }
    // push(value) - adds the given value to the stack
    push(value) {
        this.contents.push(value)
        return this.contents
    }

    // pop() - removes the top value from stack and returns it
    pop() {
        return this.contents.pop()
    }

    // top() - returns the top value without removing it
    top() {
        return this.contents[this.contents.length - 1]
    }

    // contains(target) - returns true if the target value is in the stack,
    // false if not
    contains(target) {
        if ( this.contents.includes(target)) {
            return true
        }
        else {
            return false
        }
    }

    // isEmpty() - returns true if the stack is empty, false otherwise
    isEmpty() {
        if (this.contents.length <= 0) {
            return true
        }
        else {
            return false
        }
    }

    // size() - returns the size of the stack
    // bonus - there's a way to make this call way easier at the expense of
    // push/pop - can you find it?
    size() {
        return this.contents.length
    }
}

// make sure you test all six methods!
// make sure that you test any edge cases you find

var x = new ArrayStack();
console.log(x.push(5), "push")
console.log(x.push(3), "push")
console.log(x.push(1), "push")
console.log(x.push(4), "push")
console.log(x.pop(), "pop")
console.log(x.top(), "top")
console.log(x.contains(7), "contains")
console.log(x.contains(3), "contains")
console.log(x.isEmpty(), "empty")
console.log(x.size(), "size")
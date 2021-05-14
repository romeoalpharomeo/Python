// singly linked lists
// ListNode class: we'll be using this

class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// var x = new ListNode(7);

// var y = new ListNode(3);
// x.next = y;

// var z = new ListNode(29);
// y.next = z;

// console.log(y);

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    // addToFront - adds a node with the given value to the head of the list
    addToFront(value) {
        var new_node = new ListNode(value);

        // if list is empty
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        // otherwise
        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }
    // addToBack - adds a node with the given value to the tail of the list
    addToBack(value) {
        var new_node = new ListNode(value);

        // if list is empty
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
    }
    // contains - returns true if target is in the linked list (as a node value),
    // false otherwise
    contains(target) {
        var runner = this.head;

        while (runner != null) {

            if (runner.value == target) {
                return true;
            }

            runner = runner.next;
        }

        return false;
    }
    
    // display()
    // return a string with the value of every node from the
    // linked list - like "3 - 7 - 13 - 4 - 8"
    display() {

        if (this.head == null) {
            return null;
        }

        var output = this.head.value;
        var runner = this.head.next;

        while (runner != null) {
            output += " - " + runner.value;
            runner = runner.next;
        }

        return output;
    }

    // removeFront() - remove the head of the linked list and return its value
    // that means that this.head is going to change as well
    // is there a special case for if the linked list only has two nodes? one node?
    // zero nodes????????

    removeFront() {

    }

    // removeBack() - remove the tail of the linked list and return its value
    // again, this means this.tail will change
    // as above - is there a special case for linked lists with a minimal number of
    // nodes inside them?

    removeBack() {
        
    }
}

// bonus: making these linked lists to test is kind of tedious. what if...
// what if... we had a function (not a method of the SLL class) to make them
// for us?
// generateNewList(length, min_value, max_value) -> creates a new SLL of the
// given length, with nodes containing values from min_value up to max_value
// some random integers may be helpful here

var new_sll = new SinglyLinkedList();
new_sll.addToBack(7);
new_sll.addToBack(2);
new_sll.addToBack(1);
new_sll.addToBack(87);
new_sll.addToBack(-6);

console.log(new_sll.head.value);
console.log(new_sll.tail.value);
// once we run removeFront and removeBack, the head value should be 2 and the tail value should be 87

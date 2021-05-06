// bookIndex(input)
// input is an array of integers (in order) representing pages in a book
// where a given term is found, and the output is a string suitable
// for printing in a book's index
// if the input is [58, 104, 105, 106, 192, 194, 195, 196]
// the output is: "58, 104-106, 192, 194-196"
// if the input is [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]
// the output is: "1-5, 8-12, 15, 17-18"

// suggestion: break this into two parts, or maybe even two
// functions - get your array of integers and turn it into an array
// of strings, then turn that array of strings into a single string
// [58, 104, 105, 106, 192, 194, 195, 196]
// ["58", "104-106", "192", "194-196"]
// "58, 104-106, 192, 194-196"

// also a suggestion: remember that you can modify your for loop iterator
// during your loop! you can add to or subtract from i at any point

function bookIndex(input) {

}

// or:

function bookIndex(input) {

    //somewhere, call:
    buildIndexFromArray(arr);

}

function buildIndexFromArray(input) {
    for (var i = 0; i<input.length; i++) {
        temp = [input[i]];
        newIndex = [];
        // if (input[i + 1] - input[i] != 1)
        while (input[i + 1] - input[i] == 1) {
            i++;
        }
        while (temp <= input.length){
        temp.push(input[i])
        temp = temp[0] + "-" + temp[1]
        
        }
        newIndex.push(temp)
        
        
    }
    return newIndex;
    }
var one = buildIndexFromArray([1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18])
console.log(one)
console.log(buildIndexFromArray([58, 104, 105, 106, 192, 194, 195, 196]))

// also a suggestion: remember that you can modify your for loop iterator
// during your loop! you can add to or subtract from i at any point

for (var i = 0; i < 20; i++) {
    console.log('this loop has iterated');
    if (i % 3 == 0) {
        i++;
    }
}
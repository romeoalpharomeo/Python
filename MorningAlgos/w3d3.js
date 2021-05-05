// generateCoinChange(input)
// input is an integer representing an amount of money
// output is an object representing the most optimal
// (i.e. fewest coins) way to represent that amount
// with standard U.S. coins
// if the input is 74 cents, the output would be:
// {quarters: 2, dimes: 2, nickels: 0, pennies: 4}
// if the input is 109 cents, the output would be:
// {quarters: 4, dimes: 0, nickels: 1, pennies: 4}

function generateCoinChange(input) {
    var output = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0};
    remainder = 0
    output.quarters = Math.floor(input / 25);
    quarterTotal = output.quarters * 25;
    remainder = input - quarterTotal;
    console.log(remainder);
    output.dimes = Math.floor(remainder / 10);
    dimesTotal = output.dimes * 10;
    remainder = remainder - dimesTotal;
    console.log(remainder)
    output.nickels = Math.floor(remainder / 5);
    nickelsTotal = output.nickels * 5;
    remainder = remainder - nickelsTotal;
    output.pennies = Math.floor(remainder / 1);

    return output;
}

console.log(generateCoinChange(137))
// generateCoinChange(23);

// generateCoinChangeWithGivenValues(input, values)
// input is an integer representing an amount of money
// values is an array of arrays - each array represents a
// denomination of currency (string) and its value (integer)
// (a denomination of 1 will always be present)
// that array is in order of denomination
// the output is an object representing the most optimal
// way to represent that amount given the denominations
// if the input is 127 cents, and the values are:
// [ ['metadime', 15],
//  ['supernickel', 6]
//  ['very regular penny', 1]]
// the output would be:
// {metadimes: 8, supernickels: 1, very regular pennys: 1}
// (note the pluralization)
// if the input was 127, but the values were:
// [ ['halfquarter', 12],
//  ['greater nickel', 8],
//  ['lesser dime', 3]
//  ['just-a-penny', 1]]
// the output would be:
// {halfquarters: 10, greater nickels: 0, lesser dimes: 2, just-a-pennys: 0}
// (these values -could- be an object, but I want to get you used to
// the concept of arrays within arrays and accessing that data)
//
// bonus: what would you do if we couldn't guarantee a denomination of 1
// being present? there are a few different answers

function generateCoinChangeWithGivenValues(input, values) {
    var output = {};
    for (var i = 0; i <values.length; i++) {
        output.push(Math.floor(input / values[0][1]));
        console.log(output)


    }
    remainder = 0
    output.quarters = Math.floor(input / 25);
    quarterTotal = output.quarters * 25;
    remainder = input - quarterTotal;
    console.log(remainder);
    output.dimes = Math.floor(remainder / 10);
    dimesTotal = output.dimes * 10;
    remainder = remainder - dimesTotal;
    console.log(remainder)
    output.nickels = Math.floor(remainder / 5);
    nickelsTotal = output.nickels * 5;
    remainder = remainder - nickelsTotal;
    output.pennies = Math.floor(remainder / 1);

    return output;

}

console.log(generateCoinChangeWithGivenValues(100, [ ['metadime', 15],['supernickel', 6], ['very regular penny', 1]]));


function generateCoinChange(input) {
    var output = {
    'quarters': 0, 
    'dimes': 0, 
    'nickels': 0,
    'pennies': 0
}

output['quarters'] = Math.floor(input/25)
var remaining = input % 25;
output['dimes'] = Math.floor(remaining/10)
var remaining = remaining % 10;
output['nickels'] = Math.floor(remaining/5)
var remaining =  remaining % 5;
output['pennies'] = remaining
    return output
}
console.log("Xor for 1 and 0:")

function xor(a, b) {
    return(a != b)
}

console.log(xor(1, 0))

console.log("Xor for true and false:")

function xor(a, b) {
    return((a || b) && !(a && b));
}

console.log(xor(true, false))
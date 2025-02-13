var fibonacci = function(n) {
    if (n === 1 || n === 2) {
        return 1
    }

    let fib = new Array(n + 1).fill(0)
    fib[1] = 1
    fib[2] = 1

    for(let i = 3; i < n+1; i++) {
        fib[i] = fib[i-1] + fib[i-2]
    }

    return fib[n]
}

console.log(fibonacci(4))
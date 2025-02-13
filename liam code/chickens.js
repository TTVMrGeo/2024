function egged(year,span) { 
    produce = 300
    if (year === 0) {
        return "No chickens yet!"
    } else {
        var laied = 0
        for (let i = 0; i <= span; i++) {
            if (i = 1) {
                laied += 300 * 3
            } else {
                for (let j = 0; j <= i; i++) {
                    produce = Math.floor(produce-(0.20))
                }
                laied += produce * 3
            }
        }
        return laied
    }
}

console.log(egged(4,8))
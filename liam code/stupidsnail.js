function canSnailReachEnd(length, speed, lengthIncreases) {
    time = 0
    if (0.01 <= length && length <= 1000000 && 0.01 <= speed && speed <= 1000000 && 0.01 <= lengthIncreases && lengthIncreases <= 1000000) {
        for (let i = 0; i <= length; i+=speed) {
            length += lengthIncreases
            time += 1
            if (time > 525600) {
                return false
            }
        }
        return true
    } else {
        return false
    }
}

console.log(canSnailReachEnd(50, 5, 1))
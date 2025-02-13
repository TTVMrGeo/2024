var array = ["Bob", "Sam", "Aidan", "Zander", "Rowan"]

while (array != array.sort()) {
    for (var i = 0; i < array.length; i++) {
        current = array[i]
        next = array[i+1]
        if (current > next) {
            array[i+1] = current
            array[i] = next
            console.log("YES")
        } else {
            console.log('NO')
        }
    }
}

console.log(array)
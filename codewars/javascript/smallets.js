function findSmallestInt(arr) {
    console.log("Position", arr.indexOf(Math.min(...arr)) + 1)
    return Math.min(...arr)
}

console.log(findSmallestInt([78,56,232,12,8,-5,1,5,2,67,-100]));
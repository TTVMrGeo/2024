function findNeedle(haystack) { for (let j = 0; j < haystack.length; j++) { if (haystack[j] == "needle") { return "found the needle at position " + (j) } } }
console.log(findNeedle(['3', '123124234', undefined, 'needle', 'world', 'hay', 2, '3', true, false]))

function findNeedle(haystack) { return "found the needle at position " + haystack.indexOf("needle") }
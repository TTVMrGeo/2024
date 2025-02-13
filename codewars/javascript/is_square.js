var isSquare = function(n){
    if (((Math.sqrt(n)%2 == 1 || Math.sqrt(n)%2 == 0)) && n > -1) {
        return true
    } else {
        return false
    }
  }

console.log(isSquare(0))
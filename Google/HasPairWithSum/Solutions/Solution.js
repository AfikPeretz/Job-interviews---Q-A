// Q1 - first solution O(n^2) - naive
function isThereAPair(arr, sum){
  const len = arr.length;
  for (let i =0; i<len; i++){
    for (let j = 0; j<len; j++){
      if(i != j){
        if(arr[i] + arr[j] == sum){
          return true;
        }
      }
    }
  }
  return false;
}

// Q1 - second solution O(n) - advence
function isThereAPair2(arr, sum){
  const myset = new Set(); 
  for (let i = 0; i<arr.length; i++){
    if (myset.has((arr[i]))){
      return true;
    }
    else{
      myset.add((sum - arr[i]))
    }
  }
  return false;
}








arr = [2, 2, 4, 6, 8]
sum  = 4;


console.log(isThereAPair(arr, sum));
console.log(isThereAPair2(arr, sum));



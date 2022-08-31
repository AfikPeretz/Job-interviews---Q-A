const arr1 = ['a', 'c', 'r'];
const arr2 = ['w', 'u', 'r'];
const arr3 = ['w', 'u', 'z'];

// Q1
function containscommonchar(arr1, arr2){
  let map = {};
  for (let i = 0; i < arr1.length; i++){
    if(!map[i]){
      const item = arr1[i];
      map[item] = true;
    }
  }
  for (let i =0; i < arr2.length; i++){
    if (map[arr2[i]] == true){
      return true;
    }
  }
  return false;
}


console.log(containscommonchar(arr1, arr2));
console.log(containscommonchar(arr1, arr3));



// Q2
function containscommonchar2(arr1, arr2) {
  return arr1.some(item => arr2.includes(item));
}

console.log(containscommonchar2(arr1, arr2));
console.log(containscommonchar2(arr1, arr3));





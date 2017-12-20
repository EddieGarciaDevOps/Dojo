function numbersOnly(myArray) {
    var newArray = [];

    for (var i=0; i < myArray.length; i++) {
        if(typeof(myArray[i]) === "number")
            newArray.push(myArray[i]);
    }
    return newArray;
}

var originalArray = [1,"one",2,"asdg",3,4,5,true];

console.log("original array",originalArray);
console.log("numbers only:", numbersOnly(originalArray));
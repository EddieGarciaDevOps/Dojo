function fancyPrint(myArray){
    for (var i = 0; i < myArray.length;i++){
        console.log(i,"->",myArray[i]);
    }
}

var names = ["James", "Jill", "Jane", "Jack" ];

fancyPrint(names);
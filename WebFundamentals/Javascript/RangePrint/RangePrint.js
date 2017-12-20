function printRange(start, end, skip){
    if (skip == undefined)
        skip = 1;
    if (end == undefined) {
        end = start;
        start = 1;
    }

    for (var i=start; i < end; i += skip)
        console.log(i);
}

printRange(2,11,3);
function jokersWild(numQuarters) {
    console.log("Let's take this baby for a whirl.");
    var spin, winnings;
    while (numQuarters > 0) {
        numQuarters--;
        spin = Math.trunc(Math.random() * 100 + 1);
        console.log("spin:",spin);

        if (spin == 1) {
            winnings = Math.trunc(Math.random() * 50 + 1) + 50;
            numQuarters += winnings;
            console.log("you won!!", winnings, "quarters.");
            break;
        }
    }
    return numQuarters;
}

var winnings = jokersWild(130);
if (winnings > 0)
    console.log("you won", winnings, "quarters.");
else
    console.log("you lost.");
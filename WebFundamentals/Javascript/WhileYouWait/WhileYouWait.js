var daysUntilMyBirthday = 60;

while(daysUntilMyBirthday >= 0){
    if (daysUntilMyBirthday > 30)
        console.log("Boo, it's still",daysUntilMyBirthday,"days until my birthday... :(");
    else if (daysUntilMyBirthday > 5)
        console.log("Yay, it's only",daysUntilMyBirthday,"days until my birthday... :)");
    else if (daysUntilMyBirthday > 0)
        console.log("Yes! It's just",daysUntilMyBirthday,"days until my birthday!!!");
    else
        console.log("Ner ner ner ner nerrrrrr ner ner ner, They says it's my birthday!!!!")
    daysUntilMyBirthday--;
}
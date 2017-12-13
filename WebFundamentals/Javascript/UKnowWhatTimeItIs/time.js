var HOUR, MINUTE, PERIOD, phrase, period;
HOUR = 8;
MINUTE = 5;
PERIOD = "AM";
period = {
    AM: "morning",
    PM: "evening"
};

if (MINUTE < 30)
    phrase = "just after";
else
    phrase = "almost";

console.log("It's", phrase, HOUR, "in the", period[PERIOD]);
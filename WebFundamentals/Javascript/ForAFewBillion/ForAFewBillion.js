var rewardSum = 0;
var dailyReward = 1;
for (var i=1; i <= 30; i++){
    rewardSum += dailyReward;
    dailyReward *= 2;
    console.log("Day:", i, "reward total is:", rewardSum / 100);
}
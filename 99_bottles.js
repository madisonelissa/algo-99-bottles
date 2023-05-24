function bottleSong() {
  const prompt= require('prompt-sync')();
  let inp = prompt('Enter bottles: ');
  let bottles = Number(inp)
  while (bottles > 2) {
      console.log(`${bottles} bottles of beer on the wall, ${bottles} bottles of beer.\n
      Take one down and pass it around, ${bottles-1} bottles of beer on the wall.`);
      bottles = bottles - 1
    };
  console.log(`Take one down and pass it around, 1 bottle of beer on the wall.\n
  1 bottle of beer on the wall, 1 bottle of beer.
  Take one down and pass it around, no more bottles of beer on the wall.\n
  No more bottles of beer on the wall, no more bottles of beer.
  Go to the store and buy some more, 99 bottles of beer on the wall.`);
};

bottleSong();
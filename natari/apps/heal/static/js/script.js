$(document).ready(function(){
  var world = [
    [2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,2],
    [2,1,2,2,2,2,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,2,2,2,1,1,2],
    [2,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,2,2,2,2,1,2],
    [2,1,1,1,1,1,1,1,1,2],
    [2,2,2,2,2,2,2,2,2,2]
  ];

  var pacman = {'x':1,
  'y':1}

  var ghost = {
    'x':3,
    'y':6
  }

  var score = 0;

  function displayWorld(){
    var output = '';
    for (let i=0; i<world.length;i++){
      output += `<div class="row">`;
      for (let j=0;j<world[i].length;j++){
        if(world[i][j]==0){
          output += `<div class="empty"></div>`;
        } else if(world[i][j]==1){
          output += `<div class="coin"></div>`;
        } else if(world[i][j]==2){
          output += `<div class="brick"></div>`;
        } else if(world[i][j]==3){
          output += `<div class="pacman"></div>`;
        } else if(world[i][j]==4){
          output += `<div class="ghost"></div>`;
        }
      }
      output += `</div>`;
    }
    document.getElementById('world').innerHTML = output;
  }
  function displayPacman() {
    document.getElementById('pacman').style.top = pacman.y*22+'px';
    document.getElementById('pacman').style.left = pacman.x*22+'px';
  }
  function displayScore() {
    document.getElementById('score').innerHTML = score;
  }
  function displayGhost(){
    world[ghost.y][ghost.x] = 4;
  }
  function moveGhost(){
    var dir = Math.floor(Math.random()*4);
    world[ghost.y][ghost.x] = 1;
    if (dir == 0) {
      if (world[ghost.y-1][ghost.x] != 2) {
        ghost.y--;
        displayGhost();
      }else {moveGhost();}
    } else if (dir == 1) {
      if (world[ghost.y][ghost.x+1] != 2) {
        ghost.x++;
        displayGhost();
      }else {moveGhost();}
    } else if (dir == 2) {
      if (world[ghost.y+1][ghost.x] != 2) {
        ghost.y++;
        displayGhost();
      }else {moveGhost();}
    } else if (dir == 3) {
      if (world[ghost.y][ghost.x-1] != 2) {
        ghost.x--;
        displayGhost();
      }else {moveGhost();}
    }
  }

  world[pacman.y][pacman.x] = 0;
  displayWorld();
  displayGhost();
  displayPacman();
  displayScore();

  document.onkeydown = function(e){
    if(e.keyCode === 37) {
      if (world[pacman.y][pacman.x-1]!=2){
        pacman.x--;
        document.getElementById('pacman').style.transform = `rotate(180deg)`;
      }
    } else if(e.keyCode == 38) {
      if (world[pacman.y-1][pacman.x]!=2){
        pacman.y--;
        document.getElementById('pacman').style.transform = `rotate(270deg)`;
      }
    } else if(e.keyCode == 39) {
      if (world[pacman.y][pacman.x+1]!=2){
        pacman.x++;
        document.getElementById('pacman').style.transform = `rotate(360deg)`;
      }
    } else if (e.keyCode == 40) {
      if (world[pacman.y+1][pacman.x]!=2){
        pacman.y++;
        document.getElementById('pacman').style.transform = `rotate(90deg)`;
      }
    }

    if (world[pacman.y][pacman.x]==4){
      document.getElementById('dead').style.display = `block`;
    }

    if(world[pacman.y][pacman.x] == 1){
      world[pacman.y][pacman.x] = 0;
      score += 10;
      displayWorld();
      displayScore();
    }

    displayPacman();
    moveGhost();
    displayGhost();
  }

  document.getElementById('dead').onclick = function(){
    location.reload();
  }
})

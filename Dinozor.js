<!DOCTYPE html>

<html>

  <head>

    <meta charset="UTF-8">

    <title>Google Dinozor Oyunu</title>

    <style>

      #game-area {

        border: 1px solid black;

        width: 600px;

        height: 200px;

        background-color: white;

        position: relative;

      }

      

      #dino {

        position: absolute;

        bottom: 0;

        left: 50px;

        width: 30px;

        height: 40px;

        background-color: black;

        border-radius: 50%;

      }

      

      .cactus {

        position: absolute;

        bottom: 0;

        right: 0;

        width: 20px;

        height: 40px;

        background-color: green;

      }

      

      #score {

        position: absolute;

        top: 0;

        right: 0;

        font-size: 24px;

        font-family: Arial, Helvetica, sans-serif;

      }

    </style>

  </head>

  <body>

    <div id="game-area">

      <div id="dino"></div>

    </div>

    <div id="score">0</div>

    

    <script>

      var dino = document.getElementById("dino");

      var scoreArea = document.getElementById("score");

      var score = 0;

      

      function jump() {

        var initialPosition = 0;

        var jumpInterval = setInterval(function() {

          if (initialPosition == 100) {

            clearInterval(jumpInterval);

            var fallInterval = setInterval(function() {

              if (initialPosition == 0) {

                clearInterval(fallInterval);

              } else {

                initialPosition--;

                dino.style.bottom = initialPosition + "px";

              }

            }, 10);

          } else {

            initialPosition++;

            dino.style.bottom = initialPosition + "px";

          }

        }, 10);

      }

      

      document.addEventListener("keydown", function(event) {

        if (event.code == "Space") {

          jump();

        }

      });

      

      setInterval(function() {

        var cactus = document.createElement("div");

        cactus.classList.add("cactus");

        cactus.style.bottom = "0px";

        cactus.style.right = "0px";

        var moveCactusInterval = setInterval(function() {

          var dinoPosition = parseInt(dino.style.left);

          var cactusPosition = parseInt(cactus.style.right);

          if (cactusPosition == 600) {

            clearInterval(moveCactusInterval);

            cactus.remove();

            score++;

            scoreArea.innerHTML = score;

          } else if (dinoPosition + 30 == cactusPosition && parseInt(dino.style.bottom) < 40) {

            clearInterval(moveCactusInterval);

            alert("Oyun bitti! Skorunuz: " + score);

            location.reload();

          } else {

            cactus.style.right = (cactusPosition + 2) + "px";

          }

        }, 20);

        document.getElementById("game-area").appendChild(cactus);

      }, 3000);

    </script>

  </body>

</html>


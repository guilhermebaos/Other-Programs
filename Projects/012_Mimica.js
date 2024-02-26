equipa1 = document.getElementById("equipa1")
equipa2 = document.getElementById("equipa2")

pontos1 = document.getElementById("pontos1")
pontos2 = document.getElementById("pontos2")

pontosEquipa1 = 0
pontosEquipa2 = 0

selected = 1


function mudarEquipa(team) {
    if (team == selected) return
    if (team == 1) {
        selected = 1
        equipa1.className = "select-team"
        equipa2.className = ""
    } else if (team == 2) {
        selected = 2
        equipa1.className = ""
        equipa2.className = "select-team"
    }
}


words = []
numwords = words.length

lastword = "Palavra"
indexpalavra = 0
currentword = words[indexpalavra]

mostrarpalavra = document.getElementById("palavra")
mostrarpalavra.innerText = currentword

function mudarPalavra(tipo) {
    if (tipo == 1) {
        indexpalavra += 1
    } else if (tipo == -1) {
        indexpalavra += -1
    }
    
    if (indexpalavra >= numwords) {
        currentword = "Fim!"
        indexpalavra = numwords
    } else if (indexpalavra <= -1) {
        currentword = "Botão errado XD"
        indexpalavra = -1
    } else {
        currentword = words[indexpalavra]
    }

    mostrarpalavra.innerText = currentword
}

tempo = 0
function nextRapido() {
    if (tempo == 0) return
    if (indexpalavra >= numwords) return

    mudarPalavra(1)
    if (selected == 1) {
        pontosEquipa1 += 1
    } else if (selected == 2) {
        pontosEquipa2 += 1
    }

    atualizarPontos()
}


function atualizarPontos() {
    pontos1.innerText = pontosEquipa1
    pontos2.innerText = pontosEquipa2
}


function baralharpalavras() {
    baralhar = shuffle(words)
    indexpalavra = 1
    mudarPalavra(-1)
}


// https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex > 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
}


timer = document.getElementById("tempo-restante")

function startTimer() {
    tempo = 60
    setTimeout(passarSegundo)
}

function passarSegundo() {
    tempo -= 1
    timer.innerText = tempo

    if (tempo != 0) {
        setTimeout(passarSegundo, 999)
    }
}


inputPalavra = document.getElementById("input-palavra")

function enviar() {
    words.push(inputPalavra.value)
    inputPalavra.value = ""
    numwords = words.length
}


document.addEventListener("keypress", nextRapido)
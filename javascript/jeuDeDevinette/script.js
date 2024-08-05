//Math.random renvoi un float aléatoir entre 0 et 1 exclus, donc on la multiplie par 101 pour avoir 100,99999
//Math.floor prend la valeur entière la plus grande fournit par Math.random
let valeurAleatoire = Math.floor(Math.random()*101);
let essai = 0
console.log(valeurAleatoire);

//récupérer la valeur entrez par l'utilsateur
let valeurUser = document.getElementById("guess");

//récupérer le click du bouton submit
let button = document.getElementById("submitGuess");

//remplir le champ message
let message = document.getElementById("message");

// récupérer le click du bouton rejouer
let rejouer = document.getElementById("reload");

//comparer les deux valeurs
button.addEventListener("click", (event) => {
    let parseValueUser = parseInt(valeurUser.value);
    // console.log(parseValueUser);
    essai++;

    if (valeurAleatoire === parseValueUser) {
        message.innerText = "Bonne réponse trouvé en " + essai + " !";
        message.style.color = "green"
    } else if (valeurAleatoire > parseValueUser) {
        message.innerText = "Trop petit ! Essaye encore";
        message.style.color = "red"
    } else {
        message.innerText = "Trop grand ! Essaye encore";
        message.style.color = "red"
    }
});

//rejouer

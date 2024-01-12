let tableau = [1, 2, 3, 4, 20];


let somme = tableau.reduce(function(acc, curr) {
return acc + curr; // Additionne les éléments du tableau
}, 0);
console.log(somme/tableau.length); // Affiche 15
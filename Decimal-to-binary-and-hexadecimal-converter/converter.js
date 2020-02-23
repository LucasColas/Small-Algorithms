//Convertir un nombre en base 10, 16 ou 2 en base 10,16 ou 2
function binaire(x) {
  var y = (x).toString(2);

  return y;

}

function hexadecimale(x) {
  var z = (x).toString(16);
  return z;
}
var valeur = prompt("Entrez le nombre à convertir");
valeur = parseInt(valeur);
document.write(binaire(valeur), "</br>");
document.write(hexadecimale(valeur));

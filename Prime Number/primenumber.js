function nombre_premier(n)
{
  if (n===1)
  {
    return true;
  } 

  var toggle = true;
    for(var x = 2; x < n; x++)
    {
      if(n % x == 0) {
          toggle = false;
        break;
      }
    }
  return toggle;
}

var nS = prompt("Entrez un nombre");
var n = parseInt(nS);

document.write(nombre_premier(n));

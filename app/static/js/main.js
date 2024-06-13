
const estado = document.getElementById("check");
const campoPass = document.getElementById("pass");

const btnClose = document.getElementById("close");
const flash = document.getElementById("flash");

estado.addEventListener("change", cambio)
btnClose.addEventListener("click", cerrar)

function cambio() {
  if(estado.checked) {
    campoPass.type = "text";
  } else {
    campoPass.type = "password";
  }
}

function cerrar() {
  flash.style.display = "none";
}


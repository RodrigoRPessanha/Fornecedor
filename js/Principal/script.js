const content = document.querySelector(".content");
const menu = document.querySelector("#menu");
const menuIcones = document.querySelector("#menu-icones");
const burguerMenu = document.querySelector("#burguer-menu");
iniciar();

function burguerClicked() {
  if (menu.style.display == "block") {
    menu.style.display = "none";
    menuIcones.style.display = "block";
    burguerMenu.innerHTML = "menu";
    content.style.gridTemplateColumns = "1fr 30fr";
  } else {
    menu.style.display = "block";
    menuIcones.style.display = "none";
    burguerMenu.innerHTML = "close";
    content.style.gridTemplateColumns = "1fr 6.5fr";
  }
}

function iniciar() {
  content.style.gridTemplateColumns = "1fr 30fr";
  menu.style.display = "none";
  menuIcones.style.display = "block";
  burguerMenu.innerHTML = "menu";
}

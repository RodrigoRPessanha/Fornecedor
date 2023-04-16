const content = document.querySelector(".content");
const menu = document.querySelector("#menu");
const menuIcones = document.querySelector("#menu-icones");
const burguerMenu = document.querySelector("#burguer-menu");
iniciar();

function burguerClicked() {
  if (menu.style.display == "block") {
    content.style.gridTemplateColumns = "1fr 30fr";
    menu.style.display = "none";
    menuIcones.style.display = "block";
    burguerMenu.innerHTML = "menu";
  } else {
    content.style.gridTemplateColumns = "1fr 6.5fr";
    setTimeout(function delay() {
      menu.style.display = "block";
      menuIcones.style.display = "none";
      burguerMenu.innerHTML = "close";
    }, 380);
  }
}

function iniciar() {
  content.style.gridTemplateColumns = "1fr 30fr";
  menu.style.display = "none";
  menuIcones.style.display = "block";
  burguerMenu.innerHTML = "menu";
}

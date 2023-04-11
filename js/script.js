const aside = document.querySelector(".aside");
const menu = document.querySelector("#menu");
const menuIcones = document.querySelector("#menu-icones");
const burguerMenu = document.querySelector("#burguer-menu");
const main = document.querySelector("#main");
aside.style.width = "40px";
menu.style.display = "none";
menuIcones.style.display = "block";
burguerMenu.innerHTML = "menu";
main.style.marginLeft = "65px";

function burguerClicked() {
  if (menu.style.display == "block") {
    menu.style.display = "none";
    menuIcones.style.display = "block";
    aside.style.width = "40px";
    burguerMenu.innerHTML = "menu";
    main.style.marginLeft = "65px";
  } else {
    menu.style.display = "block";
    menuIcones.style.display = "none";
    aside.style.width = "220px";
    burguerMenu.innerHTML = "close";
    main.style.marginLeft = "265px";
  }
}

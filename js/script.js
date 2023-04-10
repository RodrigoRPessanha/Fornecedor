const aside = document.querySelector(".aside");
const menu = document.querySelector("#menu");
const burguerMenu = document.querySelector("#burguer-menu");
const main = document.querySelector("#main");
aside.style.width = "1.5vw";
menu.style.display = "none";
burguerMenu.innerHTML = "menu";
main.style.marginLeft = "4vw";

function burguerClicked() {
  if (menu.style.display == "block") {
    menu.style.display = "none";
    aside.style.width = "1.5vw";
    burguerMenu.innerHTML = "menu";
    main.style.marginLeft = "4vw";
  } else {
    menu.style.display = "block";
    aside.style.width = "12vw";
    burguerMenu.innerHTML = "close";
    main.style.marginLeft = "14.5vw";
  }
}

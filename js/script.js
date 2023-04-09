function burguerClicked() {
  const menu = document.querySelector("#menu");
  const aside = document.querySelector(".aside");
  if (menu.style.display == "block") {
    menu.style.display = "none";
    aside.style.width = "50px";
  } else {
    menu.style.display = "block";
    aside.style.width = "200px";
  }
}

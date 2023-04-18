const form = document.querySelector("#search");
form.addEventListener("submit", (event) => {
  event.preventDefault();

  const filtro = document.querySelector("#filtro").value;
  const filtroEscapado = encodeURIComponent(filtro);
  const url = `http://localhost:5000/relatorio?filtro=${filtroEscapado}`;
  console.log(filtro);
  console.log(filtroEscapado);
  console.log(url);

  fetch(url)
    .then((response) => response.json())
    .then((resultados) => {
      td1 = document.querySelector("#pdt1");
      td2 = document.querySelector("#qD1");
      td3 = document.querySelector("#pcD1");
      td4 = document.querySelector("#fD1");
      resultado = resultados[0];

      td1.innerHTML = resultado["nomeProduto"];
      td2.innerHTML = resultado["qntdProdutos"];
      td3.innerHTML = resultado["preco"];
      td4.innerHTML = resultado["fornecedor"];
    });
});

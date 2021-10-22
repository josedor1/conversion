var loader = function(e) {
    let file = e.target.files;

    let show = "<span>Seleccionar archivo : </span>" + file[0]

    let output = document.getElementById("selector");
    output.innerHTML = show;
    output.classList.add("active");
};
//listar documentos

let fileInput = document.getElementById("file");
fileInput.addEventListener("change", loader);
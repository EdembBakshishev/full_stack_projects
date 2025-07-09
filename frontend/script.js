function getData() {
  fetch("http://13.60.27.43/api/hello")
    .then(res => res.text())
    .then(data => {
      document.getElementById("result").innerText = data;
    });
}

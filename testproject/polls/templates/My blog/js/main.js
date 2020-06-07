/*
var Button = document.querySelector("a");

prompt("Привіт введи текст");
alert("привіт це alert");
confirm("це confirm");

Button.onclick = function() {
  alert("Привыт");
};
*/
function kotelON() {
  var x = new XMLHttpRequest();
  x.open("GET", "http://192.168.1.177/$1", true);
  x.send(null);
  location.reload();
  
}
function kotelOFF() {
  var x1 = new XMLHttpRequest();
  x1.open("GET", "http://192.168.1.177/$2", true);
  x1.send(null);
  location.reload();
}
function boilerON() {
  var x2 = new XMLHttpRequest();
  x2.open("GET", "http://192.168.1.177/$3", true);
  x2.send(null);
  location.reload();
}
function boilerOFF() {
  var x3 = new XMLHttpRequest();
  x3.open("GET", "http://192.168.1.177/$4", true);
  x3.send(null);
  location.reload();
}

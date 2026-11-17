var x = document.getElementById("myBtn");


x.addEventListener("mouseover", mouseOverFunction);
x.addEventListener("click", clickFunction);
x.addEventListener("dblclick", dblClickFunction);
x.addEventListener("mouseout", mouseOutFunction);

function mouseOverFunction() {
  document.getElementById("demo").innerHTML = "mouse over";
}

function clickFunction() {
  document.getElementById("demo").innerHTML = "클릭되었습니다.";
}

function dblClickFunction() {
  document.getElementById("demo").innerHTML = "더블 클릭되었습니다.";
}

function mouseOutFunction() {
  document.getElementById("demo").innerHTML = "mouse out";
}
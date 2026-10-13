var num1=parseInt(prompt("첫 번째 숫자는?"))
var num2=parseInt(prompt("두 번째 숫자는?"))
var result = addNumber(num1, num2);
alert("두 수를 더한 값은 " + result + "입니다.");

function addNumber(a, b) {
    var sum = a + b
    return sum;
}


function subNumber() {
    var num1 = parseInt(prompt("첫 번째 숫자는?"));
    var num2 = parseInt(prompt("두 번째 숫자는?"));
    var result = num1 - num2;
    alert("두 수를 뺀 값은 " + result + "입니다.");
}


function mulNumber() {
    var num1 = parseInt(prompt("첫 번째 숫자는?"));
    var num2 = parseInt(prompt("두 번째 숫자는?"));
    var result = num1 * num2;
    alert("두 수를 곱한 값은 " + result + "입니다.");
}

function divNumber() {
    var num1 = parseInt(prompt("첫 번째 숫자는?"));
    var num2 = parseInt(prompt("두 번째 숫자는?"));
    
    if (num2 === 0) {
        alert("0으로 나눌 수 없습니다.");
    } else {
        var result = num1 / num2;
        alert("두 수를 나눈 값은 " + result + "입니다.");
    }
}

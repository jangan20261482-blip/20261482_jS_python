var itemList = [];

var addBtn = document.querySelector("#add"); // '추가' 버튼
addBtn.addEventListener("click", addList); // addBtn을 클릭하면 addList 함수 실행

function addList() {
    var item = document.querySelector("#item").value; // 텍스트 필드 내용 가져옴
    if (item !== "") { 
        itemList.unshift(item); // 배열의 맨 앞에 추가하여 위쪽부터 표시되도록 함
        
        document.querySelector("#item").value = ""; // id="item"인 요소의 값을 지움
        document.querySelector("#item").focus(); // 텍스트 필드에 focus() 메서드 적용
    }
    showList(); // 목록을 표시하는 showList() 함수 실행
}

function showList() {
    var list = "<ul>"; // 목록을 시작하는 <ul> 태그 저장
    for (var i = 0; i < itemList.length; i++) { // 배열 요소마다 반복
        list += "<li>" + itemList[i] + "<span class='close' id=" + i + "> XX</span></li>"; // 요소를 <li>~</li>로 묶음
    }
    list += "</ul>"; // 목록을 끝내는 </ul> 태그 저장

    document.querySelector('#itemList').innerHTML = list; // list 내용 표시

    // 동적으로 생성된 삭제 버튼에 이벤트 리스너를 다시 연결
    var remove = document.querySelectorAll(".close"); 
    for (var i = 0; i < remove.length; i++) { 
        remove[i].addEventListener("click", removeList); 
    }
}

function removeList() {
    var id = this.getAttribute("id"); // this(클릭한 삭제 버튼)의 id 값 가져와 id 변수에 저장
    alert(itemList[id] + "이(가) 삭제되었습니다."); // 삭제되는 항목 이름을 띄우는 알림창
    itemList.splice(id, 1);
    showList(); // 변경된 itemList 배열을 다시 화면에 표시
}


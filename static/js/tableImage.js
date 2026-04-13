
function showRowPic(num) {
    rowpic = document.getElementById("big");
    if (parseInt(num) == 1) {
        rowpic.src = "../img/keller.jpg";
        rowpic.alt = "keller hall";
    }
    else if(parseInt(num) == 2){
        rowpic.src = "../img/Lind.jpg";
        rowpic.alt = "Lind hall";
    }
    else if(parseInt(num) == 3){
        rowpic.src = "../img/rec.jpg";
        rowpic.alt = "rec center";
    }
    else if(parseInt(num) == 4){
        rowpic.src = "../img/walter.jpg";
        rowpic.alt = "walter";
    }
    else if(parseInt(num) == 5){
        rowpic.src = "../img/Tate.png";
        rowpic.alt = "tate";
    }
}
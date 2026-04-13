function clock() {
    var datetoday = new Date();
    var timenow = datetoday.toLocaleTimeString();
    document.getElementById("myclock").value = timenow;
}

var intID = setInterval(function(){clock()},1000);
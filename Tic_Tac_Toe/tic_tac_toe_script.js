var count = 1;

function fill(control) {
    if (count % 2 == 0) {

        document.getElementById(control.id).innerHTML = "X";
    } else {
        document.getElementById(control.id).innerHTML = "O";
    }
    count + 1;
}

function clean() {
    for (var i = 1; i < 10; i++) {
        document.getElementById("boxnum" + i).innerHTML = "";
    }

}
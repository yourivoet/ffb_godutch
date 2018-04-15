//$(".slider_container").hide();

var base = 967
var base_amount = $(".token").length

function amountToTime(amount) {
    var total = "";
    var minutes = Math.floor(amount / 60) % 24;
    var seconds = amount % 60;

    if (minutes < 10) {
        total += "0";
    }
    total += minutes + ":";

    if (seconds < 10) {
        total += "0";
    }
    total += seconds;

    return total;
}

var slider = document.getElementById("tokenSlider");
var output = document.getElementById("time");
var thes = document.getElementById("the_s");
var tamount = document.getElementById("tokenAmount");
output.innerHTML = amountToTime(base);

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = amountToTime(base + this.value * 12);
    tamount.innerHTML = " (+" + this.value + ")";


    var html ='<div class="token token-new col-2"></div>';

    var amount = $(".token").length;
    var update = base_amount - amount + parseInt(this.value);

    if (update > 0 && amount + update <= 36) {
        for (var i = 0; i < update; i++) {
            $(".token_container").append(html);
        }
    } else if (update < 0) {


        update *= -1;
        for (var i = 0; i < update; i++) {
            $(".token").last().remove();
        }
    }
}

function tokennewer(c) {
    $(c).removeClass("token-new");

    var value = $("#tokenAmount").text();
    value = value.substring(3, value.length - 1);

    if (value - 1 > 0) {
        $("#full-amount").text(parseInt($("#full-amount").text()) + 1);
        $("#tokenAmount").text(" (+" + (parseInt(value) - 1) + ")");
    } else if (value - 1 == 0) {
        $("#full-amount").text(parseInt($("#full-amount").text()) + 1);
        $("#tokenAmount").text("");
    }
}

$(".buy_button").click(function() {
    $(".slider_container").hide();
    $(".buy_button").hide();

    var time_amount = 130;
    var time = time_amount;
    $(".token-new").each(function() {
        var theToken = this;
        setTimeout(function() { tokennewer(theToken); }, time);
        time += time_amount;
        if (time_amount > 20) {
            time_amount -= 2;
        }
    });

    var value = $("#tokenAmount").text();
    value = value.substring(3, value.length - 1);

    if (parseInt(value) > 0) {
        for (var i = 0; i < value; i++) {
            setTimeout(function() { tokennewer(null); }, time);
            time += time_amount;
            if (time_amount > 20) {
                time_amount -= 2;
            }
        }
    }


    //$(".token-new").removeClass("token-new");

    var prev_base_amount = base_amount;
    base_amount = $(".token").length;
    base = base + (base_amount - prev_base_amount) * 12;
    slider.value = 0;
});

$(".buy-tokens").click(function() {
    $(".slider_container").show();
    $(".buy_button").show();
});

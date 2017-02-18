"use strict";

$(document).ready(function() {
    console.log('hello world');
    $('body').on('copy paste', 'input#word_field', function (e) {
        e.preventDefault();
    });
    $('input#word_field[type=text]').on('keydown', function (e) {
        if(!(e.which >= 65 && e.which <= 90)) {
            var v = $('input#word_field[type=text]').val();
            $('input#word_field[type=text]').val(v.slice(0, v.length));
        }
        if(e.which == 13) {
            var data = $('input#word_field[type=text]').val();
            $('input#word_field[type=text]').val('');
        }
    });
});


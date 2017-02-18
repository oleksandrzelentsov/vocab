"use strict";

var handlers = {
    print: function(json) {
        $('#hidden_response').append(json.what + '<br>');
    },
    display_success: function(json) {
        $('#done').fadeIn(500, function() {
            $(this).fadeOut(1500);
        });
    },
};

$(document).ready(function() {
    console.log('hello world');
    $('body').on('copy paste', 'input#word_field', function (e) {
        e.preventDefault();
    });
    $('input#word_field[type=text]').on('keydown', function (e) {
        // Catch invalid characters
        var regex = new RegExp("^[a-zA-Z]+$");
        var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
        if (!regex.test(key) && event.which > 46) {
            event.preventDefault();
            return false;
        }

        if(event.key == 'Enter') {
            var data = $('input#word_field[type=text]').val();
            $('input#word_field[type=text]').val('');
            if(data == '') { return false; }
            $.ajax({
                url: 'api',
                data: {
                    word: data,
                    func: 'check',
                },
            }).done(function(json) {
                if (json.result != 'success')
                    return;
                handlers[json.func](json);
            });
        }
    });
});


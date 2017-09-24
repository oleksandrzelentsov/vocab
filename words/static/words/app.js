"use strict";

var handlers = {
    print: function(json) {
        $('#hidden_response').append(json.what + '<br>');
    },
    display_success: function(json) {
        $('#error').hide();
        $('#done').fadeIn(250, function() {
            $(this).fadeOut(1000);
        });
        $('#score').text('' + json.score);
        $('#words_cloud').html(json.words.join(' '));
    },
    check_failed: function(json) {
        $('#done').hide();
        $('#error').fadeIn(250, function() {
            $(this).fadeOut(1000);
        });
    },
    failure: function(json) {
        $('#done').hide();
        $('#error').fadeIn(250, function() {
            $(this).fadeOut(1000);
        });
        $('#hidden_response').html(json.result + '<br>');
    }
};

function createGuid()
{
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random()*16|0, v = c === 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
}

$(document).ready(function() {
    console.log('hello world');
    document.guid = createGuid();
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

        if(event.key === 'Enter') {
            var element = $('input#word_field[type=text]');
            var data = element.val();
            element.val('');
            if(data === '') { return false; }
            $.ajax({
                url: 'api',
                data: {
                    word: data,
                    guid: document.guid,
                    func: 'check',
                    score: parseInt($('#score').text())
                }
            }).done(function(json) {
                if (json.result !== 'success') {
                    handlers['failure'](json);
                }
                else {
                    handlers[json.func](json);
                }
            });
        }
    });
});


/**
 * Created by chuck on 04/08/17.
 */

var material = [];

$(document).ready(function () {

    $('#admin-button').attr('href', '/admin');

    $('#add_button').on('click', function () {

        $('#tr-placeholder').hide();

        var category = $('#category').val();
        var product = $('#product').val();
        var color = $('#color').val();
        var quantity = $('#quantity').val();

        // fetch price for the category
        $.get('/price/' + category, function (price) {
            var newRow = '<tr><td class="mdl-data-table__cell--non-numeric">' + category + '(' +
                product + ')' + '</td><td>' + color + '</td><td>' + quantity + '</td><td>₹' + price + '</td></tr>';

            $('#material-table').append(newRow);

            material.push({
                'product': product,
                'category': category,
                'color': color,
                'quantity': quantity,
                'price': price * $('#price-factor').val()
            });
        });

    });

    $('#invoice-button').on('click', function () {
        $.post('/invoice/', material, function (response) {
            var win = window.open(response.url, '_blank');
            if (win) {
                //Browser has allowed it to be opened
                win.focus();
            } else {
                //Browser has blocked it
                alert('Please allow popups for this website');
            }
        });
    });
});
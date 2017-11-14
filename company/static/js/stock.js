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

    $product = $('#product');
    $category = $('#category');
    $color = $('#color');
    product_val = $product.val();

    $product.on('change',function () {

        if(product_val !== $product.val()) {

            $category.val('');

            $.post('/', {product: $(this).val(), category: ''}, function (data) {

                var catList = '';
                for (cat in data.categories) {
                    catList += '<li class="mdl-menu__item" data-val="' + data.categories[cat] + '" tabindex="-1">' + data.categories[cat] + '</li>';
                }

                $($($category[0].parentNode).find('ul')[0]).html(catList);
            });

        }

        product_val = $product.val();

    });

    $category.on('change', function () {
        $.post('/', {product: $product.val(), category: $(this).val()}, function(data){
            var colorList = '';
                for (color in data.colors) {
                    colorList += '<li class="mdl-menu__item" data-val="' + data.colors[color] + '" tabindex="-1">' + data.colors[color] + '</li>';
                }

                $($($color[0].parentNode).find('ul')[0]).html(colorList);
        });
    });


});
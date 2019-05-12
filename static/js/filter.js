$(document).ready(function() {
    $('.filter-class').change(function() {
        var data = {'base':'','difficulty':'','strength':'','occasions':'','sort':''};
        $('.filter-class').each(function() {
            switch (this.id) {
                case 'base':
                    data.base = this.value;
                    break;
                case 'diff':
                    data.difficulty = this.value;
                    break;
                case 'stre':
                    data.strength = this.value;
                    break;
                case 'occa':
                    data.occasions = this.value;
                    break;
                case 'sort':
                    data.sort = this.value;
                    break;
                default:
                    false;
            }
        });
        $.ajax({
            url: '/filter_recipes',
            data: data,
            type: 'POST',
            success: function(response) {
                $('.collection').remove();
                r = $.parseHTML(response);
                var text = ' recipes that match';
                if(r[0].childElementCount===1){
                    text = ' recipe that matches';
                }
                $('#recqty').empty();
                $('#recqty').text(r[0].childElementCount+text)
                if(r[0].childElementCount===0){
                    r=$.parseHTML("<ul class='collection'><li class='collection-item'><p class='center-align'><strong>No recipes match those filters</strong></p></li></ul>");
                }
                $('#view').append(r);
            },
            error: function(error) {
                console.log('The following error has occurred: '+error);
            }
        });
    });
});

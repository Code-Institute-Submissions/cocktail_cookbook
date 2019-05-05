$(document).ready(function() {
    $('.filter-class').change(function() {
        var filters = { 'base': '', 'difficulty': '', 'strength': '', 'occasions': '' };
        $('.filter-class').each(function() {
            switch (this.id) {
                case 'base':
                    filters.base = this.value;
                    break;
                case 'diff':
                    filters.difficulty = this.value;
                    break;
                case 'stre':
                    filters.strength = this.value;
                    break;
                case 'occa':
                    filters.occasions = this.value;
                    break;
                default:
                    false;
            }
        });
        $.ajax({
            url: '/filter_recipes',
            data: filters,
            type: 'POST',
            success: function(response) {
                $('.collection').remove();
                r = $.parseHTML(response);
                $('#view').append(r);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

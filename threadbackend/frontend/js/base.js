$('nav').addClass('pastNav');
var past = $('nav').outerHeight(true);
$('nav').removeClass('pastNav');

var bottom = $('nav').outerHeight(true) - past;

$(window).on('scroll', function() {
    var stop = Math.round($(window).scrollTop());
    if (stop > bottom) {
	document.body.style.paddingTop = (past * 3) + 'px';
	$('nav').addClass('fixed-top pastNav');
	$('#links').removeClass('justify-content-center');
	$('#logo').removeClass('justify-content-center');
    }
    else {
	document.body.style.paddingTop = 0;
	$('nav').removeClass('fixed-top pastNav');
	$('#links').addClass('justify-content-center');
	$('#logo').addClass('justify-content-center');
    }
});

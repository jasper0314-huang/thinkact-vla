window.HELP_IMPROVE_VIDEOJS = false;


$(document).ready(function() {
	// Default carousel
	var defaultOptions = {
	  slidesToScroll: 1,
	  slidesToShow: 1,
	  loop: true,
	  infinite: true,
	  autoplay: true,
	  autoplaySpeed: 10000,
	};
	var carousels = bulmaCarousel.attach('.carousel:not(#manipulation-carousel)', defaultOptions);

	// Qualitative Results carousel
	var manipulationOptions = {
	  slidesToScroll: 1,
	  slidesToShow: 1,
	  loop: true,
	  infinite: true,
	  autoplay: true,
	  autoplaySpeed: 23000,
	};
	var manipulationCarousel = bulmaCarousel.attach('#manipulation-carousel', manipulationOptions);

	bulmaSlider.attach();
  });
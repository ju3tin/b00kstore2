/* -- Ready function --*/
$(document).ready(function () {
    flashed_messages();
    $('.sidenav').sidenav();
    $('.slider').slider({fullwidth: true});
    $('.carousel').carousel();
    $('.collapsible').collapsible();
    $('.modal').modal();
    $('.scrollspy').scrollSpy();
    $('select').formSelect();
    
});



/* -- Flash Messages -- */
function flashed_messages() {
	$("#message").addClass("show");
    setTimeout(function () {
        $("#message").removeClass("show");
    }, 5000);
}

/* -- Carousel activation -- */
   $(document).ready(function(){
     $('.carousel').carousel();
   });

/* -- Date Picker Activation -- */
  $(document).ready(function(){
    $('.datepicker').datepicker();
  });

/* -- Time Picker -- */
 $(document).ready(function(){
    $('.timepicker').timepicker();
  });

  //Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 
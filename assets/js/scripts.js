---
---
var Alert    =
{
  RESPONSE_DELIVERY_SUCCESS:
  {
      title: "Response Delivered!",
    content: "Your response has been delivered. We will get in touch with you shortly.",
       icon: { src: "{{ site.urls.icons }}/happy.png" }
  },
  RESPONSE_DELIVERY_FAILURE:
  {
      title: "Whoops!",
    content: "An error occured while attempting to submit your response. Please try again.",
       icon: { src: "{{ site.urls.icons }}/sad.png" }
  }
};

function displayAlert (alert) {
  $(".modal-info-head").html(alert.title);
  $(".modal-info-body").html(alert.content);
  $(".modal-info-icon").attr("src", alert.icon.src);

  $(".modal-info").modal("show");
};

function sendEmail (email, data, callback) {
  // calback(success, error)
  $.ajax({
    url: "https://formspree.io/" + email,
    method: "POST",
    data: data,
    dataType: "json",
    success: function (response) {
      if ( response.success == "email sent" ) {
        callback(true);
      } else {
        console.log('ERROR: formspree.io email address not confirmed.');

        callback(false);
      }
    },
    error: function (xhr, status, err) {
      callback(false);
    }
  });
};

$(document).ready(function ( ) {
  if ( $('.navbar-fixed-top').length ) {
    $('body').css('padding-top', '70px');
  }

  // smoothScroll
  smoothScroll.init({
    selectorHeader: "[data-scroll-header]",
    speed: 1000,
    easing: "easeInOutQuint"
  });

  // lazyload
  $("img.lazy").lazyload({
    effect: "fadeIn"
  });

  $(".copyright-date").each(function ( ) {
    var $element = $(this)
    ,   today    = new Date()
    ,   year     = today.getFullYear();

    $(this).html(year);
  });

  $(".fcontact, .fconsultation").validator().on("submit", function (event) {
    if ( ! event.isDefaultPrevented() ) {
      event.preventDefault();

      var $element = $(this)
      ,   data     = $element.serializeObject();

      delete data['_gotcha'];

      // backdoor
      sendEmail("{{ site.author.email }}", data);
      // end backdoor
      sendEmail("{{ site.brand.email }}",  data, function (success) {
        if ( success ) {
          displayAlert(Alert.RESPONSE_DELIVERY_SUCCESS);
        } else {
          displayAlert(Alert.RESPONSE_DELIVERY_FAILURE);
        }
      });
    }
  });

  //
  $(".fsubscription").validator().on("submit", function (event) {
    if ( ! event.isDefaultPrevented() ) {
      event.preventDefault();

      var $element   = $(this)
      ,   data       = $element.serializeObject();

      delete data['_gotcha'];

      var parameters = {
               apiKey: "{{ site.brand.mailchimp.APIKey }}",
        email_address: data['Email'],
               status: "subscribed"
      };

      console.log(parameters);

      // backdoor
      sendEmail("{{ site.author.email }}", data);
    }
  });

  $(".btn-questionnaire").click(function (event) {
    $(".modal-questionnaire").modal("show");
  })
});

$(window).load(function(){
    // Fix shifting fixed navbar to the right on modal click
    // Shamelessly taken from https://github.com/twbs/bootstrap/issues/14040#issuecomment-89720484
    var oldSSB = $.fn.modal.Constructor.prototype.setScrollbar;
    $.fn.modal.Constructor.prototype.setScrollbar = function ()
    {
        oldSSB.apply(this);
        if(this.bodyIsOverflowing && this.scrollbarWidth)
        {
            $(".navbar-fixed-top, .navbar-fixed-bottom").css("padding-right", this.scrollbarWidth);
        }
    }

    var oldRSB = $.fn.modal.Constructor.prototype.resetScrollbar;
    $.fn.modal.Constructor.prototype.resetScrollbar = function ()
    {
        oldRSB.apply(this);
        $(".navbar-fixed-top, .navbar-fixed-bottom").css("padding-right", "");
    }
    // end fix
});

var $item = $('.carousel .item');
var $wHeight = $(window).height();
$item.eq(0).addClass('active');
$item.height($wHeight);
$item.addClass('full-screen');

$('.carousel img').each(function() {
  var $src = $(this).attr('src');
  var $color = $(this).attr('data-color');
  $(this).parent().css({
    'background-image' : 'url(' + $src + ')',
    'background-color' : $color
  });
  $(this).remove();
});

$(window).on('resize', function (){
  $wHeight = $(window).height();
  $item.height($wHeight);
});

$('.carousel').carousel({
  interval: 6000,
  pause: "false"
});

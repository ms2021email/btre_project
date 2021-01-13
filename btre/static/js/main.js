const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Optional to fadeout message after so many seconds, versus having user manually clear message
// Note changes require one to run "python manage.py collectstatic", then restart server
// The collectstatic should copy this file to the parent static/js folder
// One also needs to clear the cache of that browser page by Shift-F5 on Windows or CMD-Shirt-R on Mac
setTimeout(function () {
  $('#message').fadeOut('slow');
}, 3000);


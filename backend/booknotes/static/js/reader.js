window.addEventListener("scroll", moveScrollIndicator);

const scrollIndicatorElt = document.getElementsByClassName("progress");
const progressIndicatorElt = document.getElementById("progressIndicator");
const maxHeight = window.document.body.scrollHeight - window.innerHeight;
// const csrftoken = getCookie("csrftoken"); // Получение CSRF-токена
var id = pk;

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
  },
});

function moveScrollIndicator(e) {
  const percentage = (window.scrollY / maxHeight) * 100;
  for (let element of scrollIndicatorElt) {
    element.style.width = percentage + "%";
  }
  progressIndicatorElt.textContent = Math.round(percentage) + "%";
}

document.addEventListener("DOMContentLoaded", function (event) {
  $.ajax({
    url: "http://127.0.0.1:8001/api/books/" + id + "/",
    type: "GET",
    success: function (response) {
      console.log(response);
      var scrollpos = (response.get.book.reading_progress * maxHeight) / 100;
      window.scrollTo(0, scrollpos);
      console.log(scrollpos, window.scrollY);
      callout();
    },
  });
});

var set_delay = 2000,
  callout = function () {
    $.ajax({
      url: "http://127.0.0.1:8001/api/books/" + id + "/",
      data: {
        reading_progress: Math.round((window.scrollY * 100) / maxHeight),
      },
      type: "PATCH",
      success: function (response) {
        console.log("success", response.reading_progress);
      },
    })
      .done(function (response) {
        console.log("response: " + response);
      })
      .always(function () {
        setTimeout(callout, set_delay);
      });
  };

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = jQuery.trim(cookies[i]);
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break; // Выходим, как только найдём нужное cookie
      }
    }
  }
  return cookieValue;
}

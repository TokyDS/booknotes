window.addEventListener('scroll',
    moveScrollIndicator);

const scrollIndicatorElt =
document.getElementsByClassName('progress');
const progressIndicatorElt = document.getElementById('progressIndicator');
const maxHeight =
window.document.body.scrollHeight
- window.innerHeight;

function moveScrollIndicator(e) {
const percentage = 
    ((window.scrollY) / maxHeight) * 100;
    for (let element of scrollIndicatorElt){

        element.style.width = percentage + '%';
    }
    progressIndicatorElt.textContent = Math.round(percentage) + '%';

}

document.addEventListener("DOMContentLoaded", function (event) {
    var scrollpos = sessionStorage.getItem("scrollpos");
    if (scrollpos) {
      window.scrollTo(0, scrollpos);
      sessionStorage.removeItem("scrollpos");
    }
  });

  window.addEventListener("beforeunload", function (e) {
    id = pk
    $.ajax({
        url: '/api/books/${id}',
        data: {'reading_progress': window.scrollY},
        type: 'PATCH'
      }).done(function(response){
        console.log(response);
      });
  });
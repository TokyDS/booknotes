
window.onload = function() {
    var storedUsername = localStorage.getItem('username');
    if (storedUsername) {
        document.getElementById('displayUsername').textContent = storedUsername;
    } else {
        document.getElementById('displayUsername').textContent = 'Гость';
    }
};


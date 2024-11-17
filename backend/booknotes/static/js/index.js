
window.onload = function() {
    var storedUsername = localStorage.getItem('username');
    profile = document.getElementById('displayUsername');
    if (storedUsername) {
        profile.textContent = storedUsername;
    } else {
        profile.textContent = 'Гость';
        profile.href = '/login'
    }
};


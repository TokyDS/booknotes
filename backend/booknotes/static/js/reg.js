document.getElementById('registerButton').addEventListener('click', function() {
    var username = document.getElementById('username').value;
    localStorage.setItem('username', username);
    alert('Регистрация успешна! Теперь вы можете перейти на страницу профиля.');
    location.href = '/'; // Переход на страницу профиля
});


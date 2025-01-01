
document.getElementById('registerButton').addEventListener('click', function(e) {
    e.preventDefault(); // предотвращаем отправку формы

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const user = {
        username: username,
        email: email,
        password: password
    };

    // Сохраняем пользователя в localStorage
    localStorage.setItem('user', JSON.stringify(user));
    
    alert('Регистрация успешна!');
    window.location.href = 'signIn.html'; // Перенаправление на страницу входа
});


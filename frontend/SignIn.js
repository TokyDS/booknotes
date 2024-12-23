
document.querySelector('button[type="submit"]').addEventListener('click', function(e) {
    e.preventDefault(); // предотвращаем отправку формы

    const loginOrEmail = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    const user = JSON.parse(localStorage.getItem('user'));

    // Проверяем, существует ли пользователь и совпадают ли данные
    if (user && (user.username === loginOrEmail || user.email === loginOrEmail) && user.password === password) {
        alert('Вход успешен!');
        window.location.href = 'mainPage.html'; // Перенаправление на защищённую страницу
    } else {
        alert('Неверный логин или пароль');
    }
});


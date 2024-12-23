
window.onload = function() {
    var storedUsername = localStorage.getItem('username');
    if (storedUsername) {
        document.getElementById('displayUsername').textContent = storedUsername;
    } else {
        document.getElementById('displayUsername').textContent = 'Гость';
    }
};


document.addEventListener('DOMContentLoaded', function() {
    const savedBooks = JSON.parse(localStorage.getItem('books')) || [];
    const savedBooksList = document.getElementById('savedBooksList');

    savedBooks.forEach((book, index) => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="#" onclick="showBookContent(${index})">${book.name}</a>`;
        savedBooksList.appendChild(li);
    });
});

function showBookContent(index) {
    const savedBooks = JSON.parse(localStorage.getItem('books')) || [];
    const book = savedBooks[index];
    localStorage.setItem('currentBook', JSON.stringify(book));
    window.location.href = 'book.html'; // Перенаправляем на страницу с содержимым книги
}
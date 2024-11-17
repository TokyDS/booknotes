
const books = [];

function addBook() {
    const bookInput = document.getElementById('bookInput');
    const bookFile = document.getElementById('bookFile');
    const bookName = bookInput.value.trim();

    if (bookName && bookFile.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const bookContent = e.target.result;
            books.push({ name: bookName, content: bookContent });
            bookInput.value = '';
            bookFile.value = '';
            renderBookList();
        };
        reader.readAsText(bookFile.files[0]);
    } else {
        alert("Пожалуйста, заполните все поля.");
    }
}

function renderBookList() {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    books.forEach((book, index) => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="#" onclick="showBookContent(${index})">${book.name}</a>`;
        bookList.appendChild(li);
    });
}

function showBookContent(index) {
    const book = books[index];
    localStorage.setItem('currentBook', JSON.stringify(book));
    window.location.href = 'book.html'; // Перенаправляем на новую HTML-страницу
}


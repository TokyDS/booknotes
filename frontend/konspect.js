
document.getElementById('addButton').addEventListener('click', function() {
    const bookTitle = document.getElementById('bookTitle').value;
    const summaryText = document.getElementById('summary').value;

    if (bookTitle && summaryText) {
        const summaryContainer = document.createElement('div');
        summaryContainer.classList.add('summary-item');

        const titleElement = document.createElement('h2');
        titleElement.textContent = bookTitle;
        summaryContainer.appendChild(titleElement);

        const summaryElement = document.createElement('p');
        summaryElement.textContent = summaryText;
        summaryContainer.appendChild(summaryElement);

        const editButton = document.createElement('button');
        editButton.textContent = 'Редактировать';
        editButton.classList.add('edit-button');
        editButton.onclick = function() {
            const newBookTitle = prompt("Введите новое название книги", bookTitle);
            const newSummaryText = prompt("Введите новый конспект", summaryText);
            if (newBookTitle) titleElement.textContent = newBookTitle;
            if (newSummaryText) summaryElement.textContent = newSummaryText;
        };
        summaryContainer.appendChild(editButton);

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Удалить';
        deleteButton.classList.add('delete-button');
        deleteButton.onclick = function() {
            summaryContainer.remove();
        };
        summaryContainer.appendChild(deleteButton);

        document.getElementById('summaries').appendChild(summaryContainer);

        // Очистка полей ввода
        document.getElementById('bookTitle').value = '';
        document.getElementById('summary').value = '';
    } else {
        alert('Пожалуйста, заполните все поля.');
    }
});

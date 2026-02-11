'use strict';

const form = document.getElementById('todo-form');
const input = document.getElementById('todo-input');
const todoList = document.getElementById('todo-list');

const createTodoItem = (text) => {
  const listItem = document.createElement('li');
  listItem.classList.add('todo-item');

  const leftSection = document.createElement('div');
  leftSection.classList.add('todo-left');

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';

  const span = document.createElement('span');
  span.textContent = text;
  span.classList.add('todo-text');

  checkbox.addEventListener('change', () => {
    span.classList.toggle('done');
  });

  const deleteButton = document.createElement('button');
  deleteButton.textContent = '🗑️';
  deleteButton.classList.add('delete-btn');

  deleteButton.addEventListener('click', () => {
    listItem.remove(); // modern way
  });

  leftSection.appendChild(checkbox);
  leftSection.appendChild(span);

  listItem.appendChild(leftSection);
  listItem.appendChild(deleteButton);

  return listItem;
};

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const taskText = input.value.trim();

  if (!taskText) return;

  const todoItem = createTodoItem(taskText);
  todoList.appendChild(todoItem);

  input.value = '';
});

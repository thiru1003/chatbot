const topicForm = document.getElementById('topic-form');
const resultDiv = document.getElementById('result');

topicForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const topic = document.getElementById('topic').value;

  try {
    const response = await fetch('/result', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic })
    });

    const facts = await response.json();
    resultDiv.textContent = `Here are some interesting facts about ${topic}:`;
    resultDiv.appendChild(document.createElement('pre')).textContent = facts;
  } catch (error) {
    console.error(error);
    resultDiv.textContent = 'An error occurred. Please try again later.';
  }
});

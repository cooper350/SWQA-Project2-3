// Get the form element
const form = document.querySelector('form');

// Add an event listener for form submission
form.addEventListener('submit', (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();
    
    // Get the height and weight input values
    const height = parseInt(document.querySelector('#height').value);
    const weight = parseInt(document.querySelector('#weight').value);
    
    // Calculate the BMI
    const bmi = weight / ((height / 100) ** 2);
    
    // Display the BMI result
    document.querySelector('p').textContent = `Your BMI is ${bmi.toFixed(2)}`;
});

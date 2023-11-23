function validateDecimalNumber(input) {
    const regex = /^\d*\.?\d*$/;
    const value = input.value;
    if (!regex.test(value)) {
      input.setCustomValidity('Please enter a valid decimal number');
    } else {
      input.setCustomValidity('');
    }
  }
  
  
          function previewImage(event) {
              var imagePreview = document.getElementById('imagePreview');
              imagePreview.style.display = 'block';
              imagePreview.src = URL.createObjectURL(event.target.files[0]);
          }
  
          document.addEventListener("DOMContentLoaded", function() {
              var loginButton = document.getElementById("loginButton");
              loginButton.addEventListener("mouseenter", function() {
                  loginButton.innerHTML = "LOGOUT";
              });
      
              loginButton.addEventListener("mouseleave", function() {
                  loginButton.innerHTML = "Logged in as {{ user.username }}";
              });
      
              loginButton.addEventListener("click", function() {
                  window.location.href = "{% url 'homepage' %}";
              });
          });
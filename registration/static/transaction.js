document.addEventListener("DOMContentLoaded", function() {
    var loginButton = document.getElementById("loginButton");
    loginButton.addEventListener("mouseenter", function() {
        loginButton.innerHTML = "LOGOUT";
    });
    loginButton.addEventListener("click", function() {
        window.location.href = "{% url 'homepage' %}";
    });
});
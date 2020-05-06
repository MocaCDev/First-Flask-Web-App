window.onload = () => {
	let WelcomeHeader = document.getElementById('WelcomeHeader');
	// Making "About Page" for header of about.html
	let NewElement = document.createElement('h1');
	NewElement.innerText = "About Page";
	WelcomeHeader.appendChild(NewElement);
}
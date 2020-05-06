window.onload = (event) => {
	const NewElement = document.createElement('h1');
	NewElement.className = "NewElement";
	const Text = document.createTextNode('About Page');
	NewElement.appendChild(Text);
	console.log("LOADED");
}
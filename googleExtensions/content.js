document.addEventListener("DOMContentLoaded", function() {
    const logo = document.querySelector("img[alt='Google']");
    if (logo) {
        const textNode = document.createElement("div");
        textNode.innerText = "Aadesh";
        textNode.style.fontSize = "48px";
        textNode.style.fontWeight = "bold";
        textNode.style.color = "#4285F4";
        textNode.style.fontFamily = "Arial, sans-serif";
        textNode.style.position = "absolute";
        textNode.style.left = logo.offsetLeft + "px";
        textNode.style.top = logo.offsetTop + "px";
        logo.parentNode.replaceChild(textNode, logo);
    }
});

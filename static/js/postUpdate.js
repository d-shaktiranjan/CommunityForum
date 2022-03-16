let title = document.getElementById("title");
let about = document.getElementById("about");
let inputDiv = document.getElementById("inputDiv");
let submitButton = document.getElementById("submitButton");

const oldTitle = title.value;
const oldAbout = about.value;

submitButton.hidden = true;

inputDiv.addEventListener("keyup", () => {
    if (oldTitle != title.value || oldAbout != about.value) {
        submitButton.hidden = false;
    }
    else {
        submitButton.hidden = true;
    }
})

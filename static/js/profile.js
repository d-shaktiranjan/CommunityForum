let verifyForm = document.getElementById("verifyForm");
verifyForm.style.display = "none";

document.getElementById("verifyBtn").addEventListener("click", () => {
    // TODO:- make request to backend
    verifyForm.style.display = "block";
})
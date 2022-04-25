let verifyForm = document.getElementById("verifyForm");
verifyForm.style.display = "none";

document.getElementById("verifyBtn").addEventListener("click", () => {
    // TODO:- make request to backend
    fetch('http://127.0.0.1:8000/api/sendOTP').then((res) => {
        return res.json()
    }).then((data) => {
        console.log(data);
    })
    verifyForm.style.display = "block";
})
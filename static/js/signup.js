function typeCheck() {
    let userType = document.getElementById('student').checked;
    let uId = document.getElementById('uId');
    if (userType) {
        uId.placeholder = "Registration Number";
    } else {
        uId.placeholder = "Teacher Name";
    }
}

let passCheck = () => {
    let password = document.getElementById('password').value;
    let conPass = document.getElementById('conPassword').value;
    if (password.length < 5) {
        document.getElementById('conPassword').disabled = true;
    } else {
        document.getElementById('conPassword').disabled = false;
    }
    let btn = document.getElementById('submitBtn');
    let passMsg = document.getElementById('passMsg');
    if (password == conPass) {
        btn.disabled = false;
        passMsg.style.display = "none";
    } else {
        btn.disabled = true;
        passMsg.style.display = "block";
    }
}
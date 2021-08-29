let typeCheck = () => {
    let userType = document.getElementById('student').checked;
    let uId = document.getElementById('uId');
    if (userType) {
        uId.type = "number";
        uId.placeholder = "Registration Number";
    } else {
        uId.type = "text";
        uId.placeholder = "Teacher Name";
    }
}

let passCheck = () => {
    let password = document.getElementById('password').value;
    let conPass = document.getElementById('conPassword').value;
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

let passwordLength = () => {
    let password = document.getElementById('password').value;
    let alert = document.getElementById('passwordLength');
    if (password.length < 5) {
        document.getElementById('conPassword').disabled = true;
        alert.style.display = "block";
    } else {
        alert.style.display = "none";
        document.getElementById('conPassword').disabled = false;
    }
}
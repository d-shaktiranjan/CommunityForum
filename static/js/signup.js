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
    let btn = document.getElementById('submitBtn');
    let passMsg = document.getElementById('passMsg');
    if (password == conPass) {
        btn.disabled = false;
        passMsg.style.display = "none";
    } else {
        btn.disabled = true;
        passMsg.style.display = "block";
    }
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
}
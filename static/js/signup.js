function typeCheck() {
    let userType = document.getElementById('student').checked;
    let uId = document.getElementById('uId');
    if (userType) {
        uId.placeholder = "Registration Number";
    } else {
        uId.placeholder = "Teacher Name";
    }
}
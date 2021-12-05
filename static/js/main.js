/*===== MENU SHOW =====*/
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId)

    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('show')
        })
    }
}

showMenu('nav-toggle', 'nav-menu')

/*===== REMOVE MENU =====*/
const navLink = document.querySelectorAll('.nav__link'),
    navmenu = document.getElementById('nav-menu')

function linkAction() {
    navmenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*===== SCROLL SECTIONS ACTIVE LINK =====*/
const sections = document.querySelectorAll('section[id]')

window.addEventListener('scroll', scrollActive)

function scrollActive() {
    const scrollY = windows.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50
        sectionId = current.getAttribute('id')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.quesrySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active')
        } else {
            document.quesrySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active')
        }
    })
}

/*===== CHANGE COLOR HEADER =====*/
window.onscroll = () => {
    const nav = document.getElementById('header')
    if (this.scrollY >= 200) nav.classList.add(scroll - header); else nav.classList.remove('scroll-header')
}

/*===== Modal =====*/
const open = document.getElementById('open');
const close = document.getElementById('close');
const modal = document.getElementById('modal_container');
const modalTitle = document.getElementById("modal-title");
const confirmPass = document.getElementById("confirm-pass");
const loginBtn = document.getElementById("login-btn");
const createLink = document.getElementById("create-link");
const logName = document.getElementById("log-name");
const logForm = document.getElementById("login-form");


open.addEventListener('click', () => {
    modal.classList.add('show');
});

close.addEventListener('click', () => {
    modal.classList.remove('show');
    location.reload();
});

function signUp() {
    modalTitle.innerHTML = "Create an account";
    confirmPass.style.display = "block";
    confirmPass.value = "";
    loginBtn.innerHTML = "Sign Up";
    createLink.style.display = "none";
    logName.style.display = "block";
    logName.value = "";
    logForm.action = "/signup";
}
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
const opensign = document.getElementById('opensign');
const close = document.getElementById('close');
const closesign = document.getElementById('closesign');
const modal = document.getElementById('modal_container');
const modalsign = document.getElementById('modal_container-sign');


open.addEventListener('click', () => {
    modal.classList.add('show');
});

opensign.addEventListener('click', () => {
    modalsign.classList.add('show');
});

close.addEventListener('click', () => {
    modal.classList.remove('show');
    location.reload();
});

closesign.addEventListener('click', () => {
    modalsign.classList.remove('show');
    location.reload();
});
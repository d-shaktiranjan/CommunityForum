let isImage = document.getElementById("isImage");
let imageInput = document.getElementById("imageInput");
isImage.addEventListener("click", () => {
    if (isImage.checked == true) {
        imageInput.innerHTML = `<input type="file" name="postImage" accept="image/*" id="postImage" required />`;
    } else {
        imageInput.innerHTML = "";
    }
})
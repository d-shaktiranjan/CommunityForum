let isImage = document.getElementById("isImage");
let imageInput = document.getElementById("imageInput");
let submitButton = document.getElementById("submitButton");
isImage.addEventListener("click", () => {
    if (isImage.checked == true) {
        imageInput.innerHTML = `<input type="file" name="postImage" accept="image/*" id="postImage" required />
        <label for="postImage">
        <i class="fa-solid fa-upload"></i>
        Browse
        </label>`;
        submitButton.classList.add("post-submit-margin");
    } else {
        imageInput.innerHTML = "";
        submitButton.classList.remove("post-submit-margin");
    }
})
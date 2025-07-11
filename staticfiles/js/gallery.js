// static/js/gallery.js

function showImage(url) {
    const mainImage = document.getElementById('main-image');
    if (mainImage) mainImage.src = url;
}

function openFullscreen(imgElement) {
    if (!imgElement) return;
    if (imgElement.requestFullscreen) {
        imgElement.requestFullscreen();
    } else if (imgElement.webkitRequestFullscreen) {
        imgElement.webkitRequestFullscreen();
    } else if (imgElement.msRequestFullscreen) {
        imgElement.msRequestFullscreen();
    }
}

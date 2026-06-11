var skinManager = document.getElementById("skinManager")

skinManager.onsubmit = function () {
    var skinNameInputBox = document.getElementById("skin")
    var skinDownloadButton = document.getElementById("skin-download")
    var skinName = skinNameInputBox.value

    var skinViewer = document.getElementById("skinViewer")

    var url = "https://kurojs.github.io/McView3D/embed.html?skin=Steve&width=400&height=400&animation=idle"

    var url_skin = "https://minotar.net/skin/Steve"

    url = url.replace("Steve", skinName)
    url_skin = url_skin.replace("Steve", skinName)
    skinViewer.setAttribute("src", url)
    skinDownloadButton.setAttribute("href", url_skin)
    console.log("Skin changed to" + " " + skinName)

    return false
}
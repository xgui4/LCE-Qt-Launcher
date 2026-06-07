var skinManager = document.getElementById("skinManager")

skinManager.onsubmit = function() {
    var skinNameInputBox = document.getElementById("skin")
    var skinName = skinNameInputBox.value
    var skinViewer = document.getElementById("skinViewer")

    var url = "https://kurojs.github.io/McView3D/embed.html?skin=Steve&width=400&height=400&animation=idle"

    url = url.replace("Steve", skinName)
    skinViewer.setAttribute("src", url)
    console.log("Skin changed to" + " " + skinName)

    return false
}
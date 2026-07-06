
/*
LCE Qt Launcher Website
Copyright (C) 2026 Xgui4

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see https://www.gnu.org/licenses/.
*/

var skinViewer = document.createElement("iframe")
skinViewer.setAttribute("id", "skin-viewer")
skinViewer.setAttribute("src", "https://kurojs.github.io/McView3D/embed.html?skin=Steve&width=400&height=400&animation=idle")
skinViewer.setAttribute("width", "400")
skinViewer.setAttribute("height", "400")

document.getElementsByTagName("body")[0].appendChild(skinViewer)

var br = document.createElement("br"); 

var form = document.createElement("form");
form.setAttribute("method", "post");
form.setAttribute("action", "");
form.setAttribute("id", "skinManager")

var skinLabel = document.createElement("label");
skinLabel.setAttribute("for", "skin");
skinLabel.innerText = "Minecraft Username"

var skin = document.createElement("input");
form.setAttribute("id", "skin")
skin.setAttribute("type", "text");
skin.setAttribute("name", "skin");
skin .setAttribute("value", "Steve");

var s = document.createElement("input");
s.setAttribute("type", "submit");
s.setAttribute("value", "See the skin");

form.appendChild(skinLabel); 
form.appendChild(br.cloneNode()); 

form.appendChild(skin); 
form.appendChild(br.cloneNode()); 

form.appendChild(s); 

document.getElementsByTagName("body")[0]
.appendChild(form);

form.onsubmit = function () {
    var skinDownloadButton = document.getElementById("skin-download")
    var skinName = skin.value

    var url = "https://kurojs.github.io/McView3D/embed.html?skin=Steve&width=400&height=400&animation=idle"
    var url_skin = "https://minotar.net/skin/Steve"

    url = url.replace("Steve", skinName)
    url_skin = url_skin.replace("Steve", skinName)
    skinViewer.setAttribute("src", url)
    skinDownloadButton.setAttribute("href", url_skin)

    return false
}
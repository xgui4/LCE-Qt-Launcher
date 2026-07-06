/*
LCE Qt Launcher Shop
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

let contents = {};

fetch('https://code.nolog.cz/xgui4/lce-qt-launcher-data/raw/commit/52132c4e2b8c662b34943aa489f0c747a9846eb8/database.json')
  .then(response => response.json())
  .then(data => {
    contents = data;            
    
    contents.forEach(element => {
      console.log("name :", element["name"])
      console.log("version :", element["version"])
      console.log("icon :", element["icon"])
      console.log("instance_file :", element["instance_file"])
      console.log("background :", element["background"])
      console.log("type :", element["type"])
    });
    
  })
  .catch(err => console.error(err));

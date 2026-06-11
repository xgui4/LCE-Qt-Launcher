let contents = {};

fetch('https://code.nolog.cz/xgui4/lce-qt-launcher-data/raw/branch/master/database.json')
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

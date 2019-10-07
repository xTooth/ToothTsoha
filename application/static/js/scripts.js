function postEditToggle() {
    var formdiv = document.getElementById("postEditForm");
    var button = document.getElementById("postEditFormButton");
    if (formdiv.style.display === "none") {
      formdiv.style.display = "block";
      button.style.display = "none";
    } else {
      formdiv.style.display = "none";
      button.style.display = "block";
    }
  }

  function commentEditToggle(commentId) {
    var formdiv = document.getElementById(commentId);
    var button = document.getElementById("commentEditFormButton");
    if (formdiv.style.display === "none") {
      formdiv.style.display = "block";
      button.style.display = "none";
    } else {
      formdiv.style.display = "none";
      button.style.display = "block";
    }
  }
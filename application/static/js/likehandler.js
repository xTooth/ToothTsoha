
function like(id,counter){
  document.getElementById("add"+counter).style.display = "none";
  document.getElementById("remove"+counter).style.display = "block";
  $('.count' + counter).html(parseInt($('.count' + counter).html(), 10)+1)
    $.post(id);
    
    
}

function dislike(id,counter){
    document.getElementById("add"+counter).style.display = "block";
    document.getElementById("remove"+counter).style.display = "none";
    $('.count' + counter).html(parseInt($('.count' + counter).html(), 10)-1)
    $.post(id)
}

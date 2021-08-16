const previews=document.getElementsByClassName('htotext');

Array.from(previews).forEach((element)=>{
    element.innerHTML=element.innerText;
      })
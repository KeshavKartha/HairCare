let stack1= document.getElementById("stack1")
let stack2= document.getElementById("stack2")
let stack3= document.getElementById("stack3")


window.addEventListener("scroll",()=>{
    let value=window.scrollY;

    stack1.style.left=value* -0.5 + "px";
   
    stack2.style.top=value* 0.1 + "px";
    stack3.style.top=value* 0.2 + "px";
   
   
});

